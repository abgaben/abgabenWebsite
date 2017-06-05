---
layout: default
title: 'FoSAP Blatt 3'
date: 2017-05-23 13:55:00
category: FoSAP
tags: [SS-17, FoSAP]
---

Die dritte Abgabe in FoSAP.

[Uebungsblatt 3]({{ site.baseurl }}/assets/fosap/uebungsblatt3.pdf)

Die Implementation des in Aufgabe 6 geforderten Algorithmus, der
endliche reguläre Ausdrücke erkennt.

```Haskell
f :: [Char] -> Bool -> Bool
f (')':ss:s) b = b && if ss=='0' then (f ('0':s) True) else (f ('a':ss:s) True)
f (')':s) b = b && (f ('a':s) b)
f ('+':s) b = b && (f s b)
f ('0':s) _ = f s True
f ('0':'*':s) _ = f s True

f ('E':s) _ = f s True
f (a:'*':[]) _ = False
f (a:'*':s:ss:sss) b = if (s=='0') then (f (ss:sss) True)
                       else (if (s==')' && ss == '0') then (f sss True )
                        else (b && (f (s:ss:sss) False)))
f (a:'?':s) _ = f (a:a:"*") False && (f s True)
```