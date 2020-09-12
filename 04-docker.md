---
jupyter:
  jupytext:
    encoding: '# -*- coding: utf-8 -*-'
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
# Docker

<img width=200 src="images/Moby-logo.png">
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## Conteneur

Technologie logicielle datant de 2013 permettant d'éxécuter un système d'exploitation isolé et automatisé dans un autre système. La technique est proche de la virtualisation mais sans l'inconvénient de la latence.

Un conteneur permet également de sauvegarder l'état d'un ordinateur à un instant donné et de pouvoir rédemmarrer de cet état à tout moment.

**Attention l'utilisation de docker nécessite une bonne connexion internet et beaucoup d'espace disque.**
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->

## Points forts

- Installation très simple <https://www.docker.com/get-started>
- Ligne de commande facile à utiliser (`docker help`)
- Beaucoup de possibilités ( hébergement web, cloud, intégration continue, ...)

<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## Docker en 1 ligne

Pour vérifier que docker est bien installé

```bash
docker run helloworld
```

```bash
docker run --rm -it -v $PWD:/work ubuntu /bin/bash
```
- `run` : on veut lancer le conteneur
- `-it` : on veut un terminal et être interactif avec lui 
- `ubuntu` : l’image à utiliser pour ce conteneur 
- `/bin/bash` : commande éxécutée au démarrage qui permet l'interactivité
- `-v $PWD:/work` : le répertoire courant sera monté dans l'image docker sous la racine `/work`

<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## Les étapes du démarrage d'un image docker

- Recherche de l’image -> Si l’image n’existe pas en local, alors téléchargement via le hub. Construction du système de fichiers.
- Démarrage du container
- Configuration de l’adresse IP du container -> Ainsi que de la communication entre l’extérieur et le conteneur
- Capture des messages entrées-sorties
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## Principales commandes sur linux

```
sudo /usr/bin/docker -d & # run the daemon
sudo docker search ubuntu # give ubuntu images from public index 
sudo docker pull ubuntu # pull latest ubuntu images
sudo docker history ubuntu # view history for this images
sudo docker images # show local images
docker ps # show active containers
sudo docker logs ubuntu
sudo docker attach ubuntu # retake the hand on the container
sudo docker run -d -p 8888:80 ubuntu # export 8888 on master
sudo docker stop # SIGTERM suivi d’un SIGKILL
sudo docker kill # SIGKILL directement
```
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## Création d'images Docker

Il est possible de créer une image docker en utilisant des commandes en ligne mais préférez la méthode du fichier Dockerfile qui vous permettra de conserver les etapes et une trace de la procédure.
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
### Dockerfile rocker/shiny
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "fragment"} -->
```dockerfile
FROM rocker/r-ver:3.6.3
```
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
```dockerfile
RUN apt-get update && apt-get install -y \
    sudo \
    gdebi-core \
    pandoc \
    pandoc-citeproc \
    libcurl4-gnutls-dev \
    libcairo2-dev \
    libxt-dev \
    xtail \
    wget
```
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
```dockerfile
# Download and install shiny server
RUN wget --no-verbose https://download3.rstudio.org/ubuntu-14.04/x86_64/VERSION -O "version.txt" && \
    VERSION=$(cat version.txt)  && \
    wget --no-verbose "https://download3.rstudio.org/ubuntu-14.04/x86_64/shiny-server-$VERSION-amd64.deb" -O ss-latest.deb && \
    gdebi -n ss-latest.deb && \
    rm -f version.txt ss-latest.deb && \
    . /etc/environment && \
    R -e "install.packages(c('shiny', 'rmarkdown'), repos='$MRAN')" && \
    cp -R /usr/local/lib/R/site-library/shiny/examples/* /srv/shiny-server/ && \
    chown shiny:shiny /var/lib/shiny-server
```
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
```dockerfile
EXPOSE 3838
```
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "fragment"} -->
```dockerfile
COPY shiny-server.sh /usr/bin/shiny-server.sh
```
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "fragment"} -->
```dockerfile
CMD ["/usr/bin/shiny-server.sh"]
```
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## Instructions

Les instructions sont peu nombreuses : FROM, RUN, CMD, LABEL, MAINTAINER, EXPOSE, ENV, ADD, COPY, ENTRYPOINT , VOLUME, USER, WORKDIR, ARG, ONBUILD, STOPSIGNAL, HEALTHCHECK, SHELL

- Pour chaque instruction RUN, un conteneur temporaire (8xxxxxxxx) est créé depuis l’image de base.
- La commande RUN est exécutée dans ce conteneur,
- Le conteneur est commité en une image intermédiaire (7yyyyyyyy),
- Le conteneur intermédiaire (8xxxxxxxx) est supprim ́e, Le résultat, l’image intermédiaire, servira d’image de base pour l’ ́etape suivante,
etc..
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## Docker Hub

Site public permettant de sauvegarder et partager ses images docker (registry), il faut:

- Déposer son fichier Dockerfile sur un dépôt github
- Créer une image docker sur <https://hub.docker.com> et lier cette image au dépôt github
- Chaque modification sur le dépôt va mettre à jour l'image
    
    
<!-- #endregion -->
