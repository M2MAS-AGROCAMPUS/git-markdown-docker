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
# Github Action


Système d'exécution de code automatisé couplé avec un dépôt github, permet de :

- Compiler une application
- Exécuter des tests et vérifier le fonctionnement d'une application
- Contruire une documentation en html ou pdf

<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## Exemple 

Outils informatiques pour le big-data <http://pnavaro.github.io/big-data>

```yaml
name: Build and Deploy
on:
  push:
    branches:
      - master
```
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
```yaml
jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    steps:
    - name: Install pandoc
      run: |
        sudo apt-get -yq update
        sudo apt-get install -yq pandoc texlive-xetex texlive-fonts-extra graphviz
    - name: Checkout
      uses: actions/checkout@v2
      with:
        persist-credentials: false
```
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
```yaml
    - name: Install SSH Client
      uses: webfactory/ssh-agent@v0.2.0
      with:
        ssh-private-key: ${{ secrets.NBCOURSE_PRIV }}
    - name: Set up JDK 1.8
      uses: actions/setup-java@v1
      with:
        java-version: 1.8
```       
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
```yaml
    - name: Download Apache Spark
      uses: wei/wget@v1
      with:
        args: https://downloads.apache.org/spark/spark-3.0.0/spark-3.0.0-bin-hadoop2.7.tgz
    - name: Install Apache Spark
      run: tar zxf spark-3.0.0-bin-hadoop2.7.tgz
    - uses: Actions-R-Us/default-env@v1
      env:
        SPARK_HOME: '/home/runner/spark-3.0.0-bin-hadoop2.7'
```
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
```yaml
    - name: Install Miniconda and dependencies
      uses: goanpeca/setup-miniconda@v1
      with:
        miniconda-version: "latest"
        activate-environment: big-data
        environment-file: environment.yml
    - name: Install nbcourse
      shell: bash -l {0}
      run: |
        conda run -n big-data python -m ipykernel install --user --name big-data
        conda run -n base python -m pip install nbcourse
    - name: Run nbcourse
      shell: bash -l {0}
      run: conda run -n base nbcourse -n 1
    - name: Deploy on github
      uses: JamesIves/github-pages-deploy-action@releases/v3
      with:
        SSH: true
        BRANCH: gh-pages
        FOLDER: build
```
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## Création d'une paire de clés public/privée

```bash
ssh-keygen -N "" -f ma_cle
```

2 fichiers sont créés, la clé privée: ma_cle, et la clé publique ma_cle.pub.

Aller sur GitHub et votre dépôt, dans l'onglet `Settings > Secret` puis `Add new secret`,
Nommé le secret `NBCOURSE_PRIV` et copier le contenu de la clé privée.

Dans l'onglet `Settings > Deploy keys` cliquer sur `Add deploy key`,
Nommé la clé `NBCOURSE_PUB` et copier le contenu de la clé publique (ma_cle.pub).

**IMPORTANT** : Cocher la case à coté de `Enable write access`.


<!-- #endregion -->
