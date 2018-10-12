#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `textmining` package."""


import unittest
from click.testing import CliRunner

import textmining
from textmining import cli


class TestTextmining(unittest.TestCase):
    """Tests for `textmining` package."""

    def setUp(self):
        """Set up test fixtures."""
        self.doc1 = 'John and Bob are brothers.'
        self.doc2 = 'John went to the store. The store was closed.'
        self.doc3 = 'Bob went to the store too.'

        self.tdm_header = ['john', 'and', 'bob', 'are', 'brothers', 'went',
                           'to', 'the', 'store', 'was', 'closed', 'too']
        self.tdm_row1 = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]
        self.tdm_row2 = [1, 0, 0, 0, 0, 1, 1, 2, 2, 1, 1, 0]
        self.tdm_row3 = [0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1]

        self.text1 = """

    Hello there
    how are you today?

    I hope you
    are doing well.

    Thanks for using the textmining module!


    """
        self.splitby_lines1 = ['', '', '    Hello there',
                               '    how are you today?']
        self.splitby_lines2 = ['', '    I hope you', '    are doing well.']
        self.splitby_lines3 = ['',
                               '    Thanks for using the textmining module!']
        self.splitby_lines4 = ['', '', '    ']
        self.text2 = """    Document One:
    -------------

    First line of Document One
    Second line of Document One

    Third line of Document One

    Document Two:
    -------------

    First line of Document Two

    Second line of Document Two
    Document Three:
    ---------------
    First line of Document Three


    """
        self.splitby_doc1 = ['    Document One:', '    -------------', '',
                             '    First line of Document One',
                             '    Second line of Document One', '',
                             '    Third line of Document One', '']
        self.splitby_doc2 = ['    Document Two:', '    -------------', '',
                             '    First line of Document Two', '',
                             '    Second line of Document Two']
        self.splitby_doc3 = ['    Document Three:', '    ---------------',
                             '    First line of Document Three', '', '',
                             '    ']

    def tearDown(self):
        pass

    def test_tdm(self):
        """Test TermDocumentMatrix creation from input docs."""
        tdm = textmining.TermDocumentMatrix()
        tdm.add_doc(self.doc1)
        tdm.add_doc(self.doc2)
        tdm.add_doc(self.doc3)
        tdm_rows = tdm.rows(cutoff=1)
        self.assertListEqual(self.tdm_header, next(tdm_rows))
        self.assertListEqual(self.tdm_row1, next(tdm_rows))
        self.assertListEqual(self.tdm_row2, next(tdm_rows))
        self.assertListEqual(self.tdm_row3, next(tdm_rows))

    def test_splitby_default(self):
        lines = self.text1.splitlines()
        paragraphs = textmining.splitby(lines)
        self.assertListEqual(self.splitby_lines1, next(paragraphs))
        self.assertListEqual(self.splitby_lines2, next(paragraphs))
        self.assertListEqual(self.splitby_lines3, next(paragraphs))
        self.assertListEqual(self.splitby_lines4, next(paragraphs))

    def test_splitby_custom(self):
        lines = self.text2.splitlines()

        def document_boundary(line1, line2):
            return line2.strip().startswith('Document')
        paragraphs = textmining.splitby(lines, document_boundary)
        self.assertListEqual(self.splitby_doc1, next(paragraphs))
        self.assertListEqual(self.splitby_doc2, next(paragraphs))
        self.assertListEqual(self.splitby_doc3, next(paragraphs))

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'textmining.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
