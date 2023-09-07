# ZenGridAnalyser

ZenGridAnalyser is a robust data analysis tool designed to evaluate and visualize energy consumption patterns from various meters, including solar panels and electric car chargers. Utilizing the power of Python and its data science libraries, this tool provides insightful visualizations that help in understanding consumption behaviors, the impact of solar panels on net consumption, and more.

## Features

- **Comprehensive Analysis**: Provides annual and monthly breakdowns of energy consumption.
- **Intra-day Consumption Distribution**: Get insights into consumption behaviors at different times of the day.
- **Solar Impact Analysis**: Understand how solar panels are reducing your net consumption.
- **Peak Consumption Highlight**: Easily identify when your energy consumption hits its peak.

## Quick Start

1. **Setup Virtual Environment**:

    Create the virtual environment:

    ```bash
    python -m venv zengriddataenv
    ```

    Activate the virtual environment:

    - On Linux/Mac:
        ```bash
        source zengriddataenv/bin/activate
        ```

    - On Windows (Command Prompt):
        ```bash
        zengriddataenv\Scripts\activate.bat
        ```

    - On Windows (PowerShell):
        ```powershell
        .\zengriddataenv\Scripts\Activate
        ```

2. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Jupyter Notebook**:
    ```bash
    jupyter notebook cons-analysis-dyn.ipynb
    ```

## Data Preprocessing

ZenGridAnalyser ensures that your data is clean and ready for analysis. The preprocessing steps include:
- Removing outliers.
- Handling missing data.
- Extracting essential features like Hour, Minute, Day of the Week, and Month.

## Visualizations

The tool offers various visualizations, including:
- Monthly breakdowns of consumption for every 15-minute interval.
- Impact of solar panels on net consumption.
- Average consumption patterns throughout the week.

## Contributions

Feel free to fork this project and submit pull requests for any enhancements, bug fixes, or features you think would benefit ZenGridAnalyser.