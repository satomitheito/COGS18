"""A collection of function for doing my project."""
import sys


# this represents the user's (currently empty) shopping cart
shopping_cart = {}

# This function (Main_Menu) is not an external code. However, the method of user inputting numbers to navigate (using if then statements) was inspired by this source https://www.youtube.com/watchv=0m7csmqWAgI&t=8s&ab_channel=GeekTutorials I felt it was important to cite this. 
def Main_Menu():
    """ 

    Function that helps user navigate through the process of viewing items, buying, removing, and checking out through their integer inputs. 
    
    
    """
    
    while True:
        #when printed, Menu Options will be in bold
        print('\033[1m' + 'Menu Options')
        
        #this unbolds the rest of the text
        print('\033[0m')
        
        print('''Pick a number:
        1. View seeds 
        2. Add seeds to cart
        3. Remove seed from cart
        4. View cart
        5. Checkout cart
        6. Exit 
        ''')
        
        number = input('Page number: ')
        
        if number == '1':
            view_season()
        elif number == '2':
            add_seed()
        elif number == '3':
            remove_seed()
        elif number == '4':
            view_cart()
        elif number == '5':
            check_out()
        elif number == '6':
            sys.exit()
        else:
            print('Please type in a number from 1-5')
            

def view_season():
    """
    Function that lets user know that the seeds are split in four seasons.
    
    """
    while True:
        print('''Choose Season
        Pick a number:
        1. Spring
        2. Summer
        3. Fall
        4. Winter
        5. Go Back
        ''')
        
        number = input('Page number: ')
        
        if number == '1':
            Spring_Seeds()
        elif number == '2':
            Summer_Seeds()
        elif number == '3':
            Fall_Seeds()
        elif number == '4':
            Winter_Seeds()
        elif number == '5':
            Main_Menu()
        else:
            print('Please type in a number from 1-5')
    
        
# the dictionary that represents spring seeds            
spring_dict = {'cauliflower seeds': 80 , 'garlic seeds': 40 , 'jazz seeds': 30 , 'kale seeds': 70 , 'parsnip seeds': 20 , 'potato seeds': 50 , 'rhubarb seeds': 100 , 'strawberry seeds': 100 }


# the dictionary that represents summer seeds
summer_dict = {'blueberry seeds': 80 , 'corn seeds': 150 , 'melon seeds': 80 , 'pepper seeds': 40 , 'poppy seeds': 100 , 'sadish seeds': 40 , 'red cabbage seeds': 100 , 'spangle seeds': 50 , 'sunflower seeds': 200 , 'starfruit seeds': 400 , 'tomato seeds': 50 , 'wheat seeds': 10 }


#the dictionary that represents the fall seeds
fall_dict = {'amaranth seeds': 70 , 'artichoke seeds': 30 , 'beet seeds': 20 , 'bok choy seeds': 50 , 'corn seeds': 150 , 'cranberry seeds': 240 , 'eggplant seeds': 20 , 'fairy seeds': 200 , 'pumpkin seeds': 100 , 'sunflower seeds': 200 , 'wheat seeds': 10 , 'yam seeds': 60 }


# the three dictionaries listed above combined into one
all_seed = {**spring_dict, **summer_dict, **fall_dict}


def Spring_Seeds():
    """
    
    Function that prints out the spring dictionary
    
    """
    print('---- item : $ -----')
    
    #loops through the spring_dict dictionary and prints out each of the value stores in that dictionary until it reaches the end
    for seed in spring_dict:
        print(' ' + seed, ':', spring_dict[seed])
        
    print('---------')
      
        
def Summer_Seeds():
    """
    
    Function that prints out the summer dictionary
    
    """  
    print('---- item : $ -----')
    
    #loops through the summer_dict dictionary and prints out each of the value stores in that dictionary until it reaches the end
    for seed in summer_dict:
        print(' ' + seed, ':', summer_dict[seed])
        
    print('---------')
    
    
def Fall_Seeds():
    """
    
    Function that prints out the fall dictionary
    
    """
    print('---- item : $ -----')
    
    #loops through the fall_dict dictionary and prints out each of the value stores in that dictionary until it reaches the end
    for seed in fall_dict:
        print(' ' + seed, ':', fall_dict[seed])
        
    print('---------')
         
        
def Winter_Seeds():
    """
    
    Function that prints the winter option
    
    """
    print('''
    There are no winter seeds...
    ''')


def add_seed():
    """
    
    Function that adds the seed name and the amount inputted by the user into the empty shopping cart
    
    """
    #the user types the seed name
    seed = input('Type out seed name: ')
    
    #the user input would be turned into lower case
    seed = seed.lower()
    
    #the amount of items would be added to the shopping cart
    if seed in all_seed:
        amount = int(input('Enter quantity: '))
        shopping_cart[seed] = amount
        print('Added')
    
    #there won't be any duplicates of item
    elif seed in shopping_cart:
        amount = int(input('Item already in cart. Just input quantity'))
        shopping_cart[seed] = shopping_cart[seed] + amount
        
    else:
        print('Item cannot be found. Was the word spelled and spaced properly?')
    
    
def remove_seed():
    """
    
    Function that removes the inputted amount of seeds in a certain item
    
    """
    #the user types the seed name
    seed = input('Type out seed name: ')
    
    #the user input would be turned into lower case
    seed = seed.lower()
    
    #if seed inputted is detected, the amount of seed inputted would be removed
    if seed in shopping_cart:
        amount = int(input('How many would you like to remove?'))
        shopping_cart[seed] = shopping_cart[seed] - amount
        print('Removed')
        
    else:
        print('Item not found. Was the word spelled and spaced properly?')

        
def view_cart():
    """
    
    Function that indicates the item and its amount in the shopping cart along with the total price for each item
    
    """
    print('--- item : quantity ---')
    
    #the shopping cart is looped until each item and amount in the cart is printed out
    for seed in shopping_cart:
        print(seed, ':', shopping_cart[seed])
        
    print('---------')
    
    print('--- Total cost for each item in its respective order ---')
    
    #the items in the shopping are lopped until each item amount are calculated
    for seed in all_seed and shopping_cart:
        
        if seed in all_seed and shopping_cart:
            total_cost = all_seed[seed] * shopping_cart[seed]
            
        print(total_cost)

            
def check_out():
    """
    
    Function that checks out the item and clears the shopping cart if checked out
    
    """
    #user inputs based on the question
    question = input('Are you ready to check out? Type 1 for yes or 2 for no')
    
    if question == '1':
        print('''You have checked out and your shopping cart has been cleared
        
              Thank you for shopping :D''')
        
        #this clears the shopping_cart
        shopping_cart.clear()
        
    elif question == '2':
        print('We will return to main menu')
        #this takes the user back to the Main_Menu function
        Main_Menu()
        
    else:
        print('Please pick between 1 or 2')
         