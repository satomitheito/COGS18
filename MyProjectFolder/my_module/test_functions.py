"""Test for my functions.

Note: because these are 'empty' functions (return None), here we just test
  that the functions execute, and return None, as expected.
"""
import sys


from functions import Main_Menu, view_season, remove_seed


def test_Main_Menu():
    "Test if main menu does what the user inputs"
    number = 1
    assert number == view_season()

    number = 2
    assert number == add_seed()
    
    number = 3
    assert number == remove_seed()
    
    number = 4
    assert number == view_cart()
    
    number = 5
    assert number == check_out()
    
    number = 6
    assert number == sys.exit()
    
    
def test_view_season():
    "Test if user is able to view all season seed pages when requested"
    number = 1
    assert number == Spring_Seeds()
    
    number = 2
    assert number == Summer_Seeds()
    
    number = 3
    assert number == Fall_Seeds()
    
    number = 4
    assert number == Winter_Seeds()
    
    number = 5
    assert number == Main_Menu()
    
    
def test_remove_seed():    
    "Test if the seed is removed from shopping cart"
    seed = poppy seeds
    amount = 2
    shopping_cart[seed] = 10
    assert shopping_cart[seed] == 8 



                 
    