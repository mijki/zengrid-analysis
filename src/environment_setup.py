import os


# Create a .env file for the notebook "cons-analysis-dyn.ipynb"
def create_dotenv_file_cons_analysis(
    force_create, solar_panel_suffix, electric_car_charger_suffix, battery_suffix, source_file_path, price_per_kwh, threshold_for_outliers
):
    # Get the current working directory
    current_directory = os.getcwd()

    # Construct the full path to the .env file
    env_path = os.path.join(current_directory, ".env")

    # Check if the .env file already exists and if it should be overwritten
    # Check if the .env file already exists
    if not os.path.exists(env_path) or force_create:
        with open(env_path, "w") as env_file:
            env_file.write(f"source_file_path={source_file_path}\n")
            env_file.write(f"price_per_kwh={price_per_kwh}\n")
            env_file.write(f"threshold_for_outliers={threshold_for_outliers}\n")
            env_file.write(f"solar_panel_suffix={solar_panel_suffix}\n")
            env_file.write(f"electric_car_charger_suffix={electric_car_charger_suffix}\n")
            env_file.write(f"battery_suffix={battery_suffix}\n")