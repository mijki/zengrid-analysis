# ZenGridAnalyser

ZenGridAnalyser is a comprehensive data analysis tool tailored for assessing energy consumption patterns from various meters. Whether you're looking at data from solar panels, electric car chargers, or regular electricity meters, ZenGridAnalyser ensures you get a clear picture of your energy usage. Powered by Python and an array of data science libraries, it delivers intuitive visualizations and insights.

## 🌟 Features

- **Granular Analysis**: Dive deep with annual, monthly, and daily breakdowns of energy consumption.
- **Intra-day Consumption Insights**: Understand consumption behaviors with detailed hourly analyses.
- **Solar Impact**: Measure the efficacy of solar panels by analyzing their contribution to net consumption.
- **Peak Consumption Detection**: Instantly spot when and why your energy consumption is at its highest.

## 🚀 Quick Start

1. **Setup Virtual Environment**:

    Create and navigate to the desired directory for your virtual environment:

    ```bash
    mkdir .venv-zenalysis
    cd .venv-zenalysis
    ```

    Initialize the virtual environment:

    ```bash
    python -m venv .
    ```

    Activate the virtual environment:

    - On Linux/Mac:
        ```bash
        source .venv-zenalysis/bin/activate
        ```

    - On Windows (Command Prompt):
        ```bash
        .venv-zenalysis\Scripts\activate.bat
        ```

    - On Windows (PowerShell):
        ```powershell
        .\.venv-zenalysis\Scripts\Activate
        ```

2. **Install Dependencies**:

   Navigate back to your project's root directory and install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Jupyter Notebook**:

    From the project root:

    ```bash
    jupyter notebook notebooks/cons-analysis-dyn.ipynb
    ```

## 🧹 Data Preprocessing

ZenGridAnalyser ensures the integrity of your data, making it analysis-ready. Key preprocessing steps include:
- Efficient outlier removal.
- Smart handling of missing data.
- Extraction of pivotal features like Hour, Minute, Day of the Week, and Month.

## 📊 Visualizations

With ZenGridAnalyser, you gain access to:
- Detailed monthly consumption charts for every 15-minute slot.
- Visual representations showcasing the impact of solar panels on net consumption.
- Averages and patterns of consumption throughout the week.

## 🤝 Contributions

Contributions are heartily welcomed! If you'd like to enhance ZenGridAnalyser, feel free to fork the project and submit your pull requests. Whether it's a bug fix, a new feature, or just some general improvements, we appreciate all the help.
