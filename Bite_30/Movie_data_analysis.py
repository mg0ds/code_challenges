import csv
from collections import defaultdict, namedtuple
import os
from urllib.request import urlretrieve

BASE_URL = 'https://bites-data.s3.us-east-2.amazonaws.com/'
TMP = '/tmp'

fname = 'movie_metadata.csv'
remote = os.path.join(BASE_URL, fname)
local = os.path.join(TMP, fname)
urlretrieve(remote, local)

MOVIE_DATA = local
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director():
    """Extracts all movies from csv and stores them in a dict,
    where keys are directors, and values are a list of movies,
    use the defined Movie namedtuple"""
    movies = defaultdict(list)
    with open(local, newline="", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            if row[23] != "title_year" and row[23] != "":
                if int(row[23]) >= MIN_YEAR:
                    movies[row[1]].append(Movie(title=row[11].replace('\xa0', ''), year=row[23], score=row[25]))
    return movies


def calc_mean_score(movies):
    """Helper method to calculate mean of list of Movie namedtuples,
       round the mean to 1 decimal place"""
    sum = 0
    for p in movies:
        sum += float(p.score)
    mean = sum/len(movies)
    return round(mean,1)


def get_average_scores(directors):
    """Iterate through the directors dict (returned by get_movies_by_director),
       return a list of tuples (director, average_score) ordered by highest
       score in descending order. Only take directors into account
       with >= MIN_MOVIES"""
    def takeSecond(elem):
        return elem[1]
    order = []
    print(directors)
    bufor = "brak"
    mov = get_movies_by_director()
    for f in mov:
        if len(mov[f]) >= MIN_MOVIES:
            sum = 0
            for a in mov[f]:
                sum += float(a.score)
            mean = sum / len(mov[f])
            if f != bufor:
                e = (f, round(mean,1))
                order.append(e)
        bufor = f
    order.sort(key=takeSecond, reverse=True)
    return order
