"""A palindrome is a word, phrase, number, or other sequence of characters
which reads the same backward as forward"""
import os
import urllib.request
import requests
import re

TMP = os.getenv("TMP", "/tmp")
DICTIONARY = os.path.join(TMP, 'dictionary_m_words.txt')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/dictionary_m_words.txt',
    DICTIONARY
)


def load_dictionary():
    """Load dictionary (sample) and return as generator (done)"""
    with open(DICTIONARY) as f:
        return (word.lower().strip() for word in f.readlines())


def is_palindrome(word):
    """Return if word is palindrome, 'madam' would be one.
       Case insensitive, so Madam is valid too.
       It should work for phrases too so strip all but alphanumeric chars.
       So "No 'x' in 'Nixon'" should pass (see tests for more)"""
    stripped_string = re.sub(r'\W+', '', word)
    #print(stripped_string)
    if stripped_string.lower() == stripped_string.lower()[::-1]:
        return True
    else:
        return False


def get_longest_palindrome(words=None):
    """Given a list of words return the longest palindrome
       If called without argument use the load_dictionary helper
       to populate the words list"""
      
    word_len = 0
    longest_word = ""
    if words == None:
        words = load_dictionary()
    for word in words:
        stripped_string = re.sub(r'\W+', '', word)
        #print(stripped_string)
        if stripped_string.lower() == stripped_string.lower()[::-1]:
            if len(stripped_string.lower()) > word_len:
                longest_word = word
    print(longest_word)
    return longest_word
