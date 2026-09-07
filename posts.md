---
title: "All Posts"
layout: single
permalink: /posts/
author_profile: true
---

{% include blog-sidebar.html %}

{% for post in site.posts %}
### [{{ post.title }}]({{ post.url | relative_url }})

<p style="color:#888; font-size:0.85em; margin-top:-0.5em;">{{ post.date | date: "%B %d, %Y" }}{% if post.categories.size > 0 %} · {{ post.categories | join: ", " }}{% endif %}</p>

{{ post.excerpt | strip_html | truncatewords: 30 }}

[Read more →]({{ post.url | relative_url }})

---
{% endfor %}
