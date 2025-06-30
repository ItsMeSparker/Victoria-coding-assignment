import doctest

def compute_harmonic_series(n: int) -> float:
    """ This function will take an integer and return the sum of harmonic 
    series of the first n number of the series
    compute_harmonic_series(3)
    1.8333333333333333
    >>> compute_harmonic_series(5)
    2.283333333333333
    >>> compute_harmonic_series(2)
    1.5
    >>> compute_harmonic_series(30)
    3.9949871309203906
    >>> compute_harmonic_series(-1)
    0
    """
    x = 0
    for i in range(n):
        x = x + (1/(i+1))
        #print(f'1/{i+1}, {x}')
    
    return x

def get_fibonacci_sequence(n: int) -> str:
    """ This function will take an integer and return the first n number(s) of
    fibonacci sequence in string
    >>> get_fibonacci_sequence(1)
    '0'
    >>> get_fibonacci_sequence(0)
    ''
    >>> get_fibonacci_sequence(2)
    '0,1'
    >>> get_fibonacci_sequence(3)
    '0,1,1'
    >>> get_fibonacci_sequence(4)
    '0,1,1,2'
    >>> get_fibonacci_sequence(6)
    '0,1,1,2,3,5'
    >>> get_fibonacci_sequence(9)
    '0,1,1,2,3,5,8,13,21'
    >>> get_fibonacci_sequence(15)
    '0,1,1,2,3,5,8,13,21,34,55,89,144,233,377'
    """
    result = ''
    temp1 = 0
    temp2 = 1
    temptemp = 0
    if n <= 0:
        return result
    elif n == 1:
        result = result + str(temp1)
        return result
    else:
        result = result + str(temp1) + ','
        result = result + str(temp2)
        for i in range(n-2):
            result = result + ','
            result = result + str(temp1 + temp2)
            temptemp = temp1
            temp1 = temp2
            temp2 = (temptemp + temp2)
    return result
        
#0 1 1 2 3 5 8 13
# n = 3; 0 1 1
# n = 4; 0 1 1 2


def print_pattern(row: int, col: int, first: str, second: str):
    """ This functin will print you the 2 patterns that  will switch the 
    sequence one after another
    >>> print_pattern(3,4,'%%%','@')
    %%%@%%%@%%%@%%%@
    @%%%@%%%@%%%@%%%
    %%%@%%%@%%%@%%%@
    >>> print_pattern(4,3, '!@', '$$$')
    !@$$$!@$$$!@$$$
    $$$!@$$$!@$$$!@
    !@$$$!@$$$!@$$$
    $$$!@$$$!@$$$!@
    """
    for i in range(row):
        for j in range(col):
            if i%2 == 0 :
                print(first+second, end = '')
            else: print(second+first, end = '')
        print()