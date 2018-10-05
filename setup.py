from distutils.core import setup

setup(name='textmining3',
      version='0.1',
      description='Text Mining Utilities for Python 3',
      author='David Johnson',
      author_email='djcomlab@gmail.com',
      url='',
      packages=['textmining'],
      package_data={'textmining': ['data/*', 'doc/*', 'examples/*']},
      classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Text Processing :: General',
        'Topic :: Text Processing :: Linguistic'
        ],
      long_description="""
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

The original code and documentation was authored by Christian Peccei
(cpeccei@hotmail.com) and is available in PyPI under the package name
textmining. This package is a port to Python 3 and published under the package
name textmining3, and is based on the original.
"""
     )
