"""
Data module for XPhrase Generation
Contains word lists for English, German, and Portuguese languages
"""

__version__ = "1.0.2"

from .english_words import ENGLISH_WORDS
from .german_words import GERMAN_WORDS
from .portuguese_words import PORTUGUESE_WORDS

__all__ = ['ENGLISH_WORDS', 'GERMAN_WORDS', 'PORTUGUESE_WORDS']
