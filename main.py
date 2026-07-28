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


# loading the data from file handler

price_per_kwh = load_tariff()
carbon_factor = load_carbon_factor()


# asking for the users input

appliance = input('Enter appliances: ')
power_watts = float(input('Enter power (Watts): '))
hours_used = float(input('Enter hours used per day: '))


# calculating daily energy

daily_energy = calculate_energy(power_watts, hours_used)
print(f'The energy (kWh): {daily_energy}')

# calculating daily cost

daily_cost = calculate_daily_cost(daily_energy, price_per_kwh)
print(f'Daily cost (£): {daily_cost}')

# calculating monthly cost

monthly_cost = calculate_monthly_cost(daily_cost)
print(f'Monthly cost (£): {monthly_cost}')

# calculating annual cost

annual_cost = calculate_annual_cost(daily_cost)
print(f'Annual cost (£): {annual_cost}')

# calculate emissions

annual_energy = calculate_energy(power_watts, hours_used * 365)
emissions = calculate_emissions(annual_energy, carbon_factor)
print(f'Emissions: {emissions}')
