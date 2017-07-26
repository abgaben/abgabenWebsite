---
layout: post
title: 'Lineare Algebra'
date: 2017-07-26 17:27:19
category: 17SS
tags: [SS-17, 17SS]
---

Dies ist der Eintrag zu **Lineare Algebra für Informatiker** im
Sommersemester 2017, gehalten von Dr. Sebastian Thomas.

[Website](https://www2.math.rwth-aachen.de/LAInf17/) zur
Vorlesung (solange sie noch Online ist)

### Abgaben
  <div class="archive-group">
    <a name="{{ category_name | slugize }}"></a>
    {% for post in site.categories["LA"] %}
    <article class="archive-item">
      <h4><a href="{{ site.baseurl }}{{ post.url }}">{{post.title}}</a></h4>
    </article>
    {% endfor %}
  </div>