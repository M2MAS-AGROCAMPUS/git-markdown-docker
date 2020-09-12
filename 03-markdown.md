---
jupyter:
  jupytext:
    cell_metadata_filter: -all
    formats: md,notebooks//ipynb
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.6.0
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

# Markdown

La langage [Markdown](https://www.markdownguide.org) est un système de formatage de texte. Il est similaire au format [html](https://html.spec.whatwg.org/multipage/) utilisé pour éditer les pages hébergées sur un serveur web et le format [reStructuredText](https://docutils.sourceforge.io/rst.html) que l'on retrouve dans les wikis. 

Le format html utilise un système de balises qui rend le texte peu lisible. Le format rst est plus lisible avec son système de balisage plus léger. Il est utilisé notamment pour la documentation du langage Python mais son utilisation est moins répandu que le markdown. 


La documentation des fonctions Julia est en markdown. Il n'y a pas de système de documentation intégré pour la langage R mais [roxygen2](https://cran.r-project.org/web/packages/roxygen2/) est le package utilisé. La syntaxe a des similarités avec [LaTeX](https://fr.wikipedia.org/wiki/LaTeX)


Les fichiers markdown sont identifiés par la terminaison `.md`.

Dans les exemples qui vont suivre, je présente les bases du langage markdown. Il faut savoir qu'il existe un grand nombre de dialectes. Github propose des fonctionalités enrichies. Pour voir toutes les possibilités, je conseille d'aller regarder la démonstration de l'éditeur en ligne [codimd](https://demo.codimd.org/features).


## Titres

Recopier le texte suivant dans une cellule en mode `markdown`. Cliquer sur la partie gauche et appuyer sur `M`. Puis exécuter avec `shift-enter`.

```md
# Chapter

## Section

### Sous-Section

Chapter
=========

Section
---------
```


## **Gras**, *italique*, `script`




## Citation

> Labore ipsum quisquam labore.


## Liste
- Fruits
    * Oranges
    * Pommes
- Légumes
    * Aubergines
    * Courgettes





## Liste ordonnée

1. Lundi
2. Mardi
3. Mercredi




<ol>
<li>Jeudi</li>
<li>Vendredi</li>
<li>Samedi</li>
<li>Dimanche</li>
</ol>


## Code R

```r
y <-  c(1,2,3,4,5)
x0 <- c(1,1,1,1,1)  
x1 <- c(1,2,3,4,5)
x2 <- c(1,4,5,7,9)
Y <- as.matrix(y)
X <- as.matrix(cbind(x0,x1,x2))
beta = solve(crossprod(X), crossprod(X,y))
```


## Code Python

```py
import numpy as np
y =  np.array((1,2,3,4,5))
x0 = np.array((1,1,1,1,1)) 
x1 = np.array((1,2,3,4,5))
x2 = np.array((1,4,5,7,9))
X = np.c_[x0,x1,x2]
Y = y[:, np.newaxis]
beta = np.linalg.solve(X.T @ X, X.T @ Y)
```


## Code Julia

```jl
using LinearAlgebra
y =  [1,2,3,4,5]
x0 = [1,1,1,1,1]
x1 = [1,2,3,4,5]
x2 = [1,4,5,7,9]
X = hcat(x0,x1,x2)
Y = y
beta = X'X \ X'y
```


## Lignes de séparation

***
Il y a plusieurs possibilités, préférez les versions avec les espaces car cela peut être confondu avec des titres lors d'une conversion en html ou pdf.
***

```
***
---
- - -
*    *    *
```


## Images

<!-- #region -->
```markdown
![texte alt](https://www.agrocampus-ouest.fr/files/images/logos/header/logo-agrocampus-ouest.png "Logo Agrocampus")

![Logo Agrocampus](https://www.agrocampus-ouest.fr/files/images/logos/header/logo-agrocampus-ouest.png)
```
<!-- #endregion -->

![Logo Agrocampus](images/logo-agrocampus-ouest.png)


## Liens

[Lien vers le site de l'agrocampus](https://www.agrocampus-ouest.fr/f)

[Lien vers le logo](images/logo-agrocampus-ouest.png "le logo!")



## Tableaux

Colonne 1 | Colonne 2 | Colonne 3
--- | --- | ---
Pomme | Banane | Orange
1 | 2 | 3

---

Colonne 1 | Colonne 2 | Colonne 3
:--- | :---: | ---:
Pomme | Banane | Orange
1 | 2 | 3


## Equations
Les mathématiques sont écrites en langage LaTeX

$$
\text{Dist}(G):=\bigcup_{n\ge 0} \text{Dist}_n(G).
$$


\begin{align}
\frac{d x_1(t) }{dt} &= \frac{1}{\varepsilon}v_1(t)  &\qquad \frac{d v_1(t) }{dt} &= E_1(t, x(t)) + \frac{1}{\varepsilon}v_2(t)\\
\frac{d x_2(t) }{dt} &= \frac{1}{\varepsilon} v_2(t) &\qquad \frac{d v_2(t) }{dt} &= E_2(t, x(t)) - \frac{1}{\varepsilon}v_1(t)\\
\frac{d x_3(t) }{dt} &= v_3(t)                       &\qquad \frac{d v_3(t) }{dt} &= E_3(t, x(t)) 
\end{align}


$$
\left(
\begin{array}{cccccc}
a & b & c  \\
d & e & f \\
g & h & i  
\end{array}
\right)
$$


$$
\begin{bmatrix}
a & b & c \\
d & e & f \\
g & h & i
\end{bmatrix}
$$


Les fonctionnalités peuvent être plus riches avec des emojis par example. Voir [Mastering Markdown](https://guides.github.com/features/mastering-markdown/)
