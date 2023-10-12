# Data related utility functions.

# -----------------------
# IMPORTS
# -----------------------
import pandas as pd
import os
import datetime as dt
import csv

# -----------------------
# ENVIRONMENT UTILITIES
# -----------------------


# Reads data from .env file
def load_dotenv():
    """
    Reads data from .env file

    Returns:
    - dict: A dictionary containing the data from the .env file.
    """
    dotenv_path = os.path.join(os.getcwd(), ".env")
    dotenv_dict = {}

    with open(dotenv_path, "r") as dotenv_file:
        for line in dotenv_file:
            line = line.strip()

            if line.startswith("#") or not line:
                continue

            key, value = line.split("=", 1)
            dotenv_dict[key] = value

    return dotenv_dict


# -----------------------
# DATA READING UTILITIES
# -----------------------


# Define the mapping between file extensions and their respective pandas read functions
def read_data_file(file_path, **kwargs):
    """
    Read a data file into a pandas DataFrame based on its extension.

    Parameters:
    - file_path (str): Path to the data file.

    Returns:
    - DataFrame: The data loaded into a pandas DataFrame.
    """

    extension_read_function_mapping = {
        ## Modified the CSV because of the EON-specific format
        ".csv": read_csv_auto_delimiter,
        ".xlsx": pd.read_excel,
        ".xls": pd.read_excel,
        ".tsv": lambda x, **y: pd.read_csv(x, delimiter="\t", **y),
        ".json": pd.read_json,
        ".parquet": pd.read_parquet,
        ".feather": pd.read_feather,
        ".dta": pd.read_stata,
        ".pkl": pd.read_pickle,
        ".sas7bdat": pd.read_sas,
    }

    _, file_extension = os.path.splitext(file_path)

    read_function = extension_read_function_mapping.get(file_extension)

    if read_function is None:
        raise ValueError(f"Unsupported file extension: {file_extension}.")

    # Remove the sep argument if it exists, as it's handled internally for CSVs
    kwargs.pop("sep", None)
    return read_function(file_path, **kwargs)


# Automatically determines the delimiter for CSV files
def read_csv_auto_delimiter(filepath, **kwargs):
    with open(filepath, "r", encoding="utf-8", errors="ignore") as file:
        first_line = file.readline()
        if ";" in first_line:
            delimiter = ";"
        else:
            delimiter = ","
        return pd.read_csv(filepath, sep=delimiter, **kwargs)


# -----------------------
# DATA TRANSFORMATION UTILITIES
# -----------------------


# Reshapes the DataFrame to the desired format
def eon_dataframe(df):
    # Filter rows where "Mertekegys" column is "kWh"
    df_filtered = df[df["Mertekegys"] == "kWh"]

    # Drop columns "SXX", "OBIS", and "Szorzo"
    columns_to_drop = [
        col
        for col in df_filtered.columns
        if col.startswith("S") or col in ["OBIS", "Szorzo", "Mertekegys"]
    ]
    df_filtered = df_filtered.drop(columns=columns_to_drop)

    # Convert "Datum" column to datetime format
    df_filtered["Datum"] = pd.to_datetime(df_filtered["Datum"])

    # Melt the dataframe
    melted_df = df_filtered.melt(
        id_vars=["MP", "Datum"],
        value_vars=[
            col
            for col in df_filtered.columns
            if col.startswith("A")
            and len(col) >= 4
            and col[1:3].isdigit()
            and col[3:].isdigit()
            and int(col[1:3]) <= 23
            and int(col[3:]) < 4
        ],
        var_name="Time_Slice",
        value_name="Value",
    )

    print(melted_df.head())
    print(melted_df.columns)

    # Convert 'A00', 'A01', etc. to actual time intervals
    def get_time_interval(row):
        slice_name = row["Time_Slice"]
        date = row["Datum"]
        hour = int(slice_name[1:3])
        minute = 15 * (int(slice_name[3:]) if slice_name[3:] else 0)
        start_time = date.replace(
            hour=hour, minute=minute, second=0, microsecond=0
        ).strftime("%H:%M")
        end_time = (
            (date + pd.Timedelta(minutes=15))
            .replace(hour=hour, minute=minute, second=0, microsecond=0)
            .strftime("%H:%M")
        )
        return start_time + " - " + end_time

    melted_df["Időszeletek"] = melted_df.apply(get_time_interval, axis=1)

    # Drop "Datum" and "Time_Slice" columns as they are no longer needed
    melted_df = melted_df.drop(columns=["Datum", "Time_Slice"])

    reshaped_df = melted_df.pivot_table(
        index="Időszeletek", columns="MP", values="Value", aggfunc="sum"
    ).reset_index()

    # Sorting the Időszeletek column to maintain chronological order
    reshaped_df = reshaped_df.sort_values(by="Időszeletek").reset_index(drop=True)

    return reshaped_df


# Load and preprocess the data based on file type
def load_and_preprocess_data(SOURCE_FILE_PATH):
    # Task1: Load the data using the defined function based on file type
    if SOURCE_FILE_PATH.endswith(".csv"):
        data = read_data_file(SOURCE_FILE_PATH, skiprows=[1])
    else:
        data = read_data_file(SOURCE_FILE_PATH, skiprows=[1])

    # Task 2: Preprocessing
    # Check the file extension
    if SOURCE_FILE_PATH.endswith(".csv"):
        processed_data = eon_dataframe(data)
    else:
        processed_data = data.copy()

    return processed_data
