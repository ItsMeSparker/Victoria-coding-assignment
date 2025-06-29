import doctest

#Part ONE
def get_biggest(a: float, b: float, c: float) -> float:
    """ This function will take 3 floating value and return the biggest of 
    the three.
    >>> get_biggest(2,4,3)
    4
    >>> get_biggest(-1,6,9)
    9
    >>> get_biggest(10,3,7)
    10
    >>> get_biggest(-1,-2,-3)
    -1
    """    
    temp = 0
    if a > b:
        temp = a
    else: temp = b
    
    if c > temp:
        temp = c
    return temp
    
def get_smallest(a: float, b: float, c: float) -> float:
    """ This function will take 3 floating value and return the smallest of 
    the three.
    >>> get_smallest(1,2,3)
    1
    >>> get_smallest(4,9,2)
    2
    >>> get_smallest(23,10,44)
    10
    >>> get_smallest(-12,11,22)
    -12
    """    
    temp = 0
    if a < b:
        temp = a
    else: temp = b
    
    if c < temp:
        temp = c
    return temp

def is_multiple_of(n1: int, n2: int) -> bool:
    """ This function will take 2 integers and indicate if the first integer
    is the multiple of the second integer or not.
    >>> is_multiple_of(8,2)
    True
    >>> is_multiple_of(9,2)
    False
    """            
    if (n2 == 0) :
        if(n1 == 0):
            return True
        else: return False
    elif (n1%n2) == 0 :
            return True
    else: return False
    

def is_biggest_multiple_of_smallest(a: int, b: int, c: int) -> bool:
    """ This function will take 3 integers and indicate if the biggest integer
    is the multiple of the smallest integer or not.
    >>> is_biggest_multiple_of_smallest(7,12,2)
    True
    >>> is_biggest_multiple_of_smallest(7,39,18)
    False
    """      
    x = get_biggest(a ,b , c)
    y = get_smallest(a, b, c)
    result = is_multiple_of(x, y)
    return result
    
    

#Part TWO
def get_discount(discount_code: str, membership: bool) -> int:
    """This function will return the discount based on the discount code.
    >>> get_discount('FREQUENT_BUYER', True)
    -2
    >>> get_discount('FIRST_PURCHASE', False)
    -10
    >>> get_discount('NO_DISCOUNT', False)
    0
    """
    if(discount_code == 'FIRST_PURCHASE'):
        return 10
    elif(discount_code == 'FREQUENT_BUYER' and membership == True):
        return 2
    else: return 0    
    
def get_discounted_price(discount_code: str, price: float, membership: bool) -> float:
    """This function will calculate and return the price after used the 
    discount, it also uses the privious function.
    >>> get_discounted_price('FREQUENT_BUYER', 10.0, True)
    8.0
    >>> get_discounted_price('FIRST_PURCHASE', 20.0, False)
    10.0
    >>> get_discounted_price('NO_DISCOUNT', 6.0, False)
    6.0
    """    
    if price <= 0:
        return 0
    
    discount = get_discount(discount_code, membership)
    price = price - discount 
    
    if price <= 0 : 
        price = 0
    
    return price

def get_shipping(membership: bool, country: str, price: float) -> float:
    """ This function will calculate and return the shipping price based on
    country (if it outside Canada or not) and membership
    >>> get_shipping(True, 'France', 12.0)
    0
    >>> get_shipping(False, 'Canada', 16.0)
    0
    >>> get_shipping(False, 'Brazil', 18.0)
    1.8
    """
    if(country == 'Canada' or membership == True):
        return 0
    else:
        return (price*0.1)
    
def display_charges(price: float, tax: int, membership: bool, discount_code: str, country: str):
    """ This function will print the information of the certain purchase based
    on price of a product, tax, membership of the buyer, discount code, and 
    bountry on the buyer. This function uses the privious functions for
    calculating.
    >>> display_charges(22.0, 8, False, 'FIRST_PURCHASE', 'Mexico')
    price: $ 12.00
    tax: $ 0.96
    shipping: $ 2.20
    total charge: $ 15.16
    """       
    shipping = get_shipping(membership, country, price)
    price = get_discounted_price(discount_code, price, membership)   
    
    tax = price * (tax/100)
    
    print(f"price: $ {price:.2f}", f"tax: $ {tax:.2f}", f"shipping: $ {shipping:.2f}", f"total charge: $ {(price+tax+shipping):.2f}", sep = '\n' )