from random import choice

class WordFinder:
    """Word Finder: finds random words from a dictionary."""

# __init__ calls an internal method
    # internal method reads file and stores each read word in an internal list
# random method that returns a random word from that internal list
    # probably use choice function from the random library?

    def __init__(self, word_file_path):
        """Creates an empty list and calls word_list method"""
        
        file = open(word_file_path)
        self.words = self.parse_words(file) # do an instance method that does this instead
        print(f"{len(self.words)} words read")

        # another function that parses through word file that returns a list
        # adds to list to word list via comprehension

    def __repr__(self):
        """Shows what's in the read words list"""
        return f"Read words: {self.words}"

    def parse_words(self, word_file):
        """Appends each word from text file to words list
            Prints the number of words read from file
        """
        # previous attempts; did not work due to file reading errors
        # read each word in file
        # file = open(f"{word_file_path]}", "r")
        # for line in word_file:
        #     self.words.append(line)
        # file.close()

        # previous attempt; was duplicative code behavior from __init__
        # with open(word_file, "r") as file:
        #     for line in file:
        #         self.words.append(line)
        # # file.close()

        return [word.strip() for word in word_file]

    def random(self):
        """Prints a random word from read words list"""
        return choice(self.words)