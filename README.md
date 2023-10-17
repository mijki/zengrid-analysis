# ZenGridAnalyser

ZenGridAnalyser is a comprehensive data analysis tool tailored for assessing energy consumption patterns from various meters. Whether you're looking at data from solar panels, electric car chargers, or regular electricity meters, ZenGridAnalyser ensures you get a clear picture of your energy usage. Powered by Python and an array of data science libraries, it delivers intuitive visualizations and insights.

## 🌟 Features

- **Granular Analysis**: Dive deep with annual, monthly, and daily breakdowns of energy consumption.
- **Intra-day Consumption Insights**: Understand consumption behaviors with detailed hourly analyses.
- **Solar Impact**: Measure the efficacy of solar panels by analyzing their contribution to net consumption.
- **Peak Consumption Detection**: Instantly spot when and why your energy consumption is at its highest.

## 🚀 Quick Start with Poetry for Cloned Project

### 1. Clone the Repository

The repository can be cloned using the following command:

```bash
git clone https://github.com/mijki/zengrid-analysis.git
```

Then get into the project directory:

```bash
cd zengrid-analysis
```

### 2. Install Poetry

If not already installed, get [Poetry](https://python-poetry.org/docs/#installation) for your system. For example, on Linux or macOS:

```bash
curl -sSL https://install.python-poetry.org | python -
```

Or on Windows:

```bash
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```

If you have ***pip*** installed you can use:
```bash
pip install poetry
```

### 3. Install Dependencies

With poetry installed, you can install the dependencies for the project using the following command:

```bash
poetry install
```

This will read the **pyproject.toml** and poetry.lock files, set up a virtual environment, and install all necessary packages into it.

### 4. Activate the Virtual Environment

Poetry automatically creates a virtual environment for the project. To activate it, run the following command:

```bash
poetry shell
```

### 5. Setting up .env file

The .env file stores the environment variables for the notebook. Every different notebook has its own .env file in the root folder. The .env file for the notebook is named as **.env.notebook_name**. For example, the .env file for the notebook **cons-analysis-dyn.ipynb** is named as **.env.cons-analysis-dyn**.

### 6. **Run the Jupyter Notebook**

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
