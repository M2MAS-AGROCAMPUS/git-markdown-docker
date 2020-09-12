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
## Creation du JupyterBook

Pour générer le site web <https://m2mas-agrocampus.github.io/git-markdown-docker>

J'utilise les GitHub actions et voici le script placé dans le répertoire
`.github/workflows/`
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
Cette action se déclenche pour chaque `push` sur la branche `master`

```yaml
name: Build and Deploy
on:
  push:
    branches:
      - master
```
<!-- #endregion -->

- Le `runner` choisi est une VM ubuntu, attention beaucoup de logiciels sont déjà installés. Voir https://github.com/actions/virtual-environments/blob/main/images/linux/Ubuntu1804-README.md
- Nous avons besoin de `pandoc` pour transformer le `markdown` en `html`
- `Checkout` permet de copier le dépôt sur le `runner`
- Nous avons besoin de Julia et d'installer quelques packages
- Miniconda est déjà installé, utilisons le fichier `environment.yml` pour installer les dépendances.
- L'ensemble des fichiers `html` créés par `jupyter-book` est "poussé" sur la branche `gh-pages`

<!-- #region slideshow={"slide_type": "slide"} -->
```yaml
jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    steps:
    - name: Install pandoc
      run: |
        sudo apt-get -yq update
        sudo apt-get install -yq pandoc texlive-xetex texlive-fonts-extra inkscape
    - name: Checkout
      uses: actions/checkout@v2
      with:
        persist-credentials: false
    - name: Install Julia
      run: julia -e 'using Pkg; Pkg.add(["IJulia","Plots","StatsPlots","DataFrames"]); Pkg.build("IJulia")'
    - name: Install Miniconda
      uses: goanpeca/setup-miniconda@v1
      with:
        miniconda-version: "latest"
    - name: Install dependencies
      shell: bash -l {0}
      run: |
        conda env update -f environment.yml -n runenv
        conda run -n runenv python -m ipykernel install --user --name python3
        conda run -n runenv make
        conda run -n runenv Rscript -e 'IRkernel::installspec() '
    - name: Run jupyterbook
      shell: bash -l {0}
      run: conda run -n runenv jupyter-book build notebooks
    - name: Deploy
      uses: peaceiris/actions-gh-pages@v3.6.1
      with:
        github_token: ${{ secrets.GITHUB_TOKEN }}
        publish_dir: notebooks/_build/html
```
<!-- #endregion -->

```python

```
