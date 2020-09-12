---
jupyter:
  jupytext:
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

<!-- #region slideshow={"slide_type": "slide"} -->
# Binder 

- Service d'hébergement temporaire pour partager une application en ligne gratuitement
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## Preparer son dépôt github pour Binder

Les fichiers de configuration

- Dockerfile
- environment.yml  (Python/R)
- requirements.txt (Python)
- apt.txt  (paquets ubuntu)      
- postBuild # script à exécuter après construction de l'image
- Project.toml # Julia
- runtime.txt # R
- install.R # R

<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
### environment.yml

Fichier pour conda environment (https://conda.io/docs/).

Exemple
~~~yaml
channels:
  - conda-forge
  - defaults
dependencies:
  - matplotlib
  - pip
  - pip:
    - nbcourse
~~~
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
### requirements.txt

Fichier pour installer une liste de paquets Python avec pip

Exemple

~~~
numpy==1.11
matplotlib==2.1
scipy
~~~
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
### apt.txt

Liste de paquets à installer. L'image de base est la dernière version ubuntu

Exemple

~~~
ffmpeg
graphviz
~~~
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
### postBuild

Script à exécuter après la construction de l'image.

Exemple:

~~~
#!/bin/bash
wget <url-to-dataset>
python myfile.py
~~~

Note:
Le fichier doit être éxécutable
```
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## Démarrer Binder

- Aller sur <https://mybinder.org> et copier-coller l'adresse de votre dépôt git. 
- Cliquer sur `Launch`. 
- Une nouvelle image sera construite uniquement si votre dépôt a été modifié.

<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## JupyterLab + Binder

1. Launch a Binder instance

Par défaut vous aurez un accès à un serveur jupyter classique.
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "fragment"} -->
2. Remplacer `tree` par `lab`
```
https://hub.mybinder.org/user/pnavaro/agrocampus/tree
```

<!-- #endregion -->

<!-- #region slideshow={"slide_type": "fragment"} -->
3. That’s it!
```
https://hub.mybinder.org/user/groupecalcul-canum-2018-la7iw4x1/lab
```
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## Exemple avec R

runtime.txt:
```
r-<YYYY>-<MM>-<DD`
```

https://github.com/binder-examples/r
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "fragment"} -->
Fichier `install.R` pour les dépendances:
    
```R
install.packages("tidyverse")
install.packages("rmarkdown")
install.packages("httr")
install.packages("shinydashboard")
install.packages('leaflet')
```
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
 ## Remarques
 
 - Tout ce qui se passe dans une application binder est détruit au bout de quelques minutes d'inactivité
 - Ne laissez aucune information sensible dans une image binder (identifiants, mot de passe, liste d'emails, ...)
 - Le maximum de connexions simultannées est 100
 - Vous avez 1Go de RAM garanti et cela peut aller jusqu'à 4Go
 - Si vous restez actif, vous pouvez utiliser une session biender pendant 12 heures
 - Ne faites aucun push vers github depuis une session binder
 - Vous pouvez également déposer vos fichiers de configuration dans un répertoire nommé `binder`.
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## Examples

Beaucoup d'exemples sont disponibles pour Python, R, Latex, conda, docker...

<http://mybinder.readthedocs.io/en/latest/sample_repos.html>

<https://github.com/binder-examples>
<!-- #endregion -->
