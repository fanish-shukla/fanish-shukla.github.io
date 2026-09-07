---
title: "Fanish Shukla"
layout: single
permalink: /
author_profile: true
---

{% include blog-sidebar.html %}

Welcome. I'm a Solution Architect with a background in enterprise architecture in aviation, including work with SWISS International Air Lines and the Lufthansa Group Enterprise Architecture team. This blog shares practical enterprise architecture thinking, starting with a 10-part series on ArchiMate relationships.

## Latest Posts

{% for post in site.posts limit:5 %}
### [{{ post.title }}]({{ post.url | relative_url }})

<p style="color:#888; font-size:0.85em; margin-top:-0.5em;">{{ post.date | date: "%B %d, %Y" }}{% if post.categories.size > 0 %} · {{ post.categories | join: ", " }}{% endif %}</p>

{{ post.excerpt | strip_html | truncatewords: 40 }}

[Read more →]({{ post.url | relative_url }})

---
{% endfor %}

<div style="text-align:center; margin-top:1.5em; clear:both;">
  <a href="{{ '/posts/' | relative_url }}" class="btn btn--primary btn--large">Show More Posts</a>
</div>
