#!/usr/bin/env python3
import random
import sys
import argparse
try:
    # Try absolute import first (for installed package)
    from xphrase.word_manager import WordManager
except ImportError:
    # Fallback to relative import (for development)
    from word_manager import WordManager

class XPhraseGenerator:
    def __init__(self):
        self.word_manager = WordManager()
        
    def generate_phrase(self, min_words=3, max_words=21):
        """Generate a phrase with mixed language words and separators"""
        num_words = random.randint(min_words, max_words)
        words = []
        
        # Generate random words from different languages
        for _ in range(num_words):
            word = self.word_manager.get_random_word()
            words.append(word)
        
        # Process last word to end with uppercase
        if words:
            last_word = words[-1]
            if last_word:
                # Ensure last character is uppercase
                last_word_processed = last_word[:-1] + last_word[-1].upper()
                words[-1] = last_word_processed
        
        # Join words with separators
        phrase_parts = []
        for i, word in enumerate(words):
            phrase_parts.append(word)
            if i < len(words) - 1:  # Add separator after each word except last
                separator = self.word_manager.get_separator()
                phrase_parts.append(separator)
        
        return ''.join(phrase_parts)
    
    def generate_multiple_phrases(self, count=5, min_words=3, max_words=21):
        """Generate multiple phrases"""
        phrases = []
        for _ in range(count):
            phrases.append(self.generate_phrase(min_words, max_words))
        return phrases

def main():
    """Main CLI function with argument support"""
    parser = argparse.ArgumentParser(description='XPhrase Generation - Expressive phrase generator')
    parser.add_argument('--version', action='store_true', help='Show version information')
    parser.add_argument('--count', type=int, default=None, help='Number of words per phrase (5-10)')
    parser.add_argument('--min', type=int, default=3, help='Minimum words per phrase (default: 3)')
    parser.add_argument('--max', type=int, default=21, help='Maximum words per phrase (default: 21)')
    parser.add_argument('--interactive', action='store_true', help='Run in interactive mode')
    
    args = parser.parse_args()
    
    if args.version:
        print("XPhrase Generation v1.0.2")
        return
    
    generator = XPhraseGenerator()
    
    # If interactive mode or no arguments (except --version)
    if args.interactive:
        run_interactive_mode(generator)
        return
    
    # Command-line mode
    if args.count is None:
        # Default behavior: generate single phrase with exactly 8 words
        phrase = generator.generate_phrase(8, 8)
        print(phrase)
    elif 5 <= args.count <= 10:
        # Generate single phrase with exactly the specified number of words (5-10)
        phrase = generator.generate_phrase(args.count, args.count)
        print(phrase)
    else:
        print("Error: --count parameter must be between 5 and 10")
        sys.exit(1)

def run_interactive_mode(generator):
    """Run the interactive menu mode"""
    print("XPhrase Generation - Expressive phrase generator")
    print("=" * 50)
    
    while True:
        try:
            print("\nOptions:")
            print("1. Generate single phrase")
            print("2. Generate multiple phrases")
            print("3. Exit")
            
            choice = input("\nEnter your choice (1-3): ").strip()
            
            if choice == '1':
                while True:
                    try:
                        num_words = int(input("Generate between 3-21 words? "))
                        if 3 <= num_words <= 21:
                            phrase = generator.generate_phrase(num_words, num_words)
                            print(f"\nGenerated phrase: {phrase}")
                            break
                        else:
                            print("Please enter a number between 3 and 21.")
                    except ValueError:
                        print("Please enter a valid number.")
                
            elif choice == '2':
                # Get number of words per phrase
                while True:
                    try:
                        words_per_phrase = int(input("Generate between 3-21 words per phrase? "))
                        if 3 <= words_per_phrase <= 21:
                            break
                        else:
                            print("Please enter a number between 3 and 21.")
                    except ValueError:
                        print("Please enter a valid number.")
                
                # Get number of phrases
                while True:
                    try:
                        num_phrases = int(input("Generate between 5-10 phrases? "))
                        if 5 <= num_phrases <= 10:
                            break
                        else:
                            print("Please enter a number between 5 and 10.")
                    except ValueError:
                        print("Please enter a valid number.")
                
                phrases = generator.generate_multiple_phrases(num_phrases, words_per_phrase, words_per_phrase)
                print(f"\nGenerated {num_phrases} phrases:")
                for i, phrase in enumerate(phrases, 1):
                    print(f"{i}. {phrase}")
                    
            elif choice == '3':
                print("Goodbye!")
                break
                
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
                
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
