default:
	jupytext --sync 01-jupyter.py
	jupytext --sync 02-gitbasics.md
	jupytext --sync 03-markdown.md
	jupytext --sync 04-docker.md
	jupytext --sync 05-binder.md
	jupytext --sync 06-jupytext.md
	jupytext --sync 07-exemple-julia.jl
	jupytext --sync 08-exemple-python.py
	jupytext --sync 09-exemple-r.R
	jupytext --sync 10-github-action.md
