---
# You don't need to edit this file, it's empty on purpose.
# Edit theme's home layout instead if you wanna make some changes
# See: https://jekyllrb.com/docs/themes/#overriding-theme-defaults
layout: page
---
Auf dieser Website veröffentlichen wir, das sind ([Adrian](mailto:adrian.hinrichs@rwth-aachen.de)
und [Georg](mailto:georg.dorndorf@rwth-aachen.de)), alle PDFs, die während
unseres Studiums im Fach Informatik an der RWTH Aachen von uns
erstellt werden.

Alle auf dieser Seite veröffentlichten Lösungen zu den entsprechenden
Hausaufgaben sind möglicherweise unvollständig und/oder falsch. Falls
es nicht anders angemerkt ist, sind die Abgaben nicht in der durch einen Tutor
korrigierten Form hochgeladen.

Aktuell sind folgende Kategorien verfügbar:

## SS 2017
<div id="archives">
{% for category in site.categories %}
  <div class="archive-group">
    {% capture category_name %}{{ category | first }}{% endcapture %}
    <div id="#{{ category_name | slugize }}"></div>
    <p></p>
    
    <h3 class="category-head">{{ category_name }}</h3>
    <a name="{{ category_name | slugize }}"></a>
    {% for post in site.categories[category_name] %}
    <article class="archive-item">
      <h4><a href="{{ site.baseurl }}{{ post.url }}">{{post.title}}</a></h4>
    </article>
    {% endfor %}
  </div>
{% endfor %}
</div>
