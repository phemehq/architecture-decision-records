# Configuration file for the Pheme documentation.
# Mirrors the Cilium documentation build setup.
# https://www.sphinx-doc.org/en/master/usage/configuration.html

project = 'PhemeHQ ADR'
copyright = '2026, PhemeHQ Authors'
author = 'PhemeHQ Authors'
release = '1.0'
version = '1.0'

extensions = [
    'myst_parser',
    'sphinx.ext.githubpages',
    'sphinx.ext.extlinks',
    'sphinx_tabs.tabs',
    'sphinx_copybutton',
]

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- HTML output -----------------------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_css_files = ['custom.css']
html_logo = '_static/logo.png'
html_favicon = '_static/favicon.ico'
html_title = 'PhemeHQ Architecture Decision Records'
html_baseurl = 'https://phemehq.github.io/architecture-decision-records/'

html_theme_options = {
    'logo_only': True,
    'navigation_depth': 1,
    'collapse_navigation': False,
    'sticky_navigation': True,
    'includehidden': True,
    'titles_only': False,
    'style_external_links': False,
    'prev_next_buttons_location': 'bottom',
}

html_context = {
    'display_github': True,
    'github_user': 'phemehq',
    'github_repo': 'architecture-decision-records',

    'github_version': 'main',
    'conf_py_path': '/docs/',
}

# -- External links --------------------------------------------------------

extlinks = {
    'github-issue': ('https://github.com/phemehq/pheme/issues/%s', 'issue %s'),
    'github-pr': ('https://github.com/phemehq/pheme/pull/%s', 'PR %s'),
}

# -- MyST (Markdown) -------------------------------------------------------

myst_enable_extensions = [
    'colon_fence',
    'deflist',
    'tasklist',
]

# -- Syntax highlighting ---------------------------------------------------

pygments_style = 'sphinx'

# -- Copybutton ------------------------------------------------------------

copybutton_prompt_text = r'^\$ |^>>> '
copybutton_prompt_is_regexp = True
