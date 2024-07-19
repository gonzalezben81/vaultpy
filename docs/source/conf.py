# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'vaultpy'
copyright = '2024, Gonzalez'
author = 'Gonzalez'

release = '0.1'
version = '0.1.0'

# -- Path setup ----------------------------------------------------------
import os
import sys
sys.path.insert(0, os.path.abspath('../../'))


# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',  # For Google and NumPy style docstrings
    'sphinx_autodoc_typehints',  # For type hint support
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

# -- Napoleon settings (if using Google or NumPy style docstrings) --------
napoleon_google_docstring = True
napoleon_numpy_docstring = True
