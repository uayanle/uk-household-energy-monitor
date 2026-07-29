import pandas as pd


def load_carbon_factor():
    """Load the carbon factor from the CSV file and return the kg CO₂ per kWh."""

    carbon_df = pd.read_csv('data/carbon_factors.csv')

    carbon_factor = carbon_df.loc[0, 'kgCO2_per_kWh']
    return carbon_factor


def load_tariff():
    """Load the electricity tariff from the csv file then return the price per kwh"""

    tariffs_df = pd.read_csv('data/tariffs.csv')
    price = tariffs_df.loc[0, 'Price_per_kWh']  # extracts the value

    return price
