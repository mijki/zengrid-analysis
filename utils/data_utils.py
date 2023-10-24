# Data related utility functions.

# -----------------------
# IMPORTS
# -----------------------
import pandas as pd
import os
import datetime
import csv
from IPython.display import display

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
# JUPYTER DATAFRAME RELATED UTILITIES
# -----------------------


# Display basic information about a dataframe
def inspect_dataframe(df, n_rows=5):
    """
    Display basic information about a dataframe.

    Parameters:
    - df (pd.DataFrame): DataFrame to inspect.
    - n_rows (int, optional): Number of rows to display from the dataframe's head. Default is 5.
    """
    print("Head of DataFrame:")
    display(df.head(n_rows))  # Using display for a prettier output in Jupyter
    
    print("\nColumns in DataFrame:")
    print(df.columns)
    
    print("\nData Types in DataFrame:")
    print(df.dtypes)
    
    print("\nNumber of Missing Values in DataFrame:")
    print(df.isnull().sum())
    
    print("\nStatistical Summary of DataFrame:")
    display(df.describe())  # Using display for a prettier output in Jupyter
    
    print("\nConcise Summary of DataFrame:")
    df.info()


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
# DATA WRITING UTILITIES
# -----------------------
# Export a DataFrame to an Excel file
def export_dataframe_to_excel(df, df_name, export_file_path, custom_file_name=None):
    """
    Exports a DataFrame to an Excel file.

    Parameters:
    - df (pd.DataFrame): DataFrame to export.
    - df_name (str): Name of the DataFrame (used in default file naming).
    - custom_file_name (str, optional): Custom file name for the Excel file. If not provided, a default name is generated.

    Returns:
    - str: The path of the exported Excel file.
    """
    # Check if the directory exists, if not, create it
    if not os.path.exists(export_file_path):
        os.makedirs(export_file_path)

    if custom_file_name:
        file_name = custom_file_name
    else:
        current_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        file_name = f"{df_name}_{current_time}.xlsx"

    file_path = os.path.join(export_file_path, file_name)

    df.to_excel(file_path, index=False)

    print(f"DataFrame exported to: {file_path}")
    return file_path


# -----------------------
# DATA TRANSFORMATION UTILITIES
# -----------------------


# Reshapes the DataFrame to the desired format
def eon_dataframe(df):
    # Embedded function to generate time intervals
    def generate_time_intervals():
        """Generate a list of 15-minute intervals for 24 hours."""
        start_time = datetime.datetime.strptime("00:00", "%H:%M")
        intervals = []
        for _ in range(96):  # 96 intervals in a day
            end_time = start_time + datetime.timedelta(minutes=15)
            interval = f"{start_time.strftime('%H:%M')} - {end_time.strftime('%H:%M')}"
            intervals.append(interval)
            start_time = end_time
        return intervals

    # Filter on kWh in "Mertekegys" column
    df_filtered = df[df["Mertekegys"] == "kWh"]

    # Drop columns "SXX", "OBIS", and "Szorzo"
    columns_to_drop = [
        col
        for col in df.columns
        if col.startswith("S") or col in ["OBIS", "Szorzo", "Mertekegys"]
    ]
    df_filtered = df_filtered.drop(
        columns=columns_to_drop, errors="ignore"
    )  # Use errors='ignore' to handle non-existent columns

    # Transformation logic
    result_data = []

    # Define the column indices for Datum, MP, and AXX columns
    datum_col_idx = 0
    mp_col_idx = 1
    a_col_start_idx = 2  # Adjusted index due to dropped columns

    for _, row in df_filtered.iterrows():
        # Modify the date format to "YYYY.MM.DD"
        date_str = datetime.datetime.fromisoformat(
            row[datum_col_idx].split("T")[0]
        ).strftime("%Y.%m.%d")
        for i, interval in enumerate(generate_time_intervals()):
            a_col_idx = a_col_start_idx + i  # Indexing directly into AXX columns
            result_data.append(
                {"Datum": f"{date_str} {interval}", row[mp_col_idx]: row[a_col_idx]}
            )

    # Convert the list of dictionaries to a DataFrame
    result_df = pd.DataFrame(result_data)

    # Reorder columns
    result_df = result_df[
        ["Datum"] + [col for col in result_df.columns if col != "Datum"]
    ]

    # Rename 'Datum' to 'Időszeletek'
    result_df = result_df.rename(columns={"Datum": "Időszeletek"})

    # Display the first few rows
    print(result_df.head(15))

    return result_df


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
