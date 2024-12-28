import pytest
import random
from unittest.mock import patch
from io import StringIO
import sys

# Assuming the student's code is in a file named 'adventure.py'
# We'll import it to test its functions.
import adventure

# Test 5: Monster defeats player
@patch('random.choice', return_value='right')
def test_monster_wins(mock_choice, capsys):
    # Re-initialize global variables for this test
    adventure.PLAYER_HEALTH = 10
    adventure.MONSTER_HEALTH = 50
    adventure.HAS_TREASURE = False

    #reload the module to update the variables
    import importlib
    importlib.reload(adventure)

    captured = capsys.readouterr()
    assert "Game Over!" in captured.out
    assert adventure.HAS_TREASURE == False
