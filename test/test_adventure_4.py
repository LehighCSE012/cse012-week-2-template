import pytest
import random
from unittest.mock import patch
from io import StringIO
import sys

# Assuming the student's code is in a file named 'adventure.py'
# We'll import it to test its functions.
import adventure

# Test 1: Check Initial Values of Global Variables
def test_initial_values():
    assert adventure.PLAYER_HEALTH == 100
    assert 50 <= adventure.MONSTER_HEALTH <= 75
    assert adventure.HAS_TREASURE == False