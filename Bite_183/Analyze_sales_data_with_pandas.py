import os
from urllib.request import urlretrieve

import pandas as pd

TMP = os.getenv("TMP", "/tmp")
EXCEL = os.path.join(TMP, 'order_data.xlsx')
if not os.path.isfile(EXCEL):
    urlretrieve(
        'https://bites-data.s3.us-east-2.amazonaws.com/order_data.xlsx',
        EXCEL
    )


def load_excel_into_dataframe(excel=EXCEL):
    """Load the SalesOrders sheet of the excel book (EXCEL variable)
       into a Pandas DataFrame and return it to the caller"""
    df = pd.read_excel(excel, "SalesOrders")
    print("\n")
    print(df)
    return df


def get_year_region_breakdown(df):
    """Group the DataFrame by year and region, summing the Total
       column. You probably need to make an extra column for
       year, return the new df as shown in the Bite description"""
    df["Year"] = df["OrderDate"].dt.year
    df_year_region = df.groupby(["Year", "Region"])["Total"].sum()
    return df_year_region


def get_best_sales_rep(df):
    """Return a tuple of the name of the sales rep and
       the total of his/her sales"""
    df_best_sales = df.groupby("Rep", as_index=False)["Total"].sum().sort_values("Total", ascending=False)
    result = (df_best_sales.iat[0, 0], df_best_sales.iat[0, 1])
    return result


def get_most_sold_item(df):
    """Return a tuple of the name of the most sold item
       and the number of units sold"""
    df_ms = df.groupby("Item", as_index=False)["Units"].sum().sort_values("Units", ascending=False)
    result = (df_ms.iat[0, 0], df_ms.iat[0, 1])
    return result
