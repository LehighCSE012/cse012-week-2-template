import pytest
import sys
from io import StringIO
import adventure  # Assuming your code is in 'adventure.py'

def test_string_manipulation():
    """Test for correct string manipulation in intro using unittest.mock."""
    # Access the variables from the module
    assert isinstance(adventure.INTRO, str), "intro should be a string"
    assert adventure.CHARACTER_NAME in adventure.INTRO, "intro should contain character_name"
import pytest
import random
from unittest.mock import patch
from io import StringIO
import sys

# Assuming the student's code is in a file named 'adventure.py'
# We'll import it to test its functions.
import adventure

# Test 5: Simulate "left" path
@patch('random.choice', return_value='left')
def test_left_path(mock_choice, capsys):
    # Re-initialize global variables for this test
    adventure.PLAYER_HEALTH = 100
    adventure.HAS_TREASURE = False
    
    #reload the module to update the variables
    import importlib
    importlib.reload(adventure)
    
    captured = capsys.readouterr()
    assert "You encounter a friendly gnome" in captured.out
    assert adventure.PLAYER_HEALTH == 100
