# Future Associates Program - Take Home Test

## What is it?
Here is a sample data pipeline that takes JSON files and transforms them into a single DataFrame. Aggregations are performed on the DataFrame to find:
- The average temperature for each city, and:
- The top three most common "weather text" for each city.
The results are stored as CSV files in the "Results" folder.

## Features
### Data Loading - **loading.py**
Script which takes in JSON files (from **raw_data** folder) and loads to a DataFrame.
- Uses **reference.txt** to ensure files are not loaded twice.
- Saves unprocessed **raw_weather_dataframe** as CSV (in **raw_data/raw_dataframe** folder) for addition of future data.

NB: **Assumption here that all future data will be loaded to raw_data folder and is of the same schema as files provided**

### Data Cleaning - **cleaning.py**
Takes unprocessed dataframe and cleans for future use.
- **get_temperature()** - Flattens **Temperature** object and extracts temperature in celsius (as Float64).
- **missing_values()** - Converts all missing values to NaN. For **PrecipitationType** missing and None values become "n/a".
- **drop_columns()** - Removes **WeatherIcon** column as there were discrepancies between this and **WeatherText**. Removes rows if **city** is missing. Removes row if **LocalObservationDateTime** AND **EpochTime** are missing.
- **clean_text()** - Makes all text lowercase and removes whitespace from beginning and end of strings
- **drop_duplicates()** - Removes duplicate rows.
- **clean_dataframe()** - Contains above functions in order of proper use.

### Performing aggregations - **aggregations.py**
Performs key tasks issued in take-home test
- **most_weather_text()** - Creates new DataFrame that contains the top 3 most common "Weather Text" for each city.
- **average_temperature()** - Creates new DataFrame that contains the average temperature for each city.

### Exporting results as CSV - **export_weather.py**
- **export_to_csv()** - Exports a DataFrame as CSV to **results** folder.

NB: This is the executor script.

## How to run
- Pull repo from GitHub.
- Open Command Prompt and go to *future_associates_weather* directory.
- Enter **python3 export_weather.py** and press *enter*.
- If new data has been added, will updated the *result* CSV files.

NB: Python3.10 and Pandas need to be installed. Due to recent reformatting and loss of Windows Subsytem for Linux 2, this has all been scripted in Windows, because of this and time restraints, I have not packaged this. In future I will create a package that can be installed and run on Windows, OS X or Linux.
