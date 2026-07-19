import sys
from pathlib import Path

import pytest

# Add project root to Python path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from utils.food_mapper.resolver import FoodResolver


@pytest.fixture(scope="session")
def resolver():
    return FoodResolver("database/nutrition.db")