import pytest
import random
from unittest.mock import patch
from io import StringIO
import sys

# Assuming the student's code is in a file named 'adventure.py'
# We'll import it to test its functions.
import adventure

# Test 6: Simulate "right" path
@patch('random.choice', return_value='right')
def test_right_path(mock_choice, capsys):
    # Re-initialize global variables for this test
    adventure.PLAYER_HEALTH = 100
    adventure.HAS_TREASURE = False
    
    #reload the module to update the variables
    import importlib
    importlib.reload(adventure)

    captured = capsys.readouterr()
    assert "You fall into a pit" in captured.out
    assert adventure.PLAYER_HEALTH == 85
