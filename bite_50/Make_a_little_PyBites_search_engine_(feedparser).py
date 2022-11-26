from collections import namedtuple
from datetime import date

import feedparser

FEED = 'https://bites-data.s3.us-east-2.amazonaws.com/all.rss.xml'

Entry = namedtuple('Entry', 'date title link tags')


def _convert_struct_time_to_dt(stime):
    """Convert a time.struct_time as returned by feedparser into a
    datetime.date object, so:
    time.struct_time(tm_year=2016, tm_mon=12, tm_mday=28, ...)
    -> date(2016, 12, 28)
    """
    return date(*stime[:3])


def get_feed_entries(feed=FEED):
    """Use feedparser to parse PyBites RSS feed.
       Return a list of Entry namedtuples (date = date, drop time part)
    """
    fp = feedparser.parse(feed)
    nt = []

    for f in fp.entries:
        nt.append(Entry(_convert_struct_time_to_dt(f["published_parsed"]), f["title"], 
        f["link"], [x["term"].lower() for x in f["tags"]]))
    return list(nt)

def filter_entries_by_tag(search, entry):
    """Check if search matches any tags as stored in the Entry namedtuple
       (case insensitive, only whole, not partial string matches).
       Returns bool: True if match, False if not.
       Supported searches:
       1. If & in search do AND match,
          e.g. flask&api should match entries with both tags
       2. Elif | in search do an OR match,
          e.g. flask|django should match entries with either tag
       3. Else: match if search is in tags
    """
    if isinstance(entry, list):
        entry = entry[0]
        
    if "&" in search:
        sl = search.lower().split("&")
        c = 0
        for s in sl:
            if s in entry.tags:
                c += 1
        if c == len(sl):
            return True
        else:
            return False
    elif "|" in search:
        sl = search.lower().split("|")
        for s in sl:
            if s in entry.tags:
                return True
            else:
                return False
    else:
        return search.lower() in entry.tags
    

def main():
    """Entry point to the program
       1. Call get_feed_entries and store them in entries
       2. Initiate an infinite loop
       3. Ask user for a search term:
          - if enter was hit (empty string), print 'Please provide a search term'
          - if 'q' was entered, print 'Bye' and exit/break the infinite loop
       4. Filter/match the entries (see filter_entries_by_tag docstring)
       5. Print the title of each match ordered by date ascending
       6. Secondly, print the number of matches: 'n entries matched'
          (use entry if only 1 match)
    """
    entries = get_feed_entries(FEED)
    while(True):
        search = input("Search for (q for exit):")
        if search == "":
            print("Please provide a search term")
        elif search == "q":
            print("Bye")
            break
        else:
            result = []
            for en in entries:
                    if filter_entries_by_tag(search, en):
                        result.append([en.date, en.title])
            if len(result) == 0:
                print("0 entries matched")
            else:
                result.sort(reverse=False, key=lambda x: x[0])
                for poz in result:
                    print(poz[1])
                if len(result) == 1:
                    print("{} entry matched".format(len(result)))
                else:
                    print("{} entries matched".format(len(result)))
        


if __name__ == '__main__':
    main()
