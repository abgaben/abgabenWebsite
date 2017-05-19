---
layout: page
permalink: /news/
title: News
excerpt_separator: ""
---

<div id="archives">
    
    <a name="{{ category_name | slugize }}"></a>
    {% for post in site.posts %}
    <article class="archive-item">
    <p>
      <h4>{{ post.date | date_to_string  }} </h4> 
      {{ post.content }}
    </p>
    </article>
    {% endfor %}
</div>