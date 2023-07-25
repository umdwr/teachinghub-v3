# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'myDWR Teaching Hub'
copyright = '2023, DWR'
author = 'DWR'
release = '3'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.viewcode'
]

templates_path = ['_templates']
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_theme_path = ["_themes", ]

html_theme_options = {
    'logo_only': True,
    'navigation_depth': 5,
    'analytics_id': 'G-2L56XZ4KKX',  
    'sticky_navigation': True,
    'prev_next_buttons_location': 'none',
}

html_logo = "assets/logo.png"

html_favicon = "assets/favicon.ico"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = [
    'custom.css',
]

html_context = {
  'display_github': True,
  'github_user': 'umdwr',
  'github_repo': 'teachinghub-v3',
  'github_version': 'main/docs/',
}


