import os
import urllib.request

LOG = os.path.join('/tmp', 'safari.logs')
PY_BOOK, OTHER_BOOK = '🐍', '.'
urllib.request.urlretrieve('http://bit.ly/2BLsCYc', LOG)


def create_chart():
    d = ""
    koniec = ""
    with open(LOG, "r", newline="") as log:
        for a in log:
            if "sending to slack channel" in a:
                data = d[0:5]
                if data not in koniec:
                    koniec = koniec +"\n"+data + " "
                    if "python" in d.lower():
                        koniec = koniec + PY_BOOK
                    else:
                        koniec = koniec + OTHER_BOOK
                else:
                    if "python" in d.lower():
                        koniec = koniec + PY_BOOK
                    else:
                        koniec = koniec + OTHER_BOOK
            else:
                pass
            d = a
    print(koniec)
    pass
