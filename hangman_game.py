"""
WORD GUESSING GAME - Hangman Style
Author: Original code for learning purposes
Concepts: Functions, lists, strings, loops, conditionals, file I/O
"""

import random
import os

class WordGuessingGame:
    """
    A word guessing game where player tries to guess a secret word
    letter by letter before running out of attempts.
    """
    
    def __init__(self, word_list=None):
        """
        Initialize the game with a word list or default words
        """
        if word_list is None:
            self.word_list = ["PYTHON", "JAVA", "RUBY", "HTML", "CSS", 
                              "ALGORITHM", "DATABASE", "NETWORK"]
        else:
            self.word_list = word_list
        
        self.secret_word = ""
        self.guessed_letters = []
        self.max_attempts = 6
        self.attempts_left = 6
        self.game_over = False
        self.won = False
    
    def choose_secret_word(self):
        """Randomly select a word from the word list"""
        self.secret_word = random.choice(self.word_list).upper()
        return self.secret_word
    
    def display_word_state(self):
        """
        Show the word with guessed letters revealed, others as underscores
        Example: If word is PYTHON and guessed P, N: P _ _ _ _ N
        """
        display = ""
        for letter in self.secret_word:
            if letter in self.guessed_letters:
                display += letter + " "
            else:
                display += "_ "
        return display.strip()
    
    def make_guess(self, letter):
        """
        Process a player's guess
        Returns: (correct_guess, message)
        """
        letter = letter.upper()
        
        # Input validation
        if len(letter) != 1 or not letter.isalpha():
            return False, "Please enter a single letter!"
        
        if letter in self.guessed_letters:
            return False, f"You already guessed '{letter}'. Try another!"
        
        # Add to guessed letters
        self.guessed_letters.append(letter)
        
        # Check if guess is correct
        if letter in self.secret_word:
            # Check if player won
            if all(l in self.guessed_letters for l in self.secret_word):
                self.game_over = True
                self.won = True
                return True, f"Correct! You've won! The word was {self.secret_word}"
            return True, f"Good guess! '{letter}' is in the word."
        else:
            self.attempts_left -= 1
            if self.attempts_left <= 0:
                self.game_over = True
                self.won = False
                return False, f"Game Over! The word was {self.secret_word}"
            return False, f"Sorry, '{letter}' is not in the word. Attempts left: {self.attempts_left}"
    
    def get_game_state(self):
        """Return current game state as dictionary"""
        return {
            'word_state': self.display_word_state(),
            'attempts_left': self.attempts_left,
            'guessed_letters': sorted(self.guessed_letters),
            'game_over': self.game_over,
            'won': self.won
        }
    
    def reset_game(self):
        """Start a new game"""
        self.secret_word = ""
        self.guessed_letters = []
        self.attempts_left = self.max_attempts
        self.game_over = False
        self.won = False
        self.choose_secret_word()


def load_words_from_file(filename="words.txt"):
    """Try to load words from a file, return None if file doesn't exist"""
    try:
        with open(filename, 'r') as file:
            words = [line.strip().upper() for line in file if line.strip()]
        return words if words else None
    except FileNotFoundError:
        return None


def display_hangman(attempts_left):
    """Display ASCII hangman based on attempts left"""
    stages = [
        """
           -----
           |   |
           O   |
          /|\  |
          / \  |
               |
        =========
        """,  # 0 attempts left - full hangman
        """
           -----
           |   |
           O   |
          /|\  |
          /    |
               |
        =========
        """,  # 1 attempt left
        """
           -----
           |   |
           O   |
          /|\  |
               |
               |
        =========
        """,  # 2 attempts left
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        =========
        """,  # 3 attempts left
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        =========
        """,  # 4 attempts left
        """
           -----
           |   |
           O   |
               |
               |
               |
        =========
        """,  # 5 attempts left
        """
           -----
           |   |
               |
               |
               |
               |
        =========
        """   # 6 attempts left - empty
    ]
    
    # attempts_left goes from 6 to 0, we need index from 0 to 6
    index = 6 - attempts_left
    if index < 0:
        index = 0
    elif index >= len(stages):
        index = len(stages) - 1
    
    return stages[index]

def play_game():
    """Main game loop"""
    print("=" * 50)
    print("         WELCOME TO WORD GUESSING GAME")
    print("=" * 50)
    
    # Try to load custom words, use defaults if file not found
    custom_words = load_words_from_file()
    if custom_words:
        print(f"Loaded {len(custom_words)} custom words!")
        game = WordGuessingGame(custom_words)
    else:
        print("Using default word list (create 'words.txt' for custom words)")
        game = WordGuessingGame()
    
    game.choose_secret_word()
    
    while not game.game_over:
        # Clear screen for better experience (optional)
        # os.system('cls' if os.name == 'nt' else 'clear')
        
        print("\n" + "=" * 40)
        print(display_hangman(game.attempts_left))
        print("\nWord: ", game.display_word_state())
        print(f"Attempts left: {game.attempts_left}")
        print(f"Guessed letters: {', '.join(sorted(game.guessed_letters))}")
        
        guess = input("\nEnter a letter: ").strip()
        
        if not guess:  # Empty input
            continue
        
        correct, message = game.make_guess(guess)
        print("\n" + message)
        
        if game.game_over:
            play_again = input("\nPlay again? (y/n): ").strip().lower()
            if play_again == 'y':
                game.reset_game()
            else:
                print("Thanks for playing! 👋")
                break

def quick_demo():
    """Quick demonstration of the game class without the full interface"""
    print("\n📚 QUICK DEMO - Understanding the WordGuessingGame class\n")
    
    # Create a game
    game = WordGuessingGame(["TEST"])
    game.secret_word = "TEST"
    
    print("1. Initial state:")
    print(f"   Word display: {game.display_word_state()}")
    print(f"   Attempts: {game.attempts_left}")
    
    print("\n2. Guess 'T' (correct):")
    result, msg = game.make_guess("T")
    print(f"   {msg}")
    print(f"   Word now: {game.display_word_state()}")
    
    print("\n3. Guess 'E' (correct):")
    result, msg = game.make_guess("E")
    print(f"   {msg}")
    print(f"   Word now: {game.display_word_state()}")
    
    print("\n4. Guess 'X' (wrong):")
    result, msg = game.make_guess("X")
    print(f"   {msg}")
    print(f"   Attempts left: {game.attempts_left}")
    
    print("\n5. Get full game state:")
    state = game.get_game_state()
    for key, value in state.items():
        print(f"   {key}: {value}")


# Main execution
if __name__ == "__main__":
    # Run demo first to understand the class
    quick_demo()
    
    # Uncomment below to play the full game
    # play_game()
    
    print("\n" + "=" * 50)
    # Study this code! Try to understand:
    # • How the class is structured
    # • How methods work together
    # • The difference between class and functions
    # • Error handling with try/except
    print("=" * 50)