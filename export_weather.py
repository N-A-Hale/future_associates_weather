from types import NoneType
from loading import load_to_dataframe
from cleaning import clean_dataframe
from aggregations import most_weather_text, average_temperature

import pandas as pd

def export_to_csv(df, filename):
    """Exports dataframe to results directory as CSV, with name = "filename".csv"""
    df.to_csv(r"results/" + filename + ".csv")

if __name__ == "__main__":
    try:
        df = load_to_dataframe()
        cleaned_df = clean_dataframe(df)
        weather_text_df = most_weather_text(cleaned_df)
        average_temperature_df = average_temperature(cleaned_df)
        export_to_csv(weather_text_df, "most_weather_text_per_city")
        export_to_csv(average_temperature_df, "average_temperature_per_city")
    except TypeError:
        print("An error occurred. If first time running please empty reference.txt and try again.")
        print("Please make sure that new JSON files added to correct location")
