# Data related utility functions.
import pandas as pd
import os


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


# Read a data file into a pandas DataFrame based on its extension.
def read_data_file(file_path, **kwargs):
    """
    Read a data file into a pandas DataFrame based on its extension.

    Parameters:
    - file_path (str): Path to the data file.

    Returns:
    - DataFrame: The data loaded into a pandas DataFrame.
    """

    extension_read_function_mapping = {
        ".csv": pd.read_csv,
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

    return read_function(file_path, **kwargs)
