---
title: "All Posts"
layout: single
permalink: /posts/
author_profile: true
---

{% include blog-sidebar.html %}

<div class="entries-grid">
  {% for post in site.posts %}
    {% include archive-single.html type="grid" %}
  {% endfor %}
</div>
