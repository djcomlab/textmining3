===========
textmining3
===========


.. image:: https://img.shields.io/pypi/v/textmining.svg
        :target: https://pypi.python.org/pypi/textmining3

.. image:: https://img.shields.io/travis/djcomlab/textmining3.svg
        :target: https://travis-ci.org/djcomlab/textmining3

.. image:: https://readthedocs.org/projects/textmining3/badge/?version=latest
        :target: https://textmining3.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




Text Mining Utilities for Python 3


* Free software: GNU General Public License v3
* Documentation: https://textmining3.readthedocs.io.
* Requires Python >= 3.6


Features
--------

This package contains a variety of useful functions for text mining in Python 3.

It focuses on statistical text mining (i.e. the bag-of-words model) and makes it
very easy to create a term-document matrix from a collection of documents. This
matrix can then be read into a statistical package (R, MATLAB, etc.) for further
analysis. The package also provides some useful utilities for finding
collocations (i.e. significant two-word phrases), computing the edit distance
between words, and chunking long documents up into smaller pieces.

The package has a large amount of curated data (stopwords, common names, an
English dictionary with parts of speech and word frequencies) which allows the
user to extract fairly sophisticated features from a document.

This package does NOT have any natural language processing capabilities such as
part-of-speech tagging. Please see the Python NLTK for that sort of
functionality (plus much, much more).

The original code and documentation is available in PyPI under the package name
`textmining`. This package is a port to Python 3 and published in PyPI under the package
name textmining3, and is based on the original.


Credits
-------
The original `textmining` 1.0 package code was authored by Christian Peccei <cpeccei@hotmail.com>

.. _`textmining`: https://pypi.org/project/textmining/1.0/

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
