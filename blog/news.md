---
layout: page
permalink: /news/
title: News
---

<div id="archives">
    
    <a name="{{ category_name | slugize }}"></a>
    {% for post in site.posts %}
    <article class="archive-item">
      <h4><a href="{{ site.baseurl }}{{ post.url }}">{{post.title}}</a></h4>
    </article>
    {% endfor %}
</div>