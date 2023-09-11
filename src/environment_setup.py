import os
import subprocess


# Create a .env file for the notebook "cons-analysis-dyn.ipynb"
def create_dotenv_file_cons_analysis(
    notebook_name, source_file_path, price_per_kwh, threshold_for_outliers
):
    # Construct the name of the .env file based on the notebook name
    env_filename = f".env_{notebook_name}"

    # Get the current working directory
    current_directory = os.getcwd()

    # Construct the full path to the .env file
    env_path = os.path.join(current_directory, env_filename)

    with open(env_path, "w") as env_file:
        # Write source_file_path to .env
        env_file.write(f"source_file_path={source_file_path}\n")

        # Write price_per_kwh to .env
        env_file.write(f"price_per_kwh={price_per_kwh}\n")

        # Write threshold_for_outliers to .env
        env_file.write(f"threshold_for_outliers={threshold_for_outliers}\n")

    return env_filename
