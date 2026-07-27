

def calculate_energy(power_watts, hours_used):
    power_kw = power_watts / 1000
    energy_kwh = power_kw * hours_used

    return energy_kwh


def calculate_daily_cost(energy_kwh, price_per_kwh):
    return energy_kwh * price_per_kwh


def calculate_monthly_cost(daily_Cost):
    return daily_Cost * 30


def calculate_annual_cost(daily_cost):
    return daily_cost * 365


def calculate_emissions(annual_energy_kwh, carbon_factor):
    return annual_energy_kwh * carbon_factor
