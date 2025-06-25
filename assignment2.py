import math
import doctest

def check_funds(balance: float, purchase: float):
    """ Q1. a function that takes balance and amount of purchase, then calculate the result
    >>> check_funds(13,5)
    you will have $ 8.00 left after this purchase
    >>> check_funds(4,9)
    you are short $ 5.00
    >>> check_funds(-10,8)
    you have a negative balance
    """
    if balance >= purchase:
        print(f"you will have $ {(balance - purchase):.2f} left after this purchase")
    elif balance < 0:
        print("you have a negative balance")
    else:
        print(f"you are short $ {(purchase - balance):.2f}")
        

def print_biggest(a: float, b: float, c: float):
    """ Q2. a function that takes as arguments three floating point numbers and prints the biggest of the three values
    >>> print_biggest(2,4,3)
    4
    >>> print_biggest(-1,6,9)
    9
    >>> print_biggest(10,3,7)
    10
    >>> print_biggest(-1,-2,-3)
    -1
    """    
    temp = 0
    if a > b:
        temp = a
    else: temp = b
    
    if c > temp:
        temp = c
    print(temp)
    

def convert_inches(inches: int):
    """ Q3. a function that takes as an argument a distance in inches and displays the equivalent distance broken down into miles, yards, feet and inches.
    >>> convert_inches(63409)
    1 mi, 1 yd, 1 ft, 1 in
    """        
    
    # 1 ft = 12 inches
    # 1 yd = 36 inches
    # 1 mile = 63360 inches
    mile = 0
    yd = 0
    ft = 0
    
    
    while(inches >= 63360):
        inches = inches - 63360
        mile = mile + 1
    while(inches >= 36):
        inches = inches - 36
        yd = yd + 1
    while(inches >= 12):
        inches = inches - 12
        ft = ft + 1    
    print(f"{mile} mi, {yd} yd, {ft} ft, {inches} in")

    
def is_multiple_of(n1: int, n2: int):
    """ Q4. a function that takes two integers n1 and n2 and determines whether the first argument is a multiple of the second argument.
    >>> is_multiple_of(8,2)
    8 is a multiple of 2
    >>> is_multiple_of(9,2)
    9 is not a multiple of 2
    """            
    if (n2 == 0) :
        if(n1 == 0):
            print(f"{n1} is a multiple of {n2}")
        else: print(f"{n1} is not a multiple of {n2}")
    elif (n1%n2) == 0 :
            print(f"{n1} is a multiple of {n2}")
    else: print(f"{n1} is not a multiple of {n2}")
   

def display_charges(price: float, tax: int, member: bool, discount: str, country: str):
    """ Q5. a function that takes two integers n1 and n2 and determines whether the first argument is a multiple of the second argument.
    >>> display_charges(22.0, 8, False, 'FIRST_PURCHASE', 'Mexico')
    price: $ 12.00
    tax: $ 0.96
    shipping: $ 2.20
    total charge: $ 15.16
    """       
    if(member == True or country == 'Canada'):
        shipping = 0
    else: shipping = price * 0.1
    
    if(discount == 'FIRST_PURCHASE'):
        price = price - 10
    elif(discount == 'FREQUENT_BUYER' and member == True):
        price = price - 2
    else: price = price - 0
    
    if(price < 0):
        price = 0    
    
    tax = price * (tax/100)
    
    print(f"price: $ {price:.2f}\ntax: $ {tax:.2f}\nshipping: $ {shipping:.2f}\ntotal charge: $ {(price+tax+shipping):.2f}")
    
    