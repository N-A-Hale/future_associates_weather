from glob import glob
import os
import pandas as pd

# Path to JSON files, assuming new files are added to this directory
path_to_files = "raw_data"

# Initialize list to store individual dataframes
city_dataframes = []

# Adds used files to reference text
def add_to_reference(file):
    """Adds name of file to reference.txt document for future reference"""
    with open("reference.txt", "a") as reference:
        reference.write(file + "\n")


def load_to_dataframe() -> pd.DataFrame:
    """Iterates through JSON files in data directory and returns a raw/uncleaned dataframe"""

    # List of files in raw_data directory
    files = glob(os.path.join(path_to_files, "*.json"))

    # Checks if file has been loaded previously
    with open("reference.txt", "r") as read_reference:
        used_files = read_reference.read()
        for file in files:
            if not file in used_files:
                add_to_reference(file)
                
                # Read/store individual files to own dataframe
                city_dataframes.append(pd.read_json(file))

    # Loads existing raw_whole_dataframe, if exists
    try:    
        raw_whole_dataframe = pd.read_csv(os.path.join(path_to_files, "raw_dataframe", "raw_whole_dataframe.csv"))
    except FileNotFoundError:
        pass

    # Concat dataframes
    try:
        raw_whole_dataframe = pd.concat(city_dataframes)
        raw_whole_dataframe.to_csv(os.path.join(path_to_files, "raw_dataframe", "raw_whole_dataframe.csv"))
        return raw_whole_dataframe
    except: ValueError

    
