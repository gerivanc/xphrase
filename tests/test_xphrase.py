#!/usr/bin/env python3
"""
Unit tests for XPhrase Generation
"""

import unittest
import sys
import os
import re

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
    
    def test_generate_phrase_word_count(self):
        """Test that generated phrases have correct word count range"""
        # Test multiple times to account for randomness
        for _ in range(10):
            phrase = self.generator.generate_phrase(5, 10)
            # Count words by splitting on separators (special char + digit)
            words = re.split(r'[!@#$%^&*()_+\-=\[\]{}|;:,.<>?~\\][0-9]', phrase)
            words = [w for w in words if w]  # Remove empty strings
            self.assertTrue(5 <= len(words) <= 10)
    
    def test_generate_phrase_last_word_uppercase(self):
        """Test that last word ends with uppercase letter"""
        phrase = self.generator.generate_phrase(3, 3)
        # Get last character (should be uppercase)
        last_char = phrase[-1]
        self.assertTrue(last_char.isupper(), 
                       f"Last character '{last_char}' is not uppercase in phrase: {phrase}")
    
    def test_generate_phrase_separators_present(self):
        """Test that separators (special char + digit) are present between words"""
        phrase = self.generator.generate_phrase(3, 3)
        
        # Check for pattern: word + special char + digit + word
        pattern = r'[a-zA-ZäöüÄÖÜßáéíóúãõâêîôûàèìòùç]+[!@#$%^&*()_+\-=\[\]{}|;:,.<>?~\\][0-9][a-zA-ZäöüÄÖÜßáéíóúãõâêîôûàèìòùç]+'
        matches = re.findall(pattern, phrase)
        self.assertTrue(len(matches) >= 1, 
                       f"No separators found in phrase: {phrase}")
    
    def test_generate_multiple_phrases(self):
        """Test generating multiple phrases"""
        count = 5
        phrases = self.generator.generate_multiple_phrases(count)
        
        self.assertEqual(len(phrases), count)
        for phrase in phrases:
            self.assertIsInstance(phrase, str)
            self.assertTrue(len(phrase) > 0)
    
    def test_generate_phrase_custom_range(self):
        """Test generating phrases with custom word range"""
        min_words, max_words = 7, 12
        phrase = self.generator.generate_phrase(min_words, max_words)
        
        words = re.split(r'[!@#$%^&*()_+\-=\[\]{}|;:,.<>?~\\][0-9]', phrase)
        words = [w for w in words if w]
        self.assertTrue(min_words <= len(words) <= max_words)
    
    def test_phrase_structure(self):
        """Test the overall structure of generated phrases"""
        phrase = self.generator.generate_phrase(4, 4)
        
        # Should have words separated by special char + digit
        parts = re.split(r'([!@#$%^&*()_+\-=\[\]{}|;:,.<>?~\\][0-9])', phrase)
        
        # Parts should alternate: word, separator, word, separator, word, separator, word
        self.assertEqual(len(parts), 7)  # 4 words + 3 separators
        
        # Check that words are in even positions (0, 2, 4, 6)
        for i in [0, 2, 4, 6]:
            self.assertTrue(parts[i].isalpha() or any(c.isalpha() for c in parts[i]))
        
        # Check that separators are in odd positions (1, 3, 5)
        for i in [1, 3, 5]:
            self.assertEqual(len(parts[i]), 2)
            self.assertIn(parts[i][0], self.generator.word_manager.get_special_characters())
            self.assertIn(parts[i][1], self.generator.word_manager.get_digits())


class TestIntegration(unittest.TestCase):
    """Integration tests for the complete system"""
    
    def test_complete_workflow(self):
        """Test the complete phrase generation workflow"""
        generator = XPhraseGenerator()
        
        # Generate multiple phrases
        phrases = generator.generate_multiple_phrases(3)
        
        # Verify all phrases meet requirements
        for phrase in phrases:
            # Should not be empty
            self.assertTrue(len(phrase) > 0)
            
            # Should contain mixed content (letters, special chars, digits)
            has_letters = any(c.isalpha() for c in phrase)
            has_special = any(c in generator.word_manager.get_special_characters() for c in phrase)
            has_digits = any(c.isdigit() for c in phrase)
            
            self.assertTrue(has_letters, f"Phrase has no letters: {phrase}")
            self.assertTrue(has_special, f"Phrase has no special chars: {phrase}")
            self.assertTrue(has_digits, f"Phrase has no digits: {phrase}")
            
            # Last character should be uppercase
            self.assertTrue(phrase[-1].isupper(), 
                          f"Last character not uppercase: {phrase}")


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
