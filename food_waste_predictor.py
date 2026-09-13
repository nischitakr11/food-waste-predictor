"""
Food Waste Predictor - V1

A simple Python program that analyzes food waste
based on the amount of food prepared and consumed.
"""


def calculate_waste(prepared, consumed):
    """Calculate the amount of food wasted."""
    return prepared - consumed


def calculate_waste_percentage(waste, prepared):
    """Calculate the percentage of food wasted."""
    return (waste / prepared) * 100


def get_waste_level(waste_percentage):
    """Classify the waste level."""
    if waste_percentage >= 30:
        return "HIGH"
    elif waste_percentage >= 15:
        return "MODERATE"
    else:
        return "LOW"


def get_recommendation(waste_percentage):
    """Give a basic recommendation based on waste percentage."""
    if waste_percentage >= 30:
        return "Reduce the amount of food prepared and review demand patterns."
    elif waste_percentage >= 15:
        return "Monitor demand and consider preparing slightly less food."
    else:
        return "Food usage is efficient. Continue monitoring waste."


def display_report(prepared, consumed, waste, waste_percentage, level, recommendation):
    """Display the final food waste report."""
    print("\n========== FOOD WASTE REPORT ==========")
    print(f"Food Prepared     : {prepared:.2f} units")
    print(f"Food Consumed     : {consumed:.2f} units")
    print(f"Food Wasted       : {waste:.2f} units")
    print(f"Waste Percentage  : {waste_percentage:.2f}%")
    print(f"Waste Level       : {level}")
    print(f"Recommendation    : {recommendation}")
    print("Status            : Analysis completed successfully.")
    print("========================================")


def main():
    """Run the Food Waste Predictor."""
    print("========== FOOD WASTE PREDICTOR ==========")

    try:
        prepared = float(input("Enter amount of food prepared: "))
        consumed = float(input("Enter amount of food consumed: "))
    except ValueError:
        print("Error: Please enter valid numbers.")
        return

    if prepared <= 0:
        print("Error: Food prepared must be greater than 0.")
        return

    if consumed < 0:
        print("Error: Food consumed cannot be negative.")
        return

    if consumed > prepared:
        print("Error: Food consumed cannot be greater than food prepared.")
        return

    waste = calculate_waste(prepared, consumed)
    waste_percentage = calculate_waste_percentage(waste, prepared)
    level = get_waste_level(waste_percentage)
    recommendation = get_recommendation(waste_percentage)

    display_report(
        prepared,
        consumed,
        waste,
        waste_percentage,
        level,
        recommendation
    )


if __name__ == "__main__":
    main()