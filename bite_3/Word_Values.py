import os
import urllib.request

# PREWORK
DICTIONARY = os.path.join('/tmp', 'dictionary.txt')
urllib.request.urlretrieve('http://bit.ly/2iQ3dlZ', DICTIONARY)
scrabble_scores = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                   (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]
LETTER_SCORES = {letter: score for score, letters in scrabble_scores
                 for letter in letters.split()}


# start coding

def load_words():
    """Load the words dictionary (DICTIONARY constant) into a list and return it"""
    di = []
    f = open(DICTIONARY, 'r')
    for word in f:
        di.append(word.strip("\n"))
    return di


def calc_word_value(word):
    """Given a word calculate its value using the LETTER_SCORES dict"""
    score = 0
    for l in word.upper():
        if LETTER_SCORES.get(l) == None:
            score += 0
        else:
            score += LETTER_SCORES.get(l)
    return score


def max_word_value(words):
    """Given a list of words calculate the word with the maximum value and return it"""
    mscore = 0
    naj = ""
    for word in words:
        score = 0
        for l in word.upper():
            if LETTER_SCORES.get(l) == None:
                score += 0
            else:
                score += LETTER_SCORES.get(l)
        if score > mscore:
            mscore = score
            naj = word
    print(naj)
    return naj
