import doctest
#PartONE

def get_factors(n: int) -> str:
    """ This function will take an integer and return the string of set of
    numbers that are factors of a certain integer. This function will also
    assume that the taken argument is an positive integer.
    >>> get_factors(3)
    '1,3'
    >>> get_factors(8)
    '1,2,4,8'
    >>> get_factors(10)
    '1,2,5,10'
    >>> get_factors(0)
    ''
    >>> get_factors(-1)
    ''
    >>> get_factors(1)
    '1'
    >>> get_factors(25)
    '1,5,25'
    """
    x = ''
    
    if n<=0: return x
    
    for i in range(n):
        if i != 0:
            if n%i == 0:
                x = x+str(i)
                x  = x+','
    x = x+str(n)
    return x

def get_range_of_factors(a: int, b: int) -> str:
    """ This function will take 2 integers as the range of numbers and will
    return a string where each line contains the factors of each number in that range.
    It also uses the previous function.
    >>> print(get_range_of_factors(10, 13))
    1,2,5,10
    1,11
    1,2,3,4,6,12
    
    >>> print(get_range_of_factors(1, 5))
    1
    1,2
    1,3
    1,2,4
    
    >>> print(get_range_of_factors(2, 2))
    
    >>> print(get_range_of_factors(2, 1))
    
    
    Somehow the doctest occur an error when I call the it, while the result 
    behave as expect.
    """
    result = ''
    for i in range(a, b):
        x = get_factors(i)
        result += x + '\n'
    return result
#p = get_range_of_factors(10,13)
#print(p) #if this is printed, it will look exactly like the example
    
def sum_fibonacci_sequence(n: int) -> int:
    """ This function will take the integer as an first n number of fibonacci
    sequence and return the sum of that first n number of fibonacci sequence.
    >>> sum_fibonacci_sequence(7)
    20
    >>> sum_fibonacci_sequence(2)
    1
    >>> sum_fibonacci_sequence(0)
    0
    >>> sum_fibonacci_sequence(1)
    0
    >>> sum_fibonacci_sequence(13)
    376
    """
    result = 0
    temp1 = 0
    temp2 = 1
    temptemp = 0
    if n <= 1:
        return result
    else:
        result = result + temp2
        for i in range(n-2):
            result = result + (temp1 + temp2)
            temptemp = temp1
            temp1 = temp2
            temp2 = (temptemp + temp2)
    return result 

#PartTWO

def print_tail(n: int):
    """
    This function will print the tail of the rocket, as well as it will be wider
    depends on the value of an argument
    """
    x = '/\\'
    print('//  ', end = '')
    for i in range (n):
        print(f'{x:4}', end = '')
        
    print('\\\\')
        
def print_booster(n: int):
    """
    This function will print the booster of the rocket, as well as it will be
    bigger depends on the value of an argument
    """
    
    for i1 in range (n+1):
        print('|', end = '')
        for j1 in range(n+1-i1, 1, -1):
            print('.', end ='')
        for j2 in range(i1+1):
            print('/\\', end = '')
        for j3 in range(((n-i1)*2)+1, 1, -1):
            print('.', end ='')      
        for j4 in range(i1+1):
            print('/\\', end = '')        
        for j5 in range(n+1-i1, 1, -1):
            print('.', end ='')            
        print('|')
        
    for i2 in range (n+1):
        print('|', end = '')
        for l1 in range(i2):
            print('.', end ='')
        for l2 in range(n+2-i2, 1, -1):
            print('\\/', end = '')
        for l3 in range((i2) * 2):
            print('.', end ='')      
        for l4 in range(n+2-i2, 1, -1):
            print('\\/', end = '')        
        for l5 in range(i2):
            print('.', end ='')            
        print('|')
    
    print('+', end = '' )
    for k in range((n+1)*2):
        print('=*', end = '')
    print('+')          
    
def print_instrument_unit(n: int):
    """
    This function will print the instrument unit of the rocket, as well as it 
    will be wider depends on the value of an argument
    """
    for i in range(2):
        print('||', end = '')
        for j in range((n*2) + 1):
            print('~#', end = '')
        print('||')
        
    print('+', end = '' )
    for k in range((n+1)*2):
        print('=*', end = '')
    print('+')        
    
def print_lem_adapter(n: int):
    """ This function will print the booster of the rocket, as well as it will be
    bigger depends on the value of an argument
    """
    print(' //', end = '')
    for i in range(n*2):
        print(' %', end = '')
    print("\\\\")
    
    print('//', end = '')
    for i in range((n*2) + 1):
        print(' %', end = '')
    print("\\\\")    
    
    print('+', end = '' )
    for k in range((n+1)*2):
        print('=*', end = '')
    print('+')            
    
def print_space_craft(n: int):
    """
    This function will print the space craft of the rocket, as well as it 
    will be bigger depends on the value of an argument
    """
    for i in range(n*2):
        print('  ', end = '') #I print this to make it fit to the rocket
        for j1 in range((n*2)+1-i, 1, -1):
            print(' ', end = '')
        for j2 in range(i):
            print('/', end = '')
        print('**', end = '')
        for j3 in range(i):
            print('\\', end = '')       
        for j4 in range((n*2)+1-i, 1, -1):
            print(' ', end = '')
        print()
                
    print('  +', end = '' )
    for k in range(n*2):
        print('=*', end = '')
    print('+')       
    
    
def print_rocket_ship(a: int, b: int):
    """
    This function will use the privious 5 functions to print the entire rocket
    the size of the rocket will increase by argunet a and the number instrument
    unit will increase by argument b
    """
    print_space_craft(a)
    print_lem_adapter(a)
    print_instrument_unit(a)
    for i in range(b):
        print_booster(a)
    print_tail(a)

