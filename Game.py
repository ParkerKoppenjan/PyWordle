import random
import sys



class Game:
    """
    Implements Wordle game logic with colored feedback for guesses.
    Uses separate lists for valid guesses and possible answers.
    """

    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    RESET = '\033[0m'

    @staticmethod
    def get_answer_list():
        """Loads possible answers from file, returning uppercase list."""
        words = []
        with open('answerlist.txt', 'r') as file:
            for line in file:
                words.append(line.strip().upper())
        return words

    WORDS = get_answer_list()

    @staticmethod
    def get_valid_set():
        """Loads possible answers from file, returning uppercase set. O(1) efficiency!!!"""
        words = set()
        with open('valid-wordle-words.txt', 'r') as file:
            for line in file:
                words.add(line.strip().upper())
        return words

    VALID_GUESSES = get_valid_set()

    def __init__(self):
        self.random_word = random.choice(Game.WORDS)
        self.guess_count = 0

    def play_game(self):
        """Main game loop. Handles up to 6 guesses or until word is found."""
        print("Welcome to Wordle!")
        while self.guess_count < 6:
            result = self.guess()
            print(result)
        print(f"The word was: {self.random_word}")

    def guess(self):
        """
        Processes a single guess attempt.
        Returns: Colored string showing correct letters (blue),
        correct letters in wrong position (yellow), and incorrect letters.
        """
        while True:
            word_guess = (input("Enter a guess: ")).upper()
            if word_guess not in Game.VALID_GUESSES: #ensures input is a valid word and 5 characters
                print("Invalid guess, try again.")
            else:
                break

        self.guess_count += 1
        if word_guess == self.random_word: # win condition
            print("Congratulations, you win :)")
            sys.exit()

        # if input is not invalid or winning, the following:
        back = list("_____") #empty return list, converted to string at end
        remaining_indices = {0, 1, 2, 3, 4}
        for rep in range(5):
            if word_guess[rep] == self.random_word[rep]:
                back[rep] = f"{Game.BLUE}{word_guess[rep]}{Game.RESET}" #if letter in guess matches letter in random word with position, it is blue
                remaining_indices.remove(rep)
        seen = {}

        for char in self.random_word: #converts the random word to a dict, with chars and their frequency
            if char not in seen:
                seen[char] = 1
            else:
                seen[char] += 1

        for rep in remaining_indices:
            if word_guess[rep] in seen and seen[word_guess[rep]] > 0:
                back[rep] = f"{Game.YELLOW}{word_guess[rep]}{Game.RESET}" # if letter matches letter in random word but does not match position, it is yellow
                seen[word_guess[rep]] -= 1
            else:
                back[rep] = word_guess[rep]

        back = ''.join(back)
        return back

def main():
    game = Game()
    game.play_game()

if __name__ == "__main__":
    main()



















