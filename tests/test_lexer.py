import sys
import os

import unittest
from src.lexer import lexer, Token

class TestLexer(unittest.TestCase):
    def test_empty_input(self):
        """Test that the lexer handles an empty input string."""
        self.assertEqual(lexer(''), [])

    def test_single_token(self):
        """Test that the lexer correctly tokenizes a single known token."""
        self.assertEqual(lexer('apply'), [Token('APPLY', 'apply')])

    def test_ignore_whitespace(self):
        """Test that the lexer ignores spaces and tabs."""
        self.assertEqual(lexer('   \tapply\t   '), [Token('APPLY', 'apply')])

    def test_multiple_tokens(self):
        """Test that the lexer correctly tokenizes a sequence of tokens."""
        expected_tokens = [
            Token('APPLY', 'apply'),
            Token('GATE', 'X'),
            Token('TO', 'to'),
            Token('QUBIT', 'qubit'),
            Token('NUMBER', '0'),
            Token('SEMICOLON', ';')
        ]
        self.assertEqual(lexer('apply X to qubit 0;'), expected_tokens)

    def test_unknown_token(self):
        """Test that the lexer flags an unknown token."""
        with self.assertRaises(SyntaxError):
            lexer('@')

if __name__ == '__main__':
    unittest.main()

