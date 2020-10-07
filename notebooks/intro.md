Github-Markdown-Docker
======================

Bonnes pratiques numériques pour un travail collaboratif en sciences des données.

## Miniconda

Téléchargez <a href="https://docs.conda.io/en/latest/miniconda.html">miniconda</a> pour Python 3.

Sur Windows, l'installation d'anaconda vous donnera accès à `Anaconda prompt`. Sur Linux ou Mac, utilisez un *Terminal* :

```bash
cd Downloads
bash ./Miniconda*.sh
```

Configuration du channel `conda-forge`

```bash
conda config --add channels conda-forge 
conda config --set channel_priority strict 
```

Installation de `mamba`

```bash
conda install mamba
```

Création de l'environnement `book`

```bash
mamba create python=3.7 -n book
conda activate book
```

Installation de `jupytext` avec mamba

```bash
mamba install jupytext
```

Installation de jupyter-book avec pip

```bash
pip install jupyter-book
```

Construction du Jupyter Book

```
jupytext --sync *-*
jupyter-book build notebooks
```

Pour voir le site web généré <http://localhost:8000>
```bash
notebooks/_build/html/
python3 -m http.server 
```
