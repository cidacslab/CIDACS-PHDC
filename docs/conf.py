import os, sys
sys.path.insert(0, os.path.abspath(".."))

project = "CIDACS-PHDC"

extensions = [
    "myst_parser",
    "nbsphinx",          
]


nbsphinx_execute = "never"


nbsphinx_allow_errors = True

html_theme = "sphinx_rtd_theme"

