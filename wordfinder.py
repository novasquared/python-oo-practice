from random import choice

class WordFinder:
    """Word Finder: finds random words from a dictionary."""

# __init__ calls an internal method
    # internal method reads file and stores each read word in an internal list
# random method that returns a random word from that internal list
    # probably use choice function from the random library?

    def __init__(self, word_file_path):
        """Initializes a file object, 
            stores words read from the file in a list, 
            and prints the number of words read"""
        
        file = open(word_file_path)
        self.words = self.parse_words(file)
        print(f"{len(self.words)} words read")

        # another function that parses through word file that returns a list
        # adds to list to word list via comprehension

    def __repr__(self):
        """Shows what's in the read words list"""
        return f"Read words: {self.words}"

    def parse_words(self, word_file):
        """Returns words from the word list stripped of white space"""
        # reads words from file and strips white space would be a better comment
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
        """Returns a random word from read words list"""
        return choice(self.words)


class SpecialWordFinder(WordFinder):
    """Special Word Finder: finds random words from a dictionary, 
    ignoring empty lines and comment lines."""

    def parse_words(self, word_file):
        """Returns a words list that ignores empty strings and comments"""
        # Overwrites parent function.  
        return [word.strip() for word in word_file   #word for word in super.parseWords() and omit the \n check
                    if not word.startswith("\n") 
                    and not word.startswith("#")]
