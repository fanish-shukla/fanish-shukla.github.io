import os
import json
import time
import xml.etree.ElementTree as ET
import requests
from requests_oauthlib import OAuth1

FEED_URL = "https://fanish.shukla.eu/feed.xml"
STATE_FILE = "data/posted-items.json"


def load_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE) as f:
            return json.load(f)
    return {"posted": []}


def save_state(state):
    os.makedirs(os.path.dirname(STATE_FILE), exist_ok=True)
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)


def fetch_feed_items():
    resp = requests.get(FEED_URL, timeout=30)
    resp.raise_for_status()
    root = ET.fromstring(resp.content)
    channel = root.find("channel")
    items = []
    for item in channel.findall("item"):
        title = (item.findtext("title") or "").strip()
        link = (item.findtext("link") or "").strip()
        guid = (item.findtext("guid") or link).strip()
        items.append({"title": title, "link": link, "guid": guid})
    return items


def post_to_twitter(title, link):
    auth = OAuth1(
        os.environ["TWITTER_API_KEY"],
        os.environ["TWITTER_API_SECRET"],
        os.environ["TWITTER_ACCESS_TOKEN"],
        os.environ["TWITTER_ACCESS_TOKEN_SECRET"],
    )
    text = f"{title}\n\n{link}"
    if len(text) > 280:
        text = text[:275] + "…"
    resp = requests.post(
        "https://api.twitter.com/2/tweets",
        auth=auth,
        json={"text": text},
        timeout=30,
    )
    resp.raise_for_status()
    print("Posted to X:", resp.json())


def post_to_linkedin(title, link):
    token = os.environ["LINKEDIN_ACCESS_TOKEN"]
    person_urn = os.environ["LINKEDIN_PERSON_URN"]
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "X-Restli-Protocol-Version": "2.0.0",
    }
    body = {
        "author": person_urn,
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {"text": f"{title}\n\n{link}"},
                "shareMediaCategory": "ARTICLE",
                "media": [{"status": "READY", "originalUrl": link}],
            }
        },
        "visibility": {"com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"},
    }
    resp = requests.post(
        "https://api.linkedin.com/v2/ugcPosts", headers=headers, json=body, timeout=30
    )
    resp.raise_for_status()
    print("Posted to LinkedIn:", resp.status_code)


def post_to_facebook(title, link):
    page_id = os.environ["FACEBOOK_PAGE_ID"]
    token = os.environ["FACEBOOK_PAGE_ACCESS_TOKEN"]
    resp = requests.post(
        f"https://graph.facebook.com/{page_id}/feed",
        data={"message": title, "link": link, "access_token": token},
        timeout=30,
    )
    resp.raise_for_status()
    print("Posted to Facebook:", resp.json())


def main():
    state = load_state()
    posted_ids = set(state["posted"])
    items = fetch_feed_items()

    new_items = [i for i in items if i["guid"] not in posted_ids]
    new_items.reverse()  # oldest new item first, so ordering feels natural

    if not new_items:
        print("No new posts since last run.")
        return

    for item in new_items:
        print("New post found:", item["title"])
        errors = []

        try:
            post_to_twitter(item["title"], item["link"])
        except Exception as e:
            errors.append(f"X/Twitter failed: {e}")

        try:
            post_to_linkedin(item["title"], item["link"])
        except Exception as e:
            errors.append(f"LinkedIn failed: {e}")

        try:
            post_to_facebook(item["title"], item["link"])
        except Exception as e:
            errors.append(f"Facebook failed: {e}")

        # Mark as posted even if a platform failed, so we don't retry-spam
        # the platforms that DID succeed on the next run.
        posted_ids.add(item["guid"])
        state["posted"] = sorted(posted_ids)
        save_state(state)

        if errors:
            print("Some platforms failed for this post:")
            for e in errors:
                print(" -", e)

        time.sleep(2)


if __name__ == "__main__":
    main()
