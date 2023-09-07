import subprocess

def create_environment(env_name):
    """Create a new virtual environment."""
    subprocess.run(["python", "-m", "venv", env_name])

def install_packages(env_name="zengriddataenv", packages=[]):
    """Install packages into the specified virtual environment."""
    for package in packages:
        subprocess.run([f"{env_name}/bin/pip", "install", package])
        
if __name__ == "__main__":
    # List of packages to install
    packages_to_install = [
        "pandas", "matplotlib", "seaborn", "openpyxl", "numpy", "sqlalchemy",
        "scikit-learn", "plotly", "statsmodels", "python-dateutil", "joblib",
        "requests", "bokeh", "ipykernel", "jupyter", "jupyterlab", "ipywidgets",
        "python-dotenv"
    ]

    # Create environment
    create_environment()

    # Install packages into the environment
    install_packages(packages=packages_to_install)
