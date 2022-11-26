import json
import os
from pathlib import Path
from typing import Dict, List, Union
from urllib.request import urlretrieve
import pandas as pd  # type: ignore
import requests

URL: str = "https://bites-data.s3.us-east-2.amazonaws.com/MonthlySales.csv"
STATS: List[str] = ["sum", "mean", "max"]
TMP: Path = Path(os.getenv("TMP", "/tmp")) / "MonthlySales.csv"


def get_data(url: str) -> Dict[str, str]:
    """Get data from Github

    Args:
        url (str): The URL where the data is located.

    Returns:
        Dict[str, str]: The dictionary extracted from the data
    """
    if TMP.exists():
        data = json.loads(TMP.read_text())
    else:
        response = requests.get(url)
        response.raise_for_status()
        data = json.loads(response.text)
        with TMP.open("w") as tmp:
            json.dump(data, tmp)
    return data


def process_data(url: str) -> pd.DataFrame:
    """Process the data from the Github API

    Args:
        url (str): The URL where the data is located.

    Returns:
        pd.DataFrame: Pandas DataFrame generated from the processed data
    """
    data = get_data(url)
    #print(data["download_url"])
    ms = os.path.join(os.getenv("TMP", "/tmp"), 'ms_git.csv')
    urlretrieve(data["download_url"], ms)
    df = pd.read_csv(ms)
    ########
    """
    print("\n")
    df['month'] = pd.to_datetime(df['month'])
    df['year'] = pd.DatetimeIndex(df['month']).year
    df['month'] = pd.DatetimeIndex(df['month']).month
    aa = df[df.year == 2013]
    aa = aa.drop(columns = 'year')
    aa = df.groupby(['month'])['sales'].agg('sum')
    #print(aa)
    year_list = set(df['year'].tolist())
    print(year_list)
    #print(aa.columns)
    """
    #print(df)
    return df
    

def summary_report(df: pd.DataFrame, stats: Union[List[str], None] = STATS) -> None:
    """Summary report generated from the DataFrame and list of stats

    Will aggregate statistics for sum, mean, and max by default.

    Args:
        df (pd.DataFrame): Pandas DataFrame of the Github API data
        stats (List[str], optional): List of summaries to aggregate. Defaults to STATS.

    Returns:
        None (prints to standard output)

        Example:
                    sum          mean        max
        year
        2013  484247.51  40353.959167   81777.35
        2014  470532.51  39211.042500   75972.56
        2015  608473.83  50706.152500   97237.42
        2016  733947.03  61162.252500  118447.83
    """
    df['month'] = pd.to_datetime(df['month'])
    df['year'] = pd.DatetimeIndex(df['month']).year
    print(df.groupby('year')['sales'].agg(stats))
    #return df.groupby('year').agg(stats)
    


def yearly_report(df: pd.DataFrame, year: int) -> None:
    """Generate a sales report for the given year

    Args:
        df (pd.DataFrame): Pandas DataFrame of the Github API data
        year (int): The year to generate the report for

    Raises:
        ValueError: Error raised if the year requested is not in the data.
        Should be in the form of "The year YEAR is not included in the report!"

    Returns:
        None (prints to standard output)

        Example:
        2013
                  sales
        month
        1      14236.90
        2       4519.89
        3      55691.01
        4      28295.35
        5      23648.29
        6      34595.13
        7      33946.39
        8      27909.47
        9      81777.35
        10     31453.39
        11     78628.72
        12     69545.62
    """
    
    df['month'] = pd.to_datetime(df['month'])
    df['year'] = pd.DatetimeIndex(df['month']).year
    df['month'] = pd.DatetimeIndex(df['month']).month
    year_set = set(df['year'].tolist())
    if year not in year_set:
        raise ValueError(f"The year {year} is not included in the report!")
    aa = df[df.year == year]
    aa = aa.drop(columns = 'year')
    aa = aa.groupby(['month']).agg('sum')
    print(year)
    print('sales')
    print(aa)


# uncomment the following for viewing/testing the reports/code
# if __name__ == "__main__":
#     data = process_data(URL)
#     summary_report(data)
#     for year in (data["month"].dt.year).unique():
#         yearly_report(data, year)

#     yearly_report(data, 2020)
