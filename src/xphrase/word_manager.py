import random
from .data.english_words import ENGLISH_WORDS
from .data.german_words import GERMAN_WORDS  
from .data.portuguese_words import PORTUGUESE_WORDS

class WordManager:
    def __init__(self):
        self.language_pools = {
            'english': ENGLISH_WORDS,
            'german': GERMAN_WORDS,
            'portuguese': PORTUGUESE_WORDS 
        }
        
    def get_random_word(self, language=None):
        """Get a random word from specified language or any language"""
        if language and language in self.language_pools:
            return random.choice(self.language_pools[language])
        else:
            # Choose random language
            lang = random.choice(list(self.language_pools.keys()))
            return random.choice(self.language_pools[lang])
    
    def get_special_characters(self):
        """Return special characters for separation"""
        return "!@#$%^&*()_+-=[]{}|;:,.<>?~\\"
    
    def get_digits(self):
        """Return digits for separation"""
        return "0123456789"
    
    def get_separator(self):
        """Get a random separator (special char + digit)"""
        special_char = random.choice(self.get_special_characters())
        digit = random.choice(self.get_digits())
        return f"{special_char}{digit}"
