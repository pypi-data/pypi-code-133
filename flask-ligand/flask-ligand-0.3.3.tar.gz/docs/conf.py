# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

import flask_ligand

project = "flask-ligand"
copyright = "2022, Ryan Gard and contributors"
author = "Ryan Gard"

version = release = flask_ligand.__version__

# -- General configuration ---------------------------------------------------

extensions = [
    "hoverxref.extension",
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
    "sphinx_issues",
]

myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]

extlinks = {"sqlalchemy": ("https://docs.sqlalchemy.org/en/14/%s", None)}

intersphinx_mapping = {
    "apispec": ("https://apispec.readthedocs.io/en/latest/", None),
    "flask": ("https://flask.palletsprojects.com/en/latest/", None),
    "flask-cors": ("https://flask-cors.readthedocs.io/en/latest/", None),
    "flask-jwt-extended": ("https://flask-jwt-extended.readthedocs.io/en/stable/", None),
    "flask-migrate": ("https://flask-migrate.readthedocs.io/en/latest/", None),
    "flask-smorest": ("https://flask-smorest.readthedocs.io/en/latest/", None),
    "flask-sqlalchemy": ("https://flask-sqlalchemy.palletsprojects.com/en/2.x/", None),
    "marshmallow": ("https://marshmallow.readthedocs.io/en/stable/", None),
    "marshmallow-sqlalchemy": ("https://marshmallow-sqlalchemy.readthedocs.io/en/latest/", None),
    "quart": ("https://quart.palletsprojects.com/en/latest/", None),
    "sqlalchemy-utils": ("https://sqlalchemy-utils.readthedocs.io/en/latest/", None),
    "webargs": ("https://webargs.readthedocs.io/en/latest/", None),
}
intersphinx_disabled_domains = ["std"]

issues_github_path = "cowofevil/flask-ligand"

templates_path = ["_templates"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = [".rst", ".md"]

# The master toctree document.
master_doc = "index"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
# language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "alabaster"
html_static_path = ["_static"]
html_theme_options = {
    "description_font_style": "italic",
    "fixed_sidebar": True,
    "sidebar_collapse": True,
    "logo": "small_logo.jpg",
    "github_user": "cowofevil",
    "github_repo": "flask-ligand",
    "github_banner": True,
    "github_button": False,
    "code_font_size": "0.8em",
    "extra_nav_links": {
        "flask-ligand@PyPI": "https://pypi.python.org/pypi/flask-ligand",
        "flask-ligand@GitHub": "https://github.com/cowofevil/flask-ligand",
    },
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ["_static"]

html_sidebars = {
    "**": ["about.html", "navigation.html", "searchbox.html"],
}

# -- Configuration for hoverxref extension -------------------------------------------------

hoverxref_auto_ref = False
hoverxref_domains = ["py"]
hoverxref_roles = [
    "option",
    "doc",  # Documentation pages
    "term",  # Glossary terms
]
hoverxref_role_types = {
    "mod": "modal",  # for Python Sphinx Domain
    "doc": "modal",  # for whole docs
    "class": "tooltip",  # for Python Sphinx Domain
    "ref": "tooltip",  # for hoverxref_auto_ref config
    "confval": "tooltip",  # for custom object
    "term": "tooltip",  # for glossaries
}

hoverxref_intersphinx = [
    "apispec",
    "flask",
    "flask-cors",
    "flask-jwt-extended",
    "flask-migrate",
    "flask-smorest",
    "flask-sqlalchemy",
    "marshmallow",
    "marshmallow-sqlalchemy",
    "quart",
    "sqlalchemy-utils",
    "webargs",
]
