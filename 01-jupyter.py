# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: -all
#     formats: py:light,notebooks//ipynb
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.6.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# # Jupyter
#
# ## Installation
#
# Pour construire note site, nous avez besoin d'une distribution Python. [Miniconda](https://conda.io/miniconda.html) est une solution légère permettant d'installer tous les packages nécessaires.
#
# Une fois installer miniconda en ayant suivi les instructions, ouvrez un terminal sur Linux/Macos ou un anaconda prompt sur Windows.
#

# ### Environnement conda
#
# ```bash
# git clone https://github.com/M2MAS-AGROCAMPUS/git-markdown-docker
# # cd git-markdown-docker
# conda env create -n agrocampus
# ```
#
# [documentation](https://conda.io/docs/using/envs.html).
#
# L'environnement est créé a partir d'un fichier nommé `environment.yml` qui contient la liste des packages dont nous avons besoin.

# ### Activer l'environnement conda
#
# Lorsque vous activer l'environement conda, votre configuration du terminal est modifiée et la version
# de python qui sera disponible sera celle ou tous nos packages seront installés.
# <pre>
# $ conda activate agrocampus
# (agrocampus) $ python
# Python 3.6.2 (default, Jul 17 2017, 16:44:45) 
# [GCC 4.2.1 Compatible Apple LLVM 8.1.0 (clang-802.0.42)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> quit()
# </pre>
#

# ## Jupyter Notebook
#
# - Le calepin Jupyter est un outil de rédaction qui permet de partager une analyse mathématique. 
# - Rassembler du code informatique, du texte, des images et des formules mathématiques dans un seul document. 
# - Le code informatique est modifiable et exécutable. 
# - Excellent support pour travailler et surtout pour partager.
# - Jupyter comporte de nombreuses extensions et supporte [un nombre important de langages](https://github.com/jupyter/jupyter/wiki/Jupyter-kernels). 
# - Logiciel libre, ouvert et totalement gratuit qui fonctionne sur tous les systèmes d'exploitation existants.
#
# Jupyter est un acronyme des 3 langages supportés à l'origine du projet: **JU**lia, **PYT**hon, et **R**

# ```bash
# conda install -c conda-forge jupyter
# ```

# ## Raccoucis clavier
#
# - Pour afficher les commandes disponibles: `Cmd + Shift + P`
# - Exécuter une cellule
#     - 'Cmd-Enter' exécute la cellule courante 
#     - 'Shift-Enter' exécute la cellule courante et passe à la suivante
#     - 'Alt-Enter' exécute la cellule et crée une nouvelle en dessous.
#     
#
# - `Esc` permet de basculer en mode "commande" et vous pouvez naviguer dans le document avec les flèches de votre clavier. En mode "commande":
#    - `A` permet d'insérer une nouvelle cellule **au dessus** de la cellule active
#    - `B` permet d'insérer une nouvelle cellule **en dessous** de la cellule active
#    - `M` bacule en mode texte (markdown), `Y` pour revenir au code
#    - `D + D` en pressant deux fois ce caractère vous effacez la cellule courante
# - "Shift-Ctrl-M" permet de couper une cellule en deux au niveau du curseur.

# ## Installation de packages Python dans Jupyter 
#
# ### Avec conda
#
# Pour installer `numpy` du canal *conda-forge*
# ```ipython
# # %conda install -c conda-forge numpy
# ```
#
# ### Avec pip
#
# ```ipython
# # %pip install numpy
# ```

# ## Documentation
#
# - Shift + Tab donne accès à la documentation des fonctions

dict

# Si vous passez la cellule suivante en *Code* et l'exécutez, la documentation apparaît dans le *pager*

# ?dict

# ## Graphique (en python)
#
# la première ligne de la cellule suivante permet de tracer vos graphiques juste après l"éxécution de la céllule.

# %matplotlib inline
# %config InlineBackend.figure_format = 'retina'
import matplotlib.pyplot as plt
import numpy as np

# +
plt.rcParams['figure.figsize'] = (10,6)
fig, ax = plt.subplots()
np.random.seed(0)
x, y = np.random.normal(size=(2, 200))
color, size = np.random.random((2, 200))

ax.scatter(x, y, c=color, s=500 * size, alpha=0.3)
ax.grid(color='lightgray', alpha=0.7)
# -

# ## Les commandes magiques

# %lsmagic

# %ls

# +
# %%file sample.txt

write the cell content to the file sample.txt.
The file is created when you run this cell.
# -

# %cat sample.txt

# +
# %%file fibonacci.py

f1, f2 = 1, 1
for n in range(10):
    print(f1, end=',')
    f1, f2 = f2, f1+f2
# -

# %run fibonacci.py

# +
# # %load fibonacci.py

f1, f2 = 1, 1
for n in range(10):
    print(f1, end=',')
    f1, f2 = f2, f1+f2

# -

# %%time
f1, f2 = 1, 1
for n in range(10):
    print(f1, end=',')
    f1, f2 = f2, f1+f2
print()

# %who int

import numpy as np
# %timeit np.random.normal(size=100)

from time import sleep
def fibonacci(n):
    f1, f2 = 1, 1
    res = []
    for i in range(n):
        sleep(0.1)
        f1, f2 = f2, f1+f2
        res.append(f1)
    return res


import IPython.core
IPython.core.page = print


# %prun -q -T prof.txt fibonacci(10)

# %cat prof.txt

# %load_ext heat

# +
# %%heat

def fibonacci(n):
    f1, f2 = 1, 1
    res = []
    for i in range(n):
        f1, f2 = f2, f1+f2
        res.append(f1)
    return res

fibonacci(100)

# +
from tqdm.notebook import tqdm
from time import sleep

n = 10
res = [1]

for x in tqdm(range(2, n)):
    sleep(0.5)
    for i in range(2, x):
        if (x % i) == 0:
            break
        else:
            res.append(x)
            break

res
# -

# ## Interactivité

# +
from ipywidgets import interact


@interact(x=True, y=1.0)
def g(x, y):
    return (x, y)


# -

@interact(tau=(0.01, 0.2, 0.01))
def f(tau):
    plt.figure(2)
    t = np.linspace(0, 1, num=1000)
    plt.plot(t, 1 - np.exp(-t/tau), t,  np.exp(-t/tau))
    plt.xlim(0, 1)
    plt.ylim(0, 1)
# ## Remarque importante
#
# - Un calepin Jupyter n'est pas vraiment un programme Python
# - Il s'agit d'une suite d'instructions exécutées dans un ordre particulier avec éventuellement des répétitions.
# - Avant de partager un notebook, il est préférable d'aller dans l'onglet `Kernel` et cliquer sur `Restart & Run All` et vérifier que tout ce passe bien.
#
# ![](images/joelgrus_tweet.png)
#
# [@joelgrus](https://twitter.com/joelgrus/status/1290072502060740610?s=20)
