#!/usr/bin/env python3
"""
Unit tests for XPhrase Generation
"""

import unittest
import sys
import os
import re
import subprocess
import argparse

# Add the parent directory to the Python path to import the main modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from xphrase import XPhraseGenerator
from word_manager import WordManager


class TestWordManager(unittest.TestCase):
    """Test cases for WordManager class"""
    
    def setUp(self):
        self.word_manager = WordManager()
    
    def test_get_random_word(self):
        """Test that get_random_word returns a non-empty string"""
        word = self.word_manager.get_random_word()
        self.assertIsInstance(word, str)
        self.assertTrue(len(word) > 0)
    
    def test_get_random_word_specific_language(self):
        """Test getting words from specific languages"""
        for lang in ['english', 'german', 'portuguese']:
            word = self.word_manager.get_random_word(lang)
            self.assertIsInstance(word, str)
            self.assertTrue(len(word) > 0)
    
    def test_get_separator(self):
        """Test that separator contains special char and digit"""
        separator = self.word_manager.get_separator()
        self.assertEqual(len(separator), 2)
        
        # Check if first character is a special character
        special_chars = self.word_manager.get_special_characters()
        self.assertIn(separator[0], special_chars)
        
        # Check if second character is a digit
        digits = self.word_manager.get_digits()
        self.assertIn(separator[1], digits)
    
    def test_language_pools_not_empty(self):
        """Test that all language pools have words"""
        for lang, words in self.word_manager.language_pools.items():
            self.assertTrue(len(words) > 0, f"Language pool for {lang} is empty")
            # Test that we can get a word from each pool
            word = self.word_manager.get_random_word(lang)
            self.assertIn(word, words)


class TestXPhraseGenerator(unittest.TestCase):
    """Test cases for XPhraseGenerator class"""
    
    def setUp(self):
        self.generator = XPhraseGenerator()
    
    def test_generate_phrase_default_8_words(self):
        """Test that default command generates exactly 8 words"""
        phrase = self.generator.generate_phrase(8, 8)
        words = self._count_words_in_phrase(phrase)
        self.assertEqual(len(words), 8)
    
    def test_generate_phrase_exact_word_count(self):
        """Test generating phrases with exact word counts (5-10)"""
        for word_count in range(5, 11):
            phrase = self.generator.generate_phrase(word_count, word_count)
            words = self._count_words_in_phrase(phrase)
            self.assertEqual(len(words), word_count)
    
    def test_generate_phrase_custom_range(self):
        """Test generating phrases with custom word range using --min and --max"""
        min_words, max_words = 5, 10
        phrase = self.generator.generate_phrase(min_words, max_words)
        words = self._count_words_in_phrase(phrase)
        self.assertTrue(min_words <= len(words) <= max_words)
    
    def test_generate_phrase_last_word_uppercase(self):
        """Test that last word ends with uppercase letter"""
        phrase = self.generator.generate_phrase(8, 8)
        # Get last character (should be uppercase)
        last_char = phrase[-1]
        self.assertTrue(last_char.isupper(), 
                       f"Last character '{last_char}' is not uppercase in phrase: {phrase}")
    
    def test_generate_phrase_separators_present(self):
        """Test that separators (special char + digit) are present between words"""
        phrase = self.generator.generate_phrase(8, 8)
        
        # Check for pattern: word + special char + digit + word
        pattern = r'[a-zA-ZäöüÄÖÜßáéíóúãõâêîôûàèìòùç]+[!@#$%^&*()_+\-=\[\]{}|;:,.<>?~\\][0-9][a-zA-ZäöüÄÖÜßáéíóúãõâêîôûàèìòùç]+'
        matches = re.findall(pattern, phrase)
        self.assertTrue(len(matches) >= 1, 
                       f"No separators found in phrase: {phrase}")
    
    def test_generate_multiple_phrases(self):
        """Test generating multiple phrases with exact word counts"""
        count = 5
        word_count = 8
        phrases = self.generator.generate_multiple_phrases(count, word_count, word_count)
        
        self.assertEqual(len(phrases), count)
        for phrase in phrases:
            self.assertIsInstance(phrase, str)
            self.assertTrue(len(phrase) > 0)
            words = self._count_words_in_phrase(phrase)
            self.assertEqual(len(words), word_count)
    
    def test_phrase_structure(self):
        """Test the overall structure of generated phrases"""
        phrase = self.generator.generate_phrase(8, 8)
        
        # Should have words separated by special char + digit
        parts = re.split(r'([!@#$%^&*()_+\-=\[\]{}|;:,.<>?~\\][0-9])', phrase)
        
        # Parts should alternate: word, separator, word, separator, etc.
        # For 8 words, we should have 8 words + 7 separators = 15 parts
        self.assertEqual(len(parts), 15)
        
        # Check that words are in even positions
        for i in range(0, len(parts), 2):
            self.assertTrue(parts[i].isalpha() or any(c.isalpha() for c in parts[i]))
        
        # Check that separators are in odd positions
        for i in range(1, len(parts), 2):
            self.assertEqual(len(parts[i]), 2)
            self.assertIn(parts[i][0], self.generator.word_manager.get_special_characters())
            self.assertIn(parts[i][1], self.generator.word_manager.get_digits())
    
    def _count_words_in_phrase(self, phrase):
        """Helper method to count words in a phrase"""
        # Count words by splitting on separators (special char + digit)
        words = re.split(r'[!@#$%^&*()_+\-=\[\]{}|;:,.<>?~\\][0-9]', phrase)
        words = [w for w in words if w]  # Remove empty strings
        return words


