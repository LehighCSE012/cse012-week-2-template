import pytest
import random
from unittest.mock import patch
from io import StringIO
import sys

# Assuming the student's code is in a file named 'adventure.py'
# We'll import it to test its functions.
import adventure
# Test 7: Treasure not found
def test_treasure_not_found(capsys):
    # Re-initialize global variables for this test
    adventure.PLAYER_HEALTH = 100
    adventure.MONSTER_HEALTH = 60
    adventure.HAS_TREASURE = False
    
    #reload the module to update the variables
    import importlib
    importlib.reload(adventure)

    captured = capsys.readouterr()
    assert "The monster did not have the treasure. You continue your journey." in captured.out or "Game Over!" in captured.out