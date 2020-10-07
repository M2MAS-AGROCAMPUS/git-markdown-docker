# Miniconda

Téléchargez <a href="https://docs.conda.io/en/latest/miniconda.html">miniconda</a> pour Python 3.

Sur Linux ou Mac, utilisez un *Terminal* :

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
jupytext --set-formats=md,notebooks//ipynb --sync *-*.md
jupyter-book build notebooks
```

Pour voir un appercu du site web généré
```bash
cd notebooks/build/html
python3 -m http.server 
```
