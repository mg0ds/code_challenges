import os
import urllib.request
import collections
import re

# data provided
stopwords_file = os.path.join('/tmp', 'stopwords')
harry_text = os.path.join('/tmp', 'harry')
urllib.request.urlretrieve('http://bit.ly/2EuvyHB', stopwords_file)
urllib.request.urlretrieve('http://bit.ly/2C6RzuR', harry_text)


def get_harry_most_common_word():
    bbb = []
    cnt = collections.Counter()
    words = re.findall(r"[\w']+", open(harry_text).read().lower())
    for a in words:
        if a not in open(stopwords_file).read().lower():
            bbb.append(a)
    v = collections.Counter(bbb).most_common(1)
    tb = []
    for a in v:
        for c in a:
            tb.append(c)
    t = tuple(tb)
    return t
    
