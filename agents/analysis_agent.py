"""
Analysis Agent for NourishBot.

Responsible for:
- Calculating nutrition for detected foods
- Generating a nutrition report
"""

from typing import Any

from utils.nutrition_db import calculate_nutrition

REPORT_SEPARATOR = "=" * 42


def analyze_meal(food_items: list[str]) -> str:
    """
    Analyze detected foods and generate a nutrition report.

    Args:
        food_items: List of detected food names.

    Returns:
        Formatted nutrition report.
    """

    if not food_items:
        return (
            f"{REPORT_SEPARATOR}\n"
            "NUTRITION REPORT\n"
            f"{REPORT_SEPARATOR}\n\n"
            "No foods were detected.\n"
        )

    nutrients: dict[str, Any] = calculate_nutrition(food_items)

    report = (
        f"{REPORT_SEPARATOR}\n"
        "NUTRITION REPORT\n"
        f"{REPORT_SEPARATOR}\n\n"
        f"Detected Foods:\n"
        f"{', '.join(food_items)}\n\n"
        f"Calories : {nutrients['calories']} kcal\n"
        f"Protein  : {nutrients['protein']} g\n"
        f"Carbs    : {nutrients['carbs']} g\n"
        f"Fat      : {nutrients['fat']} g\n\n"
        f"{REPORT_SEPARATOR}"
    )

    return report