import pytest
import random
from unittest.mock import patch
from io import StringIO
import sys

# Assuming the student's code is in a file named 'adventure.py'
# We'll import it to test its functions.
import adventure

# Test 6: Treasure found
def test_treasure_found(capsys):
    # Re-initialize global variables for this test
    adventure.PLAYER_HEALTH = 100
    adventure.MONSTER_HEALTH = 60
    adventure.HAS_TREASURE = True
    
    #reload the module to update the variables
    import importlib
    importlib.reload(adventure)
    
    captured = capsys.readouterr()
    assert "You found the hidden treasure! You win!" in captured.out
