---
layout: post
title: 'LaTeX-Snippet: Mergesort'
date: 2017-05-22 20:42:00
category: LaTeX
tags: [LaTeX]
---

LaTeX-Schnipsel zur Visualisierung von Sortierungsalgorithmen
(z.B. Aufgabe 5 von [DSAL Abgabe 3]({{ site.baseurl }}/dsal/2017/05/16/dsal-blatt-3.html))

```LaTeX
\begin{tikzpicture}[ level 1/.style={sibling distance=30mm}, level
  2/.style={sibling distance=30mm}, level 3/.style={sibling
    distance=20mm}]
  % Layer 0
  \node[array,rectangle split parts=9] at (-0.25,0)
  {14
    \nodepart{two}97
    \nodepart{three}7
    \nodepart{four}42
    \nodepart{five}12
    \nodepart{six}3
    \nodepart{seven}5
    \nodepart{eight}2
    \nodepart{nine}7 };

  % Layer 1
  \node[style=array, rectangle split parts=5,color=gray] at (-1.9,-1)
  {14
    \nodepart{two}97
    \nodepart{three}7
    \nodepart{four}42
    \nodepart{five}12
  };
  \node[array,rectangle split parts=4,color=gray] at (1.75,-1)
  {3
    \nodepart{two}5
    \nodepart{three}2
    \nodepart{four}7};

  % Layer 2
  \node[array, rectangle split parts=3,color=gray] at (-2.75,-2)
  {14
    \nodepart{two}97
    \nodepart{three}7
  };
  \node[array, rectangle split parts=2,color=gray] at (-.9,-2)
  {42
    \nodepart{two}12
  };
  \node[array,rectangle split parts=4, draw,color=gray] at (1.75,-2)
  {3
    \nodepart{two}5
    \nodepart{three}2
    \nodepart{four}7};
  
  % Layer 3
  \node[array, rectangle split parts=2,color=gray] at (-3.3,-3)
  {14
    \nodepart{two}97
  };
  \node[array, rectangle split parts=1,color=gray] at (-2.2,-3)
  {7};
  \node[array, rectangle split parts=2,color=gray] at (-.9,-3)
  {42
    \nodepart{two}12
  };
  \node[array,rectangle split parts=4, draw,color=gray] at (1.75,-3)
  {3
    \nodepart{two}5
    \nodepart{three}2
    \nodepart{four}7
  };
  
  
  % Layer 4
  \node[array, rectangle split parts=1,color=gray] at (-3.75,-4)
  {14
  };
  \node[array, rectangle split parts=1,color=gray] at (-3,-4)
  {97};
  \node[array, rectangle split parts=1,color=gray] at (-2.2,-4)
  {7};
  \node[array, rectangle split parts=2,color=gray] at (-.9,-4)
  {42
    \nodepart{two}12
  };
  \node[array,rectangle split parts=4,color=gray] at (1.75,-4)
  {3
    \nodepart{two}5
    \nodepart{three}2
    \nodepart{four}7
  };

  % Layer 5
  \node[array, rectangle split parts=2] at (-3.3,-5)
  {14
    \nodepart{two}97
  };
  \node[array, rectangle split parts=1] at (-2.2,-5)
  {7};
  \node[array, rectangle split parts=2] at (-.9,-5)
  {42
    \nodepart{two}12
  };
  \node[array,rectangle split parts=4, draw] at (1.75,-5)
  {3
    \nodepart{two}5
    \nodepart{three}2
    \nodepart{four}7
  };

  % Layer 6
  \node[array, rectangle split parts=3] at (-2.75,-6)
  {7
    \nodepart{two}14
    \nodepart{three}97
  };
  \node[array, rectangle split parts=2] at (-.9,-6)
  {42
    \nodepart{two}12
  };
  \node[array,rectangle split parts=4, draw] at (1.75,-6)
  {3
    \nodepart{two}5
    \nodepart{three}2
    \nodepart{four}7
  };

  % Layer 7
  \node[array, rectangle split parts=3, color=gray] at (-2.75,-7)
  {7
    \nodepart{two}14
    \nodepart{three}97
  };
  \node[array, rectangle split parts=1, color=gray] at (-1.3,-7)
  {42};
  \node[array,rectangle split parts=1, color=gray] at (-.5,-7)
  {12 };
  \node[array,rectangle split parts=4, color=gray] at (1.75,-7)
  {3
    \nodepart{two}5
    \nodepart{three}2
    \nodepart{four}7
  };

  % Layer 8
  \node[array, rectangle split parts=3] at (-2.75,-8)
  {7
    \nodepart{two}14
    \nodepart{three}97
  };
  \node[array, rectangle split parts=2] at (-.9,-8)
  {12
    \nodepart{two}42
  };
  \node[array,rectangle split parts=4, draw] at (1.75,-8)
  {3
    \nodepart{two}5
    \nodepart{three}2
    \nodepart{four}7
  };

  % Layer 9
  \node[style=array, rectangle split parts=5] at (-1.9, -9)
  {7
    \nodepart{two}12
    \nodepart{three}14
    \nodepart{four}42
    \nodepart{five}97
  };
  \node[array,rectangle split parts=4, draw] at (1.75,-9)
  {3
    \nodepart{two}5
    \nodepart{three}2
    \nodepart{four}7
  };

  % Layer 10
  \node[style=array, rectangle split parts=5,color=gray] at (-1.9, -10)
  {7
    \nodepart{two}12
    \nodepart{three}14
    \nodepart{four}42
    \nodepart{five}97
  };
  \node[array, rectangle split parts=2,color=gray] at (1.25,-10)
  {3
    \nodepart{two}5
  };
  \node[array, rectangle split parts=2,color=gray] at (2.5,-10)
  {2
    \nodepart{two}7
  };

  % Layer 11
  \node[style=array, rectangle split parts=5,color=gray] at (-1.9, -11)
  {7
    \nodepart{two}12
    \nodepart{three}14
    \nodepart{four}42
    \nodepart{five}97
  };
  \node[array ,rectangle split parts=1,color=gray] at (.9,-11)
  {3 };
  \node[array ,rectangle split parts=1,color=gray] at (1.5,-11)
  {5 }; 
  \node[array, rectangle split parts=2,color=gray] at (2.5,-11)
  {2
    \nodepart{two}7
  };
  
  % Layer 12
  \node[style=array, rectangle split parts=5] at (-1.9, -12)
  {7
    \nodepart{two}12
    \nodepart{three}14
    \nodepart{four}42
    \nodepart{five}97
  };
  \node[array, rectangle split parts=2] at (1.25,-12)
  {3
    \nodepart{two}5
  };
  \node[array, rectangle split parts=2] at (2.5,-12)
  {2
    \nodepart{two}7
  };
  
  % Layer 13
  \node[style=array, rectangle split parts=5,color=gray] at (-1.9, -13)
  {7
    \nodepart{two}12
    \nodepart{three}14
    \nodepart{four}42
    \nodepart{five}97
  };
  \node[array, rectangle split parts=2,color=gray] at (1.25,-13)
  {3
    \nodepart{two}5
  };
  \node[array, rectangle split parts=1,color=gray] at (2.3,-13)
  {2 };
  \node[array,rectangle split parts=1,color=gray] at (3,-13)
  {7 };

\end{tikzpicture}
```
Zweite Hälfte:
```LaTeX
\begin{tikzpicture}[ level 1/.style={sibling distance=30mm}, level
  2/.style={sibling distance=30mm}, level 3/.style={sibling
    distance=20mm}]

  % Layer 14
  \node[style=array, rectangle split parts=5] at (-1.9, -14)
  {7
    \nodepart{two}12
    \nodepart{three}14
    \nodepart{four}42
    \nodepart{five}97
  };
  \node[array, rectangle split parts=2] at (1.25,-14)
  {3
    \nodepart{two}5
  };
  \node[array, rectangle split parts=2] at (2.5,-14)
  {2
    \nodepart{two}7
  };

  
  % Layer 14
  \node[style=array, rectangle split parts=5] at (-1.9, -15)
  {7
    \nodepart{two}12
    \nodepart{three}14
    \nodepart{four}42
    \nodepart{five}97
  };
  \node[array,rectangle split parts=4, draw] at (1.75,-15)
  {2
    \nodepart{two}3
    \nodepart{three}5
    \nodepart{four}7
  };
  
  \node[array,rectangle split parts=9] at (-0.25,-16)
    {2
      \nodepart{two}3
      \nodepart{three}5
      \nodepart{four}7
      \nodepart{five}7
      \nodepart{six}12
      \nodepart{seven}14
      \nodepart{eight}42
      \nodepart{nine}97 };

\end{tikzpicture}
```
(Diese Trennung wurde wegen der Länge des Bildes eingeführt)