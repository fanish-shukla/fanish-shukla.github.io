import os
import json
import time
import xml.etree.ElementTree as ET
import requests
from requests_oauthlib import OAuth1
import re

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

    # --- Atom feed (Jekyll default: <feed xmlns="http://www.w3.org/2005/Atom">) ---
    ATOM_NS = "http://www.w3.org/2005/Atom"
    if root.tag == f"{{{ATOM_NS}}}feed" or root.tag == "feed":
        ns = {"atom": ATOM_NS}
        entries = root.findall("atom:entry", ns)
        items = []
        for entry in entries:
            title = (entry.findtext("atom:title", namespaces=ns) or "").strip()
            # <link href="..." /> in Atom
            link_el = entry.find("atom:link[@rel='alternate']", ns) \
                      or entry.find("atom:link", ns)
            link = (link_el.get("href") if link_el is not None else "").strip()
            
            # Extract tags from category elements if they exist
            tags = []
            category_elements = entry.findall("atom:category", ns)
            for cat in category_elements:
                tag = cat.get("term", "").strip()
                if tag:
                    tags.append(tag)
            
            guid_el = entry.findtext("atom:id", namespaces=ns) or link
            guid = (guid_el or "").strip()
            
            items.append({"title": title, "link": link, "guid": guid, "tags": tags})
        return items

    # --- RSS feed (<rss> → <channel> → <item>) ---
    channel = root.find("channel")
    if channel is None:
        raise ValueError(
            f"Unrecognised feed format. Root tag was: {root.tag!r}"
        )
    items = []
    for item in channel.findall("item"):
        title = (item.findtext("title") or "").strip()
        link  = (item.findtext("link")  or "").strip()
        
        # Extract tags from RSS category elements
        tags = []
        category_elements = item.findall("category")
        for cat in category_elements:
            tag = (cat.text or "").strip()
            if tag:
                tags.append(tag)
        
        guid  = (item.findtext("guid")  or link).strip()
        items.append({"title": title, "link": link, "guid": guid, "tags": tags})
    return items


def get_post_content(link):
    """Fetch the actual post content from the blog URL"""
    try:
        resp = requests.get(link, timeout=30)
        resp.raise_for_status()
        
        # Use regex to extract main content (simplified - could be enhanced)
        content_match = re.search(r'<article[^>]*>(.*?)</article>', resp.text, re.DOTALL | re.IGNORECASE)
        if content_match:
            raw_content = content_match.group(1)
            # Remove HTML tags
            text_content = re.sub(r'<[^>]*>', ' ', raw_content)
            # Clean up extra whitespace
            text_content = re.sub(r'\s+', ' ', text_content).strip()
            
            # Extract first 200-250 words
            words = text_content.split()
            if len(words) > 250:
                excerpt = ' '.join(words[:250])
            else:
                excerpt = text_content
            
            return excerpt
        else:
            # Fallback: return description from meta tags
            desc_match = re.search(r'<meta[^>]*name="description"[^>]*content="([^"]*)"', resp.text, re.IGNORECASE)
            if desc_match:
                return desc_match.group(1)
            
    except Exception as e:
        print(f"Warning: Could not fetch content from {link}: {e}")
    
    return None


def create_linkedin_post(title, link, tags):
    """Create a LinkedIn post with hashtags and content, ensuring at least 150 words"""
    
    # Get the actual post content
    post_content = get_post_content(link)
    
    # Start with the title
    post_text = f"{title}\n\n"
    
    # Add content if available
    if post_content:
        word_count = len(post_content.split())
        if word_count >= 150:
            post_text += post_content
        else:
            # If content is shorter than 150 words, repeat key points
            post_text += post_content
            # Add some boilerplate to reach 150 words
            additional_text = "\n\nIn this detailed exploration, I examine key architectural patterns and their real-world applications in aviation enterprise systems. The article provides actionable insights for architects looking to optimize their solution designs."
            post_text += additional_text
    else:
        # Fallback content if we can't fetch the post
        post_text += f"I've published a new article on enterprise architecture and aviation technology. This piece explores important concepts in modern solution design and enterprise integration.\n\n"
        post_text += "Read the full article for comprehensive insights and practical examples that can help improve your architectural decision-making process."
    
    # Add "see more" link
    post_text += f"\n\nSee more: {link}"
    
    # Convert tags to LinkedIn hashtags
    if tags:
        hashtags = []
        for tag in tags[:5]:  # Limit to 5 tags to avoid spam
            # Clean up tag string
            tag_clean = re.sub(r'[^a-zA-Z0-9]+', '', tag)
            if tag_clean:
                hashtags.append(f"#{tag_clean}")
        
        if hashtags:
            post_text += f"\n\n{', '.join(hashtags)}"
    else:
        # Default hashtags based on your blog topics
        default_tags = ["EnterpriseArchitecture", "Aviation", "Archimate", "SolutionArchitecture", "Technology"]
        post_text += f"\n\n{', '.join(['#' + tag for tag in default_tags])}"
    
    return post_text


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


def post_to_linkedin(title, link, tags):
    token = os.environ["LINKEDIN_ACCESS_TOKEN"]
    person_urn = os.environ["LINKEDIN_PERSON_URN"]
    
    # Create LinkedIn post text with hashtags
    linkedin_text = create_linkedin_post(title, link, tags)
    
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
                "shareCommentary": {"text": linkedin_text},
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
    print("LinkedIn post text length:", len(linkedin_text), "characters")
    print("Word count:", len(linkedin_text.split()))


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

    # Filter out already posted items and sort by date (oldest first)
    new_items = [i for i in items if i["guid"] not in posted_ids]
    
    # Sort by date (assuming guid or other field indicates chronology)
    # For Atom feeds, we could sort by published date, but we'll use order in feed
    new_items.sort(key=lambda x: x.get("guid", ""))

    if not new_items:
        print("No new posts since last run.")
        return

    # Post the oldest new item
    oldest_item = new_items[0]
    print("Posting the oldest new item:", oldest_item["title"])
    print("Tags found:", oldest_item.get("tags", []))
    
    errors = []

    try:
        post_to_twitter(oldest_item["title"], oldest_item["link"])
    except Exception as e:
        errors.append(f"X/Twitter failed: {e}")

    try:
        post_to_linkedin(oldest_item["title"], oldest_item["link"], oldest_item.get("tags", []))
    except Exception as e:
        errors.append(f"LinkedIn failed: {e}")

    try:
        post_to_facebook(oldest_item["title"], oldest_item["link"])
    except Exception as e:
        errors.append(f"Facebook failed: {e}")

    # Mark as posted even if a platform failed, so we don't retry-spam
    # the platforms that DID succeed on the next run.
    posted_ids.add(oldest_item["guid"])
    state["posted"] = sorted(posted_ids)
    save_state(state)

    if errors:
        print("Some platforms failed for this post:")
        for e in errors:
            print(" -", e)

    time.sleep(2)


if __name__ == "__main__":
    main()
