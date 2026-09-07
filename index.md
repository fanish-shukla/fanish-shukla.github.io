---
layout: default
title: Home
---

<div class="post-layout">
  <div class="main-content">
    <h1>Latest Insights</h1>
    <ul class="post-list">
      {% for post in site.posts %}
        <li style="margin-bottom: 25px;">
          <span class="post-meta">{{ post.date | date: "%b %d, %Y" }}</span>
          <h3>
            <a class="post-link" href="{{ post.url | relative_url }}">{{ post.title | escape }}</a>
          </h3>
          <p>{{ post.excerpt | strip_html | truncatewords: 30 }}</p>
        </li>
      {% endfor %}
    </ul>
  </div>

  <div class="sidebar-right">
    <h3>Feeds & RSS</h3>
    <p>Subscribe to updates directly via RSS or follow recent architectural topics:</p>
    <ul>
      <li><a href="{{ '/feed.xml' | relative_url }}" target="_blank">📡 RSS Feed</a></li>
      <li><a href="https://linkedin.com" target="_blank">💼 LinkedIn Updates</a></li>
    </ul>
    <hr>
    <h4>Categories</h4>
    <ul>
      <li>Enterprise Architecture</li>
      <li>ArchiMate 3.0</li>
      <li>Aviation Tech</li>
    </ul>
  </div>
</div>
