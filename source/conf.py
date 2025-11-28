"""Sphinx configuration for the Sports Application help files.

This file controls how Sphinx builds the documentation for the
Activity 5 sports application.
"""

import os
import sys

# Make the project root (activity_5) available so Sphinx can find our packages
# such as league, team, player and sports_app.
sys.path.insert(0, os.path.abspath('..'))

# -- Project information -----------------------------------------------------

project = "Sports Application"
author = "Your Name"          # Replace with your own name
release = "1.0.0"             # Matches the __version__ in the code base

# -- General configuration ---------------------------------------------------

# Sphinx extensions used for this project. autodoc reads our docstrings
# and turns them into documentation.
extensions = [
    'sphinx.ext.autodoc',
]

# Paths that contain templates, relative to this directory.
templates_path = ['_templates']

# Patterns to ignore when looking for source files.
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

# Theme used for the HTML help pages. This is a simple default theme.
html_theme = 'alabaster'

# Paths that contain custom static files (such as style sheets).
html_static_path = ['_static']
