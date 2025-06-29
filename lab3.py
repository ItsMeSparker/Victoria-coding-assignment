import doctest
GST = 0.05
PST = 0.1

def get_longer(s1: str, s2: str) -> str:
    """
    Q1. a function that will take as arguments two strings and will return the
    string that is the longer of the two.
    >>> get_longer('Cookies', 'Truck')
    'Cookies'
    >>> get_longer('Phone', 'Coffee')
    'Coffee'
    >>> get_longer('Tesla', 'Zebra')
    'Tesla'
    """
    if(len(s1) >= len(s2)):
        return s1
    else: return s2
    

def get_tax(food: float, alcohol: float) -> float:
    """
    Q2. a function that will calculate and return the tax owed on restaurant 
    charges for food and alcohol.
    >>> get_tax(10,15)
    2.75
    """
    food = (food * GST)
    alcohol = (alcohol * GST) + (alcohol * PST)
    tax = food + alcohol
    return tax
    
def get_bill_share(food: float, alcohol: float, people: int) -> float:
    """
    Q3. a function that will calculate and return the amount each person in a 
    group owes on restaurant charges for food and alcohol divided equally among 
    them.
    >>> get_bill_share(20,30,5)
    11.1
    >>> get_bill_share(40,60,1)
    111.0

    """
    charge = food + alcohol + get_tax(food, alcohol)
    share = charge/people
    return share

