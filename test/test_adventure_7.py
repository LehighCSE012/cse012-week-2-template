import pytest
import random
from unittest.mock import patch
from io import StringIO
import sys

# Assuming the student's code is in a file named 'adventure.py'
# We'll import it to test its functions.
import adventure

# Test 4: Player defeats monster
@patch('random.choice', return_value='right') 
def test_player_wins(mock_choice, capsys):
    # Re-initialize global variables for this test
    adventure.PLAYER_HEALTH = 100
    adventure.MONSTER_HEALTH = 15 #Ensure player will win in one turn
    adventure.HAS_TREASURE = False
    
    #reload the module to update the variables
    import importlib
    importlib.reload(adventure)
    
    captured = capsys.readouterr()
    assert "You defeated the monster!" in captured.out
    assert adventure.HAS_TREASURE == True
