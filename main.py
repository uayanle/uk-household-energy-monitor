import pandas as pd
from calculations import calculate_annual_cost
from calculations import calculate_daily_cost
from calculations import calculate_emissions
from calculations import calculate_energy
from calculations import calculate_monthly_cost

from file_handler import load_carbon_factor
from file_handler import load_tariff

print("=" * 50)
print("      UK Household Energy Monitor")
print("=" * 50)  # this is so user can see something more proffesionally


results = []


# loading the data from file handler

price_per_kwh = load_tariff()
carbon_factor = load_carbon_factor()

while True:
    # asking for the users input
    appliance = input('Enter appliances (or press Enter to finish): ')
    if appliance == '':
        break
    power_watts = float(input('Enter power (Watts): '))
    hours_used = float(input('Enter hours used per day: '))

    # calculating daily energy
    daily_energy = calculate_energy(power_watts, hours_used)
    print(f'The energy (kWh): {daily_energy:.2f}')

    # calculating daily cost
    daily_cost = calculate_daily_cost(daily_energy, price_per_kwh)
    print(f'Daily cost (£): {daily_cost:.2f}')

    # calculating monthly cost
    monthly_cost = calculate_monthly_cost(daily_cost)
    print(f'Monthly cost (£): {monthly_cost:.2f}')

    # calculating annual cost
    annual_cost = calculate_annual_cost(daily_cost)
    print(f'Annual cost (£): {annual_cost:.2f}')

    # calculate emissions
    annual_energy = calculate_energy(power_watts, hours_used * 365)
    emissions = calculate_emissions(annual_energy, carbon_factor)
    print(f'Emissions: {emissions:.2f}')


# storing each appliance

    appliance_data = {
        'Appliance': appliance,
        'Power (W)': power_watts,
        'Hours used': hours_used,
        'Daily energy (kWh)': daily_energy,
        'Daily cost (£)': daily_cost,
        'Monthly cost (£)': monthly_cost,
        'Annual cost (£)': annual_cost,
        'Annual emissions': emissions
    }

    results.append(appliance_data)  # putting the dictionary into results list


# empty data frame output and storing results
if not results:
    print('No appliance was entered')
else:
    df = pd.DataFrame(results)
    print("Summary of appliances")
    print(df)
    df.to_csv("outputs/results.csv", index=False)

# total cost
total_daily_cost = df['Daily cost (£)'].sum()
total_annual_cost = df['Annual cost (£)'].sum()
total_emissions = df['Annual emissions'].sum()

print('Household total')
print(f'Total daily cost: £{total_daily_cost:.2f}')
print(f'Total annual cost: £{total_annual_cost:.2f}')
print(f'Total annual emissions: {total_emissions:.2f}')