class TestCommandLineInterface(unittest.TestCase):
    """Test cases for command line interface"""
    
    def test_default_command_8_words(self):
        """Test that 'python xphrase.py' generates exactly 8 words"""
        result = subprocess.run(['python', 'xphrase.py'], 
                              capture_output=True, text=True, cwd='..')
        self.assertEqual(result.returncode, 0)
        
        phrase = result.stdout.strip()
        words = re.split(r'[!@#$%^&*()_+\-=\[\]{}|;:,.<>?~\\][0-9]', phrase)
        words = [w for w in words if w]
        self.assertEqual(len(words), 8)
    
    def test_count_parameter_valid_range(self):
        """Test --count parameter with valid range (5-10)"""
        for count in range(5, 11):
            result = subprocess.run(['python', 'xphrase.py', '--count', str(count)], 
                                  capture_output=True, text=True, cwd='..')
            self.assertEqual(result.returncode, 0)
            
            phrase = result.stdout.strip()
            words = re.split(r'[!@#$%^&*()_+\-=\[\]{}|;:,.<>?~\\][0-9]', phrase)
            words = [w for w in words if w]
            self.assertEqual(len(words), count)
    
    def test_count_parameter_invalid_range(self):
        """Test --count parameter with invalid range (1-4)"""
        for count in range(1, 5):
            result = subprocess.run(['python', 'xphrase.py', '--count', str(count)], 
                                  capture_output=True, text=True, cwd='..')
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("Error", result.stderr)
    
    def test_min_max_parameters(self):
        """Test --min and --max parameters"""
        result = subprocess.run(['python', 'xphrase.py', '--min', '5', '--max', '10'], 
                              capture_output=True, text=True, cwd='..')
        self.assertEqual(result.returncode, 0)
        
        phrase = result.stdout.strip()
        words = re.split(r'[!@#$%^&*()_+\-=\[\]{}|;:,.<>?~\\][0-9]', phrase)
        words = [w for w in words if w]
        self.assertTrue(5 <= len(words) <= 10)


class TestIntegration(unittest.TestCase):
    """Integration tests for the complete system"""
    
    def test_complete_workflow(self):
        """Test the complete phrase generation workflow"""
        generator = XPhraseGenerator()
        
        # Test default 8-word phrase
        phrase = generator.generate_phrase(8, 8)
        self._verify_phrase_structure(phrase, 8)
        
        # Test multiple phrases with exact word counts
        phrases = generator.generate_multiple_phrases(3, 6, 6)
        self.assertEqual(len(phrases), 3)
        for phrase in phrases:
            self._verify_phrase_structure(phrase, 6)
    
    def _verify_phrase_structure(self, phrase, expected_word_count=None):
        """Helper method to verify phrase structure"""
        # Should not be empty
        self.assertTrue(len(phrase) > 0)
        
        # Should contain mixed content (letters, special chars, digits)
        has_letters = any(c.isalpha() for c in phrase)
        has_special = any(c in '!@#$%^&*()_+-=[]{}|;:,.<>?~\\' for c in phrase)
        has_digits = any(c.isdigit() for c in phrase)
        
        self.assertTrue(has_letters, f"Phrase has no letters: {phrase}")
        self.assertTrue(has_special, f"Phrase has no special chars: {phrase}")
        self.assertTrue(has_digits, f"Phrase has no digits: {phrase}")
        
        # Last character should be uppercase
        self.assertTrue(phrase[-1].isupper(), 
                      f"Last character not uppercase: {phrase}")
        
        # Verify word count if expected
        if expected_word_count is not None:
            words = re.split(r'[!@#$%^&*()_+\-=\[\]{}|;:,.<>?~\\][0-9]', phrase)
            words = [w for w in words if w]
            self.assertEqual(len(words), expected_word_count)


def run_tests():
    """Run all tests and return results"""
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(sys.modules[__name__])
    runner = unittest.TextTestRunner(verbosity=2)
    return runner.run(suite)


if __name__ == '__main__':
    print("Running XPhrase Generation Tests...")
    print("=" * 50)
    
    result = run_tests()
    
    if result.wasSuccessful():
        print("\n✅ All tests passed!")
    else:
        print(f"\n❌ {len(result.failures)} test(s) failed")
        sys.exit(1)
