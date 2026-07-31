import matplotlib.pyplot as plt

# bar chart


def annual_cost_chart(df):
    """Create a bar chart that shows annual cost for each appliance."""

    plt.figure(figsize=(8, 5))
    plt.bar(
        df['Appliance'],
        df['Annual cost (£)']
    )

    plt.title('Annual cost by appliance')
    plt.xlabel('Appliance')
    plt.ylabel('Annual cost (£)')
    plt.xticks(rotation=45)             # makes it easier to read
    plt.tight_layout()                  # stops labels getting cut off
    plt.savefig("outputs/graphs/annual_cost.png")

    plt.close()


# pie chart

def daily_energy_chart(df):
    """Create a pie chart that shows the daily energy usage for each appliance."""

    plt.figure(figsize=(8, 8))
    plt.pie(
        df['Daily energy (kWh)'],
        labels=df['Appliance'],
        autopct="%1.1f%%"
    )

    plt.title("Daily energy usage per appliance (kWh)")
    plt.axis("equal")
    plt.tight_layout()
    plt.savefig("outputs/graphs/daily_energy_cost.png")

    plt.close()
