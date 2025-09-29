import os, sys
sys.path.insert(0, os.path.abspath("..")) 

project = "CIDACS-PHDC"
extensions = [
    "myst_parser",         
]
myst_enable_extensions = ["colon_fence", "deflist", "fieldlist", "tasklist"]
templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
