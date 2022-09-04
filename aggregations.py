import pandas as pd

def most_weather_text(df) -> pd.DataFrame:
    """Returns a DataFrame of the top 3 WeatherText for each city"""

    # Initialize WeatherText DataFrame
    weather_df = pd.DataFrame(columns=["city", "WeatherText", "occurences"])

    # Loop through each unique city in the dataframe
    for city in df['city'].unique():

        # Store list of WeatherText's to weather_text variable in descending order of number of occurences
        weather_text = df[df['city'] == city].groupby("WeatherText").size().sort_values(ascending = False).index.values

        # Store list of the number of occurences of all WeatherText's in descending order
        occurences = df[df['city'] == city].groupby("WeatherText").size().sort_values(ascending = False).values

        # Finds index position of 3rd most common weather_text
        for i in range(len(occurences)):
            try:
                if occurences[i] == occurences[2]:
                    index = i
            except IndexError:
                continue

        # Adds row to weather_dataframe
        try:
            for i in range(index + 1):
                weather_df.loc[len(weather_df.index)] = [city, weather_text[i], occurences[i]]
        except IndexError:
            continue

    # Set city to index of weather_df
    weather_df = weather_df.set_index('city')

    return weather_df


def average_temperature(df) -> pd.DataFrame:
    """Returns dataframe of mean temperature for each city"""
    # Initialize temperature dataframe
    temperature_df = pd.DataFrame(columns= ["city", "temperature_celsius"])

    # Store cities and mean temperatures in lists
    city = df.groupby('city')["Temperature"].mean().index.values
    temperature = df.groupby('city')["Temperature"].mean().values

    # Loop through cities and temperatures, and add to temperature_df
    for index, (city, temperature) in enumerate(zip(city, temperature)):
        temperature_df.loc[index] = [city, temperature]

    temperature_df = temperature_df.set_index('city')

    return temperature_df

