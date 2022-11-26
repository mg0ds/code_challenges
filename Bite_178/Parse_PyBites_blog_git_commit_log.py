from collections import Counter
import os
from urllib.request import urlretrieve
from dateutil.parser import parse
import datetime
import re

commits = os.path.join(os.getenv("TMP", "/tmp"), 'commits.txt')
filepath, header = urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/git_log_stat.out',
    commits
)


# you can use this constant as key to the yyyymm:count dict
YEAR_MONTH = '{y}-{m:02d}'


def get_min_max_amount_of_commits(commit_log: str = commits,
                                  year: int = None) -> (str, str):
    """
    Calculate the amount of inserts / deletes per month from the
    provided commit log.

    Takes optional year arg, if provided only look at lines for
    that year, if not, use the entire file.

    Returns a tuple of (least_active_month, most_active_month)
    """
    changes_per_y = {}
    with open(commit_log) as aa:
        for i in aa:
            date_modified, changes = i.split(" | ")
            date_modified = date_modified.replace("Date:   ", "")
            date_short = parse(date_modified)
            date_short = date_short.strftime("%Y"+"-"+"%m")
            changes = changes.split(", ")
            changes_n = [int(re.findall('\d+', x)[0]) for x in changes]
            if changes_per_y.get(date_short) != None:
                changes_per_y[date_short] = changes_per_y[date_short] + sum(changes_n[1:])
            else:
                changes_per_y[date_short] = sum(changes_n[1:])
    
    max_qt = 0
    min_qt = 99999999
    max_y = ""
    min_y = ""
    for date, qt in changes_per_y.items():
        if date[:4] == str(year) or year == None:
            if qt > max_qt:
                max_qt = qt
                max_y = date
            elif qt < min_qt:
                min_qt = qt
                min_y = date
    result = (min_y, max_y)
    print(result)
    return result
            
