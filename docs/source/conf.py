import sphinx_nameko_theme

# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'u-locate'
copyright = '2023, u-blox'
author = 'Magnus Johansson'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinxcontrib.httpdomain',
    'myst_parser',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'restructuredtext',
    '.md': 'markdown',
}

# The master toctree document.
master_doc = "index"

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
# -- Pimping the theme
#html_theme_options = {
#    'style_nav_header_background':'#FF6E59;'
#}

# -- uncomment for nameko theme. Navigation works badly with current content
#html_theme = 'nameko'
#html_theme_path = [sphinx_nameko_theme.get_html_theme_path()]

# -- uncomment for groundwork theme. Navigation works badly with current content
# -- groundwork theme
#html_theme = 'groundwork'

# -- Options for EPUB output
epub_show_urls = 'footnote'
