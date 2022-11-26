import itertools
import os
import urllib.request

# PREWORK
TMP = os.getenv("TMP", "/tmp")
DICT = 'dictionary.txt'
DICTIONARY = os.path.join(TMP, DICT)
urllib.request.urlretrieve(
    f'https://bites-data.s3.us-east-2.amazonaws.com/{DICT}',
    DICTIONARY
)

with open(DICTIONARY) as f:
    dictionary = set([word.strip().lower() for word in f.read().split()])


def get_possible_dict_words(draw):
    """Get all possible words from a draw (list of letters) which are
       valid dictionary words. Use _get_permutations_draw and provided
       dictionary"""
    slowa = []
    for line in dictionary:
        if len(line) <= len(draw):
            #print(line)
            drawtemp = str(draw)
            a = 0
            for letter in line:
                if letter.upper() in drawtemp:
                    drawtemp = drawtemp.replace(letter.upper(), "")
                    #print(drawtemp)
                    a += 1
                    if a == len(line):
                        #print(a)
                        #print(len(line))
                        #print(line)
                        slowa.append(str(line))
                else:
                    pass
    return slowa

def _get_permutations_draw(draw):
    """Helper to get all permutations of a draw (list of letters), hint:
       use itertools.permutations (order of letters matters)"""
    pass
