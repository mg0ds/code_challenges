from typing import List


def common_words(sentence1: List[str], sentence2: List[str]) -> List[str]:
    """
    Input:  Two sentences - each is a  list of words in case insensitive ways.
    Output: those common words appearing in both sentences. Capital and lowercase 
            words are treated as the same word. 

            If there are duplicate words in the results, just choose one word. 
            Returned words should be sorted by word's length.
    """
    s1 = [word.lower() for word in sentence1]
    s1 = set(s1)
    s2 = [word.lower() for word in sentence2]
    s2 = set(s2)
    output = []

    for word in s1:
        if word in s2:
            output.append(word)
    return sorted(output, key=len)
