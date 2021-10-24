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
from os import path
import sys
__dir__ = path.abspath(path.dirname(__file__))
sys.path.insert(0, __dir__)

# config source dir and import its configuration
SOURCE_DIR = path.abspath(path.join(*'../extern/array-api/spec'.split('/')))
sys.path.insert(0, path.abspath(path.join(SOURCE_DIR, '..')))
from spec.conf import *
sys.path.pop(0)

# fix relative paths
for conf_name, conf_value in [*locals().items()]:
    if conf_name.endswith('_path'):
        for conf_idx, conf_path in enumerate(conf_value):
            conf_value[conf_idx] = path.abspath(path.join(SOURCE_DIR, conf_path))

# -- General configuration ---------------------------------------------------

suppress_warnings = [
    'image.not_readable', # fails to load imagery
    'ref.ref' # fails to link to documentation outside the specification
]

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions.append('gen')


