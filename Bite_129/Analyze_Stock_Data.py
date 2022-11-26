import requests

STOCK_DATA = 'https://bites-data.s3.us-east-2.amazonaws.com/stocks.json'

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(STOCK_DATA).json()


# your turn:

def _cap_str_to_mln_float(cap):
    """If cap = 'n/a' return 0, else:
       - strip off leading '$',
       - if 'M' in cap value, strip it off and return value as float,
       - if 'B', strip it off and multiple by 1,000 and return
         value as float"""
    if cap =="n/a":
        #row["cap"] = 0
        #print(row["name"]+" "+"cap: 0")
        return 0
    else:
        ncap = cap.strip("$")
        if ncap[-1] == "M":
            #print(row["name"]+" "+"cap: %.2f" %float(ncap.strip("M")))
            return float(ncap.strip("M"))
        elif ncap[-1] == "B":
            #fncap = float(ncap.strip("B"))*1000
            #print(row["name"]+" "+"cap: %.2f" %fncap)
            return float(ncap.strip("B"))*1000
        #print(row["cap"])

def get_industry_cap(industry):
    """Return the sum of all cap values for given industry, use
       the _cap_str_to_mln_float to parse the cap values,
       return a float with 2 digit precision"""
    indu = 0
    for row in data:
        if row["industry"] == industry:
            indu += _cap_str_to_mln_float(row["cap"])
    return float(format(indu, ".2f"))


def get_stock_symbol_with_highest_cap():
    """Return the stock symbol (e.g. PACD) with the highest cap, use
       the _cap_str_to_mln_float to parse the cap values"""
    result = ""
    max = 0
    for row in data:
        if _cap_str_to_mln_float(row["cap"]) > max:
            max = _cap_str_to_mln_float(row["cap"])
            result = row["symbol"]
    return result


def get_sectors_with_max_and_min_stocks():
    """Return a tuple of the sectors with most and least stocks,
       discard n/a"""
    sdict = {}
    for row in data:
        sec = _cap_str_to_mln_float(row["cap"])
        if row["sector"] not in sdict:
            sdict[row["sector"]] = float(sec)
        else:
            x = sdict[row["sector"]]
            a = x + sec
            sdict[row["sector"]] = a
    maxmin = (max(sdict, key=sdict.get), min(sdict, key=sdict.get))
    return maxmin
