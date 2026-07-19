"""
Unit tests for the Food Resolver.

Run using:
    pytest
"""

import pytest


# -------------------------------------------------
# Input Validation
# -------------------------------------------------

def test_empty_string(resolver):
    """Empty string should return None."""
    assert resolver.resolve("") is None


def test_whitespace_string(resolver):
    """Whitespace-only input should return None."""
    assert resolver.resolve("     ") is None


def test_none_input(resolver):
    """None input should return None."""
    assert resolver.resolve(None) is None


# -------------------------------------------------
# Exact Match Tests
# -------------------------------------------------

def test_exact_banana(resolver):
    result = resolver.resolve("banana")

    assert result is not None
    assert result["normalized_name"] == "banana"


def test_exact_pizza(resolver):
    result = resolver.resolve("pizza")

    assert result is not None
    assert result["normalized_name"].lower() == "pizza"


def test_exact_broccoli(resolver):
    result = resolver.resolve("broccoli cooked")

    assert result is not None
    assert result["normalized_name"] == "broccoli cooked"


# -------------------------------------------------
# Fuzzy Matching
# -------------------------------------------------

def test_fuzzy_banana(resolver):
    """Misspelled banana should still resolve."""

    result = resolver.resolve("bananna")

    assert result is not None
    assert result["normalized_name"] == "banana"


def test_fuzzy_white_rice(resolver):
    result = resolver.resolve("white rice")

    assert result is not None


# -------------------------------------------------
# Unknown Foods
# -------------------------------------------------

def test_unknown_food(resolver):
    result = resolver.resolve("xyzfoodabc123")

    assert result is None


# -------------------------------------------------
# Returned Database Row
# -------------------------------------------------

def test_database_row_contains_fields(resolver):
    result = resolver.resolve("banana")

    assert result is not None

    expected_fields = [
        "normalized_name",
        "calories",
        "protein",
        "carbs",
        "fat",
    ]

    for field in expected_fields:
        assert field in result


# -------------------------------------------------
# Nutrition Values
# -------------------------------------------------

def test_nutrition_values_are_numeric(resolver):
    result = resolver.resolve("banana")

    assert isinstance(result["calories"], (int, float))
    assert isinstance(result["protein"], (int, float))
    assert isinstance(result["carbs"], (int, float))
    assert isinstance(result["fat"], (int, float))


# -------------------------------------------------
# Case Insensitivity
# -------------------------------------------------

@pytest.mark.parametrize(
    "query",
    [
        "banana",
        "BANANA",
        "Banana",
        "bAnAnA",
    ],
)
def test_case_insensitive_lookup(resolver, query):
    result = resolver.resolve(query)

    assert result is not None
    assert result["normalized_name"] == "banana"


# -------------------------------------------------
# Resolver Stability
# -------------------------------------------------

@pytest.mark.parametrize(
    "query",
    [
        "rice",
        "white rice",
        "banana",
        "pizza",
        "broccoli",
        "milk",
        "apple",
        "egg",
        "chicken",
    ],
)
def test_resolver_never_crashes(resolver, query):
    """
    The resolver should never raise an exception
    for common food names.
    """

    resolver.resolve(query)