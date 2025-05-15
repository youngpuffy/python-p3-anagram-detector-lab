# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()


    def match(self, word_list):
        sorted_original = sorted(self.word)
        return[
            candidate for candidate in word_list
            if sorted(candidate.lower()) == sorted_original and candidate.lower() != self.word
        ]