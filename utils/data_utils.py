# Data related utility functions.
import pandas as pd
import os


# Define a function to read a data file into a pandas DataFrame based on its extension
def read_data_file(file_path, **kwargs):
    """
    Read a data file into a pandas DataFrame based on its extension.

    Parameters:
    - file_path (str): Path to the data file.

    Returns:
    - DataFrame: The data loaded into a pandas DataFrame.
    """

    # Get file extension
    _, file_extension = os.path.splitext(file_path)

    # Read data based on file extension
    if file_extension == ".csv":
        return pd.read_csv(file_path, **kwargs)
    elif file_extension in [".xlsx", ".xls"]:
        return pd.read_excel(file_path, **kwargs)
    elif file_extension == ".tsv":
        return pd.read_csv(file_path, delimiter="\t", **kwargs)
    elif file_extension == ".json":
        return pd.read_json(file_path, **kwargs)
    elif file_extension == ".parquet":
        return pd.read_parquet(file_path, **kwargs)
    elif file_extension == ".feather":
        return pd.read_feather(file_path, **kwargs)
    elif file_extension == ".msgpack":
        return pd.read_msgpack(file_path, **kwargs)
    elif file_extension == ".dta":
        return pd.read_stata(file_path, **kwargs)
    elif file_extension == ".pkl":
        return pd.read_pickle(file_path, **kwargs)
    elif file_extension == ".sas7bdat":
        return pd.read_sas(file_path, **kwargs)
    else:
        raise ValueError(f"Unsupported file extension: {file_extension}.")
