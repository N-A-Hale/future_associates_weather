from webbrowser import get
import pandas as pd
import numpy as np

def get_temperature(df) -> pd.DataFrame:
    """Extracts the temperature in degrees C"""

    df["Temperature"] = pd.json_normalize(df["Temperature"])["Metric.Value"]

    return df


def missing_values(df) -> pd.DataFrame:
    """Converts PrecipitationType to "n/a" if missing or None. Converts all other missing values to nan values"""

    df["PrecipitationType"] = df["PrecipitationType"].fillna("n/a")

    df.replace("", np.nan, inplace = True)

    return df

def drop_columns(df) -> pd.DataFrame:
    """Drops unnecessary columns from dataframe, and any without time or city"""

    # Drop WeatherIcon column as does not always match WeatherText column
    df = df.drop(columns=["WeatherIcon"])

    # Drop row if LocalObservationDateTime AND EpochTime missing
    df = df.dropna(how = "all", subset = ["LocalObservationDateTime", "EpochTime"])

    # Drop row if city is missing
    df = df.dropna(subset = ["city"])

    return df


def clean_text(df) -> pd.DataFrame:
    """Makes text lowercase and removes whitespace"""

    for column in df.columns:
        try:
            df[column] = df[column].str.strip()
            df[column] = df[column].str.lower()
        except AttributeError:
            continue

    return df


def drop_duplicates(df) -> pd.DataFrame:
    """Removes duplicate rows from dataframe"""

    df = df.drop_duplicates()

    return df


def clean_dataframe(df) -> pd.DataFrame:

    try:
        df = get_temperature(df)
    except: 
        print("There was a problem getting the temperature, please review raw dataframe")
    try:
        df = missing_values(df)
    except:
        print("There was a problem converting missing values to nan, please review raw dataframe")
    try:
        df = drop_columns(df)
    except:
        print("There was a problem dropping columns, please review raw dataframe")
    try:
        df = clean_text(df)
    except:
        print("There was a problem cleaning the text, please review raw dataframe")
    try:
        df = drop_duplicates(df)
        return df
    except:
        print("There was a problem dropping duplicate rows, please review raw dataframe")

