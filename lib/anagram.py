# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word
        
    def match(self, word_list):
        anagrams = []
        for word in word_list:
            if sorted(word) == sorted(self.word):
                anagrams.append(word)
        return anagrams