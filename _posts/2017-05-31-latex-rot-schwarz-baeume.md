---
layout: post
title: 'LaTeX-Snippet: Rot-Schwarz-Bäume'
date: 2017-05-31 10:38:00
category: LaTeX
tags: [LaTeX]
---

LaTeX-Schnipsel zur Visualisierung von Rot-Schwarz-Bäumen
(z.B. Aufgabe 11 von [DSAL Abgabe 5]({{ site.baseurl
}}/dsal/2017/05/31/dsal-blatt-5.html), dort ist auch ein Java-programm
zur generierung von TikZ-Bildern zu finden).

Benötigte Pakete sowie benutzte Style Settings:
```LaTeX
\usepackage{tikz}
\usetikzlibrary{shapes,arrows,positioning,decorations,
  automata,backgrounds,petri,bending,
  shapes.multipart
} %Eventuell sind nicht alle nötig
\usepackage{pgf}

\tikzset{
  treenode/.style = {shape=circle,
    draw, align=center},
  graynode/.style = {fill=gray},
  normal/.style     = {treenode, font=\Large, bottom color=white},
  blackTreeNode/.style =
  {treenode,shape=rectangle,white,fill=black,minimum width=1.5em, ,
    minimum height=1.5em },% arbre rouge noir, noeud noir
  redTreeNode/.style = {treenode, red, draw=red,fill=red!15!white,
    thick},% arbre rouge noir, noeud rouge 
  externalBlackNode/.style = {treenode, shape=rectangle, draw=black,
    minimum width=0.25em, minimum height=0.25em,fill=black}% arbre rouge noir, nil
}
```
(Dies ist die ganze Aufgabe DSAL-U5-A11, klau dir einfach das, was du brauchst)
```LaTeX
\newsubsubproblem[1]
\begin{figure}[H]
  \centering
  \begin{tikzpicture}
    [sibling distance        = 3em,
    level distance          = 3em,
    edge from parent/.style = {draw, -latex},
    every node/.style       = {font=\footnotesize},
    level 1/.style={sibling distance=8em},
    level 2/.style={sibling distance=4em},
    level 3/.style={sibling distance=2em},
    level 4/.style={sibling distance=1em},
    sloped
    ]
    \node [blackTreeNode] {6}
    child { 
      node [externalBlackNode] {}} 
    child { 
      node [externalBlackNode] {}}
    ;
  \end{tikzpicture}
  \caption{\texttt{Einf\"uge-Operation} von 6}
\end{figure}

\newsubsubproblem[2]
\begin{figure}[H]
  \centering
  \begin{tikzpicture}
    [sibling distance        = 3em,
    level distance          = 3em,
    edge from parent/.style = {draw, -latex},
    every node/.style       = {font=\footnotesize},
    level 1/.style={sibling distance=8em},
    level 2/.style={sibling distance=4em},
    level 3/.style={sibling distance=2em},
    level 4/.style={sibling distance=1em},
    sloped
    ]
    \node [blackTreeNode] {6}
    child { 
      node [redTreeNode] {0}
      child { 
        node [externalBlackNode] {}} 
      child { 
        node [externalBlackNode] {}}
    } 
    child { 
      node [externalBlackNode] {}};
  \end{tikzpicture}
  \caption{\texttt{Einf\"uge-Operation} von 0}
\end{figure}

\newsubsubproblem[3]
\begin{figure}[H]
  \centering
  \begin{tikzpicture}
    [sibling distance        = 3em,
    level distance          = 3em,
    edge from parent/.style = {draw, -latex},
    every node/.style       = {font=\footnotesize},
    level 1/.style={sibling distance=8em},
    level 2/.style={sibling distance=4em},
    level 3/.style={sibling distance=2em},
    level 4/.style={sibling distance=1em},
    sloped
    ]
    \node [blackTreeNode] {6}
    child { 
      node [redTreeNode] {0}
      child { 
        node [externalBlackNode] (rotate2) {}} 
      child { 
        node [redTreeNode] (rotate1) {2}
        child { 
          node [externalBlackNode] {}} 
        child { 
          node [externalBlackNode] {}}
      }
    } 
    child { 
      node [externalBlackNode] {}};

    \node [left=.01 of rotate1] (rotate1L) {};
    \node [right=.01 of rotate2] (rotate2R) {};
    %\draw [->, line width=2pt,color=blue] (rotate2R) to[bend left=75] (rotate1L);
    \draw [->, line width=2pt,color=blue] (rotate1L) to[bend right=75] (rotate2R);
  \end{tikzpicture}
  \caption{\texttt{Einf\"uge-Operation} von 2}
\end{figure}

\begin{figure}[H]
  \centering
  \begin{tikzpicture}
    [sibling distance        = 3em,
    level distance          = 3em,
    edge from parent/.style = {draw, -latex},
    every node/.style       = {font=\footnotesize},
    level 1/.style={sibling distance=8em},
    level 2/.style={sibling distance=4em},
    level 3/.style={sibling distance=2em},
    level 4/.style={sibling distance=1em},
    sloped
    ]
    \node [blackTreeNode] {6}
    child { 
      node [redTreeNode] (rotate1) {2}
      child { 
        node [redTreeNode] {0}
        child { 
          node [externalBlackNode] {}} 
        child { 
          node [externalBlackNode] {}}
      } 
      child { 
        node [externalBlackNode] {}}
    } 
    child { 
      node [externalBlackNode] (rotate2) {}};

    
    \node [left=.01 of rotate1] (rotate1L) {};
    \node [right=.01 of rotate2] (rotate2R) {};
    \node [left=.01 of rotate2] (rotate2L) {};
    \node [right=.01 of rotate1] (rotate1R) {};
    \draw [->, line width=2pt,color=blue] (rotate1R) to[bend left=45] (rotate2L);
    %\draw [->, line width=2pt,color=blue] (rotate1L) to[bend right=75] (rotate2R);
  \end{tikzpicture}
  \caption{\texttt{Left-Rotate} \"uber 0}
\end{figure}

\begin{figure}[H]
  \centering
  \begin{tikzpicture}
    [sibling distance        = 3em,
    level distance          = 3em,
    edge from parent/.style = {draw, -latex},
    every node/.style       = {font=\footnotesize},
    level 1/.style={sibling distance=8em},
    level 2/.style={sibling distance=4em},
    level 3/.style={sibling distance=2em},
    level 4/.style={sibling distance=1em},
    sloped
    ]
    \node [redTreeNode] {2}
    child { 
      node [redTreeNode] {0}
      child { 
        node [externalBlackNode] {}} 
      child { 
        node [externalBlackNode] {}}
    } 
    child { 
      node [blackTreeNode] {6}
      child { 
        node [externalBlackNode] {}} 
      child { 
        node [externalBlackNode] {}}
    }
    ;
  \end{tikzpicture}
  \caption{\texttt{Right-Rotate} \"uber 6}
\end{figure}

\begin{figure}[H]
  \centering
  \begin{tikzpicture}
    [sibling distance        = 3em,
    level distance          = 3em,
    edge from parent/.style = {draw, -latex},
    every node/.style       = {font=\footnotesize},
    level 1/.style={sibling distance=8em},
    level 2/.style={sibling distance=4em},
    level 3/.style={sibling distance=2em},
    level 4/.style={sibling distance=1em},
    sloped
    ]
    \node [blackTreeNode] {2}
    child { 
      node [redTreeNode] {0}
      child { 
        node [externalBlackNode] {}} 
      child { 
        node [externalBlackNode] {}}
    } 
    child { 
      node [redTreeNode] {6}
      child { 
        node [externalBlackNode] {}} 
      child { 
        node [externalBlackNode] {}}
    }
    ;
  \end{tikzpicture}
  \caption{\texttt{Umf\"arbung}}
\end{figure}

\newsubsubproblem[4]
\begin{figure}[H]
  \centering
  \begin{tikzpicture}
    [sibling distance        = 3em,
    level distance          = 3em,
    edge from parent/.style = {draw, -latex},
    every node/.style       = {font=\footnotesize},
    level 1/.style={sibling distance=8em},
    level 2/.style={sibling distance=4em},
    level 3/.style={sibling distance=2em},
    level 4/.style={sibling distance=1em},
    sloped
    ]
    \node [blackTreeNode] {2}
    child { 
      node [redTreeNode] {0}
      child { 
        node [externalBlackNode] {}} 
      child { 
        node [externalBlackNode] {}}
    } 
    child { 
      node [redTreeNode] {6}
      child { 
        node [externalBlackNode] {}} 
      child { 
        node [redTreeNode] {19}
        child { 
          node [externalBlackNode] {}} 
        child { 
          node [externalBlackNode] {}}
      }
    }
    ;
  \end{tikzpicture}
  \caption{\texttt{Einf\"uge-Operation} von 19}
\end{figure}

\begin{figure}[H]
  \centering
  \begin{tikzpicture}
    [sibling distance        = 3em,
    level distance          = 3em,
    edge from parent/.style = {draw, -latex},
    every node/.style       = {font=\footnotesize},
    level 1/.style={sibling distance=8em},
    level 2/.style={sibling distance=4em},
    level 3/.style={sibling distance=2em},
    level 4/.style={sibling distance=1em},
    sloped
    ]
    \node [blackTreeNode] {2}
    child { 
      node [blackTreeNode] {0}
      child { 
        node [externalBlackNode] {}} 
      child { 
        node [externalBlackNode] {}}
    } 
    child { 
      node [blackTreeNode] {6}
      child { 
        node [externalBlackNode] {}} 
      child { 
        node [redTreeNode] {19}
        child { 
          node [externalBlackNode] {}} 
        child { 
          node [externalBlackNode] {}}
      }
    }
    ;
  \end{tikzpicture}
  \caption{\texttt{Umf\"arbung}}
\end{figure}

\newsubsubproblem[5]
\begin{figure}[H]
  \centering
  \begin{tikzpicture}
    [sibling distance        = 3em,
    level distance          = 3em,
    edge from parent/.style = {draw, -latex},
    every node/.style       = {font=\footnotesize},
    level 1/.style={sibling distance=8em},
    level 2/.style={sibling distance=4em},
    level 3/.style={sibling distance=2em},
    level 4/.style={sibling distance=1em},
    sloped
    ]
    \node [blackTreeNode] {2}
    child { 
      node [blackTreeNode] {0}
      child { 
        node [externalBlackNode] {}} 
      child { 
        node [externalBlackNode] {}}
    } 
    child { 
      node [blackTreeNode] {6}
      child { 
        node [externalBlackNode] {}} 
      child { 
        node [redTreeNode] {19}
        child { 
          node [redTreeNode] (rotate1) {12}
          child { 
            node [externalBlackNode] {}} 
          child { 
            node [externalBlackNode] {}}
        } 
        child { 
          node [externalBlackNode] (rotate2) {}}
      }
    };
    
    \node [left=0 of rotate1] (rotate1L) {};
    \node [right=0 of rotate2] (rotate2R) {};
    \node [left=0 of rotate2] (rotate2L) {};
    \node [right=0 of rotate1] (rotate1R) {};
    \draw [->, line width=2pt,color=blue] (rotate1) to[bend left=90] (rotate2);
    %\draw [->, line width=2pt,color=blue] (rotate1L) to[bend right=75] (rotate2R);
  \end{tikzpicture}
  \caption{\texttt{Einf\"uge-Operation} von 12}
\end{figure}

\begin{figure}[H]
  \centering
  \begin{tikzpicture}
    [sibling distance        = 3em,
    level distance          = 3em,
    edge from parent/.style = {draw, -latex},
    every node/.style       = {font=\footnotesize},
    level 1/.style={sibling distance=8em},
    level 2/.style={sibling distance=4em},
    level 3/.style={sibling distance=2em},
    level 4/.style={sibling distance=1em},
    sloped
    ]
    \node [blackTreeNode] {2}
    child { 
      node [blackTreeNode] {0}
      child { 
        node [externalBlackNode] {}} 
      child { 
        node [externalBlackNode] {}}
    } 
    child { 
      node [blackTreeNode] {6}
      child { 
        node [externalBlackNode] (rotate2) {}} 
      child { 
        node [redTreeNode] (rotate1) {12}
        child { 
          node [externalBlackNode] {}} 
        child { 
          node [redTreeNode] {19}
          child { 
            node [externalBlackNode] {}} 
          child { 
            node [externalBlackNode] {}}
        }
      }
    };

    \node [left=.01 of rotate1] (rotate1L) {};
    \node [right=.01 of rotate2] (rotate2R) {};
    \node [left=.01 of rotate2] (rotate2L) {};
    \node [right=.01 of rotate1] (rotate1R) {};
    %\draw [->, line width=2pt,color=blue] (rotate1R) to[bend left=45] (rotate2L);
    \draw [->, line width=2pt,color=blue] (rotate1L) to[bend right=75] (rotate2R);
  \end{tikzpicture}
  \caption{\texttt{Right-Rotate} \"uber 19}
\end{figure}

\begin{figure}[H]
  \centering
  \begin{tikzpicture}
    [sibling distance        = 3em,
    level distance          = 3em,
    edge from parent/.style = {draw, -latex},
    every node/.style       = {font=\footnotesize},
    level 1/.style={sibling distance=8em},
    level 2/.style={sibling distance=4em},
    level 3/.style={sibling distance=2em},
    level 4/.style={sibling distance=1em},
    sloped
    ]
    \node [blackTreeNode] {2}
    child { 
      node [blackTreeNode] {0}
      child { 
        node [externalBlackNode] {}} 
      child { 
        node [externalBlackNode] {}}
    } 
    child { 
      node [redTreeNode] {12}
      child { 
        node [blackTreeNode] {6}
        child { 
          node [externalBlackNode] {}} 
        child { 
          node [externalBlackNode] {}}
      } 
      child { 
        node [redTreeNode] {19}
        child { 
          node [externalBlackNode] {}} 
        child { 
          node [externalBlackNode] {}}
      }
    }
    ;
  \end{tikzpicture}
  \caption{\texttt{Left-Rotate} \"uber 6}
\end{figure}

\begin{figure}[H]
  \centering
  \begin{tikzpicture}
    [sibling distance        = 3em,
    level distance          = 3em,
    edge from parent/.style = {draw, -latex},
    every node/.style       = {font=\footnotesize},
    level 1/.style={sibling distance=8em},
    level 2/.style={sibling distance=4em},
    level 3/.style={sibling distance=2em},
    level 4/.style={sibling distance=1em},
    sloped
    ]
    \node [blackTreeNode] {2}
    child { 
      node [blackTreeNode] {0}
      child { 
        node [externalBlackNode] {}} 
      child { 
        node [externalBlackNode] {}}
    } 
    child { 
      node [blackTreeNode] {12}
      child { 
        node [redTreeNode] {6}
        child { 
          node [externalBlackNode] {}} 
        child { 
          node [externalBlackNode] {}}
      } 
      child { 
        node [redTreeNode] {19}
        child { 
          node [externalBlackNode] {}} 
        child { 
          node [externalBlackNode] {}}
      }
    }
    ;
  \end{tikzpicture}
  \caption{\texttt{Umf"arbung}}
\end{figure}

\newsubsubproblem[6]
\begin{figure}[H]
  \centering
  \begin{tikzpicture}
    [sibling distance        = 3em,
    level distance          = 3em,
    edge from parent/.style = {draw, -latex},
    every node/.style       = {font=\footnotesize},
    level 1/.style={sibling distance=8em},
    level 2/.style={sibling distance=4em},
    level 3/.style={sibling distance=2em},
    level 4/.style={sibling distance=1em},
    sloped
    ]
    \node [blackTreeNode] {2}
    child { 
      node [blackTreeNode] {0}
      child { 
        node [externalBlackNode] {}} 
      child { 
        node [externalBlackNode] {}}
    } 
    child { 
      node [blackTreeNode] {12}
      child { 
        node [redTreeNode] {6}
        child { 
          node [externalBlackNode] {}} 
        child { 
          node [externalBlackNode] {}}
      } 
      child { 
        node [redTreeNode] {19}
        child { 
          node [redTreeNode] {12}
          child { 
            node [externalBlackNode] {}} 
          child { 
            node [externalBlackNode] {}}
        } 
        child { 
          node [externalBlackNode] {}}
      }
    }
    ;
  \end{tikzpicture}
  \caption{\texttt{Einf\"uge-Operation} von 12}
\end{figure}

\begin{figure}[H]
  \centering
  \begin{tikzpicture}
    [sibling distance        = 3em,
    level distance          = 3em,
    edge from parent/.style = {draw, -latex},
    every node/.style       = {font=\footnotesize},
    level 1/.style={sibling distance=8em},
    level 2/.style={sibling distance=4em},
    level 3/.style={sibling distance=2em},
    level 4/.style={sibling distance=1em},
    sloped
    ]
    \node [blackTreeNode] {2}
    child { 
      node [blackTreeNode] {0}
      child { 
        node [externalBlackNode] {}} 
      child { 
        node [externalBlackNode] {}}
    } 
    child { 
      node [redTreeNode] {12}
      child { 
        node [blackTreeNode] {6}
        child { 
          node [externalBlackNode] {}} 
        child { 
          node [externalBlackNode] {}}
      } 
      child { 
        node [blackTreeNode] {19}
        child { 
          node [redTreeNode] {12}
          child { 
            node [externalBlackNode] {}} 
          child { 
            node [externalBlackNode] {}}
        } 
        child { 
          node [externalBlackNode] {}}
      }
    }
    ;
  \end{tikzpicture}
  \caption{\texttt{Umf\"arbung}}
\end{figure}
```