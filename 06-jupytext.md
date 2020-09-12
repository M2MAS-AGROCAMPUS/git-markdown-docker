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
# Jupytext et pandoc

Jupytext est un outil de conversion de format des notebooks. Il permet de synchroniser des 
notebooks au format ipynb avec des scripts commentés (Julia, Python ou R), ou en fichier markdown.

Pandoc est un outil de conversion des fichiers markdown vers des formats d'édition ou d'impression comme html, pdf, latex ou word.
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## Installlation

```
conda install -c conda-forge jupytext
```
ou
```
pip install jupytext
```
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## Jupytext

La commande`jupytext` permet de convertir un notebook dans differents formats:

```bash
jupytext --to py notebook.ipynb                 # convert notebook.ipynb to a .py file
jupytext --to markdown notebook.ipynb           # convert notebook.ipynb to a .md file
```
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
```bash
jupytext --to notebook notebook.py              # convert notebook.py to an .ipynb file with no outputs
jupytext --update --to notebook notebook.py     # update the input cells in the .ipynb file and preserve outputs and metadata

jupytext --to md --test notebook.ipynb          # Test round trip conversion
```
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
### Convertir le notebook Python en markdown

```bash
jupytext --to markdown 08-example-python.ipynb
```

<!-- #endregion -->

<!-- #region slideshow={"slide_type": "fragment"} -->
### Convertir le notebook Python en script python

```bash
jupytext --to script 08-example-python.ipynb
```

<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
### Convertir le notebook R en script R

```bash
jupytext --to R 10-example-r.ipynb
```


<!-- #endregion -->

<!-- #region slideshow={"slide_type": "fragment"} -->
### Convertir le notebook R en fichier Rmd

```bash
jupytext --to Rmd 10-example-r.ipynb
```


```bash
jupytext --to ipynb 10-example-r.Rmd
```



<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
### Convertir le notebook Julia en script julia

```bash
jupytext --to jl 07-example-julia.ipynb
```



<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
### Synchronisation

```bash
jupytext --set-formats ipynb,py notebook.ipynb  # Turn notebook.ipynb into a paired ipynb/py notebook
jupytext --sync notebook.ipynb 
```

Jupytext verifie les dates des fichiers
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
## Pandoc
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "fragment"} -->
```bash
pandoc -s 07-exemple-julia.ipynb -o example-julia.html
```
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "fragment"} -->
```bash
pandoc -s 07-exemple-julia.ipynb --pdf-engine=xelatex -o example-julia.pdf
```
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "fragment"} -->
```bash
pandoc -t beamer 01-jupyter.ipynb -o example8.pdf
```
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "fragment"} -->
```bash
pandoc -s 09-exemple-r.ipynb -o example-r.docx
```
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "slide"} -->
**[Très très nombreuses possibilités](https://pandoc.org/demos.html)**
<!-- #endregion -->
