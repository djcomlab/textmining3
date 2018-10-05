# Python textmining3 package

## Overview
This package contains a variety of useful functions for text mining in Python.
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

The original code and documentation was authored by Christian Peccei
(cpeccei@hotmail.com) in 2010 and is available in PyPI under the package name
`textmining`. You can read more about it on his website 
https://www.christianpeccei.com/textmining/ and find the original code and PyPI
package here https://pypi.org/project/textmining/.

This package is a port to Python 3 and published under the package
name `textmining3`.

Installation
------------
Clone this repository and run

```
python setup.py install
```

or install from PyPI with (TODO: publish to PyPI)

```
pip install textmining3
```

or install from Anaconda Cloud with (TODO: publish to Conda)

```
conda install textmining3
```

Documentation
-------------

Please see the docstrings in the functions themselves and the `examples`
subdirectory for actual applications of the various functions.
