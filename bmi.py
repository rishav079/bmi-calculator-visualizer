"""
============================================================
                 BMI CALCULATOR & VISUALIZER
============================================================

A professional Python application that:
• Collects BMI data for multiple people
• Calculates and classifies BMI
• Displays a formatted BMI report
• Generates a color-coded comparison chart

Author  : Rishav Kaushik
Version : 1.0.0

============================================================
"""

import matplotlib.pyplot as plt
from matplotlib.patches import Patch


# ============================================================
# BMI CATEGORY COLORS
# ============================================================

BMI_COLORS = {
    "Underweight": "#3498db",   # Blue
    "Normal": "#2ecc71",        # Green
    "Overweight": "#f39c12",    # Orange
    "Obese": "#e74c3c"          # Red
}


# ============================================================
# BMI CALCULATION
# ============================================================

def calculate_bmi(weight: float, height: float) -> float:
    """
    Calculate Body Mass Index.

    Formula:
        BMI = Weight / Height²

    Args:
        weight (float): Weight in kilograms
        height (float): Height in meters

    Returns:
        float: BMI rounded to 2 decimal places
    """
    return round(weight / (height ** 2), 2)


# ============================================================
# BMI CATEGORY CLASSIFICATION
# ============================================================

def get_bmi_category(bmi: float) -> str:
    """
    Determine BMI category.

    Args:
        bmi (float): Calculated BMI

    Returns:
        str: BMI category
    """
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


# ============================================================
# USER INPUT SECTION
# ============================================================

def collect_user_data() -> list:
    """
    Collect user information and calculate BMI.

    Returns:
        list: List containing user records
    """

    users = []

    print("\n" + "=" * 60)
    print("            BMI DATA COLLECTION")
    print("=" * 60)

    while True:
        try:
            total_people = int(
                input("\nEnter number of people to Calculate BMI: ")
            )

            if total_people > 0:
                break

            print("Please enter a value greater than zero.")

        except ValueError:
            print("Invalid input! Please enter a number.")

    for person in range(1, total_people + 1):

        print(f"\n---------- Person {person} ----------")

        name = input("Name   : ").strip().title()

        while True:
            try:
                weight = float(input("Weight (kg) : "))
                if weight > 0:
                    break
                print("Weight must be greater than 0.")
            except ValueError:
                print("Enter a valid weight.")

        while True:
            try:
                height = float(input("Height (m) : "))
                if height > 0:
                    break
                print("Height must be greater than 0.")
            except ValueError:
                print("Enter a valid height.")

        bmi = calculate_bmi(weight, height)
        category = get_bmi_category(bmi)

        users.append({
            "name": name,
            "bmi": bmi,
            "category": category
        })

        print("\n✓ Record Saved Successfully")
        print(f"  BMI      : {bmi}")
        print(f"  Category : {category}")

    return users


# ============================================================
# DISPLAY BMI REPORT
# ============================================================

def display_report(users: list) -> None:
    """
    Display formatted BMI report.
    """

    print("\n")
    print("=" * 70)
    print("                         BMI REPORT")
    print("=" * 70)

    print(
        f"{'Name':<25}"
        f"{'BMI':<15}"
        f"{'Category'}"
    )

    print("-" * 70)

    for user in users:
        print(
            f"{user['name']:<25}"
            f"{user['bmi']:<15}"
            f"{user['category']}"
        )

    print("=" * 70)


# ============================================================
# BMI VISUALIZATION
# ============================================================

def show_bar_graph(users: list) -> None:
    """
    Display BMI comparison graph.
    """

    names = [user["name"] for user in users]
    bmis = [user["bmi"] for user in users]
    colors = [BMI_COLORS[user["category"]] for user in users]

    plt.figure(figsize=(12, 7))

    bars = plt.bar(
        names,
        bmis,
        color=colors,
        edgecolor="black",
        linewidth=1.2
    )

    # Display BMI value above bars
    for bar in bars:

        height = bar.get_height()

        plt.text(
            bar.get_x() + bar.get_width() / 2,
            height + 0.3,
            f"{height}",
            ha="center",
            fontsize=10,
            fontweight="bold"
        )

    # BMI Reference Lines
    plt.axhline(
        y=18.5,
        linestyle="--",
        linewidth=1.5,
        alpha=0.7,
        label="Underweight Limit"
    )

    plt.axhline(
        y=25,
        linestyle="--",
        linewidth=1.5,
        alpha=0.7,
        label="Normal Limit"
    )

    plt.axhline(
        y=30,
        linestyle="--",
        linewidth=1.5,
        alpha=0.7,
        label="Obesity Limit"
    )

    # Category Legend
    legend_items = [
        Patch(
            facecolor=BMI_COLORS["Underweight"],
            label="Underweight (<18.5)"
        ),
        Patch(
            facecolor=BMI_COLORS["Normal"],
            label="Normal (18.5 - 24.9)"
        ),
        Patch(
            facecolor=BMI_COLORS["Overweight"],
            label="Overweight (25 - 29.9)"
        ),
        Patch(
            facecolor=BMI_COLORS["Obese"],
            label="Obese (30+)"
        )
    ]

    plt.legend(
        handles=legend_items,
        title="BMI Categories",
        loc="upper right"
    )

    plt.title(
        "BMI Comparison Dashboard",
        fontsize=18,
        fontweight="bold"
    )

    plt.xlabel(
        "Participants",
        fontsize=12,
        fontweight="bold"
    )

    plt.ylabel(
        "BMI Score",
        fontsize=12,
        fontweight="bold"
    )

    plt.grid(
        axis="y",
        linestyle="--",
        alpha=0.4
    )

    plt.tight_layout()
    plt.show()


# ============================================================
# MAIN FUNCTION
# ============================================================

def main() -> None:
    """
    Program entry point.
    """

    print("=" * 60)
    print("       WELCOME TO BMI CALCULATOR & VISUALIZER")
    print("=" * 60)

    users = collect_user_data()

    display_report(users)

    print("\nGenerating visualization...")
    show_bar_graph(users)

    print("\nThank you for using BMI Calculator & Visualizer.")


# ============================================================
# RUN APPLICATION
# ============================================================

if __name__ == "__main__":
    main()