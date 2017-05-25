---
layout: post
title: 'LaTeX-Snippet: Heapsort'
date: 2017-05-23 10:38:00
category: LaTeX
tags: [LaTeX]
---

LaTeX-Schnipsel zur Visualisierung von Sortierungsalgorithmen
(z.B. Aufgabe 4 von [DSAL Abgabe 3]({{ site.baseurl
}}/dsal/2017/05/16/dsal-blatt-3.html))

Benötigte Pakete sowie benutzte Style Settings:
```LaTeX
\usepackage{tikz}
\usetikzlibrary{shapes,arrows,positioning,decorations,
  automata,backgrounds,petri,bending,
  shapes.multipart
} %Eventuell sind nicht alle nötig
\usepackage{pgf}

\tikzset{
  treenode/.style = {shape=circle, rounded corners,
    draw, align=center},
  graynode/.style = {fill=gray},
  normal/.style     = {treenode, font=\Large, bottom color=white}
  }
```
```LaTeX
\begin{figure}[H]
  \centering
  \subfloat[Heap vor dem Sortieren.]
  {
    \begin{tikzpicture}
      [
      sibling distance        = 3em,
      level distance          = 3em,
      edge from parent/.style = {draw, -latex},
      every node/.style       = {font=\footnotesize},
      level 1/.style={sibling distance=6em},
      level 2/.style={sibling distance=3em},
      sloped
      ]
      \node [treenode] {5}
      child {node [treenode] {7}
        child {node [treenode] {4}}
        child {node [treenode] {2}}}
      child {node [treenode] {97}
        child {node [treenode] {42}}
        child[fill=none] {edge from parent[draw=none]}};
      
      
    \end{tikzpicture}
  }
  \subfloat[Heap-Array vor dem sortieren.]
  {
    \begin{tikzpicture}
      \node[array, name = array, rectangle split parts=6,draw] at (0,1)
      {\nodepart{one}5
        \nodepart{two}7
        \nodepart{three}97
        \nodepart{four}4
        \nodepart{five}2
        \nodepart{six}42
      };
      \draw [<->] (array.one north) |- ++(0,0.4) -| (array.three north);
    \end{tikzpicture}
  }
  
  \subfloat[Heap vor dem Sortieren.]
  {
    \begin{tikzpicture}
      [
      sibling distance        = 6em,
      level distance          = 3em,
      edge from parent/.style = {draw, -latex},
      every node/.style       = {font=\footnotesize},
      level 1/.style={sibling distance=6em},
      level 2/.style={sibling distance=3em},
      sloped
      ]
      \node [treenode] {97}
      child {node [treenode] {7}
        child {node [treenode] {4}}
        child {node [treenode] {2}}}
      child {node [treenode] {5}
        child {node [treenode](left node) {42}}
        child[fill=none] {edge from parent[draw=none]}};
      
      
    \end{tikzpicture}
  }
  \subfloat[Heap-Array vor dem sortieren.]
  {
    \begin{tikzpicture}
      \node[array, name=array, rectangle split parts=6] at (0,1)
      {\nodepart{one}97
        \nodepart{two}7
        \nodepart{three}5
        \nodepart{four}4
        \nodepart{five}2
        \nodepart{six}42
      };
      \draw [<->] (array.three north) |- ++(0,0.4) -| (array.six north);
    \end{tikzpicture}
  }
  
  \caption[Heap Aufbau]{Aufbau des Heaps }
  \label{fig:a6_heapsort_1}
\end{figure}
```