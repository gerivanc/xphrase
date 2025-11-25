#!/usr/bin/env python3
"""
Unit tests for XPhrase Generation
"""
import unittest
import sys
import os
import re
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
SRC_PATH = os.path.join(PROJECT_ROOT, 'src')
if SRC_PATH not in sys.path:
    sys.path.insert(0, SRC_PATH)

# Agora os imports absolutos funcionam perfeitamente
from xphrase.main import XPhraseGenerator, main
from xphrase.word_manager import WordManager


class TestWordManager(unittest.TestCase):
    def setUp(self):
        self.wm = WordManager()

    def test_get_random_word(self):
        word = self.wm.get_random_word()
        self.assertIsInstance(word, str)
        self.assertGreater(len(word), 0)

    def test_get_random_word_specific_language(self):
        for lang in ['english', 'german', 'portuguese']:
            word = self.wm.get_random_word(lang)
            self.assertIsInstance(word, str)
            self.assertGreater(len(word), 0)

    def test_get_separator(self):
        sep = self.wm.get_separator()
        self.assertEqual(len(sep), 2)
        self.assertIn(sep[0], self.wm.get_special_characters())
        self.assertIn(sep[1], self.wm.get_digits())

    def test_language_pools_not_empty(self):
        for lang, pool in self.wm.language_pools.items():
            self.assertGreater(len(pool), 0)


class TestXPhraseGenerator(unittest.TestCase):
    def setUp(self):
        self.gen = XPhraseGenerator()

    def _count_words(self, phrase):
        words = re.split(r'[!@#$%^&*()_+\-=\[\]{}|;:,.<>?~\\][0-9]', phrase)
        return [w for w in words if w]

    def test_default_8_words(self):
        phrase = self.gen.generate_phrase(8, 8)
        self.assertEqual(len(self._count_words(phrase)), 8)

    def test_exact_word_count(self):
        for n in range(5, 11):
            phrase = self.gen.generate_phrase(n, n)
            self.assertEqual(len(self._count_words(phrase)), n)

    def test_range_min_max(self):
        phrase = self.gen.generate_phrase(5, 10)
        count = len(self._count_words(phrase))
        self.assertTrue(5 <= count <= 10)

    def test_last_character_uppercase(self):
        phrase = self.gen.generate_phrase(8, 8)
        self.assertTrue(phrase and phrase[-1].isupper())

    def test_separators_present(self):
        phrase = self.gen.generate_phrase(8, 8)
        self.assertRegex(phrase, r'[!@#$%^&*()_+\-=\[\]{}|;:,.<>?~\\][0-9]')

    def test_multiple_phrases(self):
        phrases = self.gen.generate_multiple_phrases(5, 6, 6)
        self.assertEqual(len(phrases), 5)
        for p in phrases:
            self.assertEqual(len(self._count_words(p)), 6)


class TestIntegration(unittest.TestCase):
    def test_full_workflow(self):
        gen = XPhraseGenerator()
        phrase = gen.generate_phrase(10, 10)
        words = re.split(r'[!@#$%^&*()_+\-=\[\]{}|;:,.<>?~\\][0-9]', phrase)
        words = [w for w in words if w]
        self.assertEqual(len(words), 10)
        self.assertTrue(phrase[-1].isupper())
        self.assertIn(any(c.isdigit() for c in phrase), [True])


if __name__ == '__main__':
    unittest.main(verbosity=2)
