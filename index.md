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
korrigierten Form hochgeladen. Insbesondere sind die Abgabe in der
Regel nach der Korrektur nicht durch uns verbessert worden!

Wir veröffentlichen hier ausserdem LaTeX-Snippets, welche wir als für die
allgemeinheit nützlich erachten.


Aktuell sind folgende Kategorien verfügbar:

*Um die Übersichtlichkeit zu verbessern sind module in denen keine neuen
Abgaben mehr hinzu kommen auf eigene Seiten ausgelagert.*
## SS 2017
### [Datenstrukturen und Algorithmen]({{ site.baseurl }})
<div id="archives">
{% assign ss17 = "BuS|LA|FoSAP" | split: "|" %}
{% for category_name in ss17 %}
  <div class="archive-group">
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

<div class="archive-group">
  <div id="#{{ category_name | slugize }}"></div>
  <p></p>   
  <h3 class="category-head">LaTeX-Snippets</h3>
  <a name="{{ category_name | slugize }}"></a>
  {% for post in site.categories["LaTeX"] %}
  <article class="archive-item">
    <h4><a href="{{ site.baseurl }}{{ post.url }}">{{post.title}}</a></h4>
  </article>
  {% endfor %}
</div>
