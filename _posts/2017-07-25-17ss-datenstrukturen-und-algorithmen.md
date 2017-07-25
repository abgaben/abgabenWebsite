---
layout: post
title: 'Datenstrukturen und Algorithmen'
date: 2017-07-25 23:20:42
category: 17SS
tags: [SS-17, 17SS]
---

Dies ist der Eintrag zu **Datenstrukturen und Algorithmen** im
Sommersemester 2017, gehalten von Prof. Dr. Ir. Gerhard Woeginger.

[Website](https://algo.rwth-aachen.de/Lehre/SS17/DSA.php) zur
Vorlesung (solange sie noch Online ist)

### Abgaben
  <div class="archive-group">
    <a name="{{ category_name | slugize }}"></a>
    {% for post in site.categories["DSAL"] %}
    <article class="archive-item">
      <h4><a href="{{ site.baseurl }}{{ post.url }}">{{post.title}}</a></h4>
    </article>
    {% endfor %}
  </div>