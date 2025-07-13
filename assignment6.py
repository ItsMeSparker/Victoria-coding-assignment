import doctest
import math

def get_powers(li: list[int], exponant: int) -> list[int]:
    """ This function will take a list of bases and a integer that will
    use as an exponant. the function will return the list of power.
    >>> get_powers([1,2,3,4,5],2)
    [1, 4, 9, 16, 25]
    >>> get_powers([-1,-2,-3,-4,-5],2)
    [1, 4, 9, 16, 25]
    >>> get_powers([-1,-2,-3,-4,-5],3)
    [-1, -8, -27, -64, -125]
    >>> get_powers([1,2,3,4,5],0)
    [1, 1, 1, 1, 1]
    >>> get_powers([0,0,0],2)
    [0, 0, 0]
    >>> get_powers([],100)
    []
    """
    new_list = []
    for i in range(len(li)):
        new_list.append(pow(li[i], exponant))
    
    return new_list
    
def concatenate(li: list[str]) -> str:
    """ This function will take a list of strings and return a string will all
    the elements in the list seperated with one single space.
    >>> concatenate(['abc', 'ef'])
    'abc ef'
    >>> concatenate(['This', 'is', 'banana'])
    'This is banana'
    >>> concatenate([])
    ''
    >>> concatenate(['Python is', 'so much', 'fun'])
    'Python is so much fun'
    >>> concatenate(['Hello', 'World'])
    'Hello World'
    """
    result = ''
    for i in range(len(li)):
        result += li[i] + ' '
        
        
    return result[:-1]

def contains_multiple(li: list[int], num: int) -> bool:
    """ This function will take a list of integers and a number, which will 
    return True if the element(s) of the list contain multiply of that number.
    >>> contains_multiple([1,2,3,5,7,9],2)
    True
    >>> contains_multiple([1,3,5,7,9],2)
    False
    >>> contains_multiple([],2)
    False
    >>> contains_multiple([0,0,0,0,0],2)
    True
    >>> contains_multiple([-1,-2,-3,-5,-7,-9],2)
    True
    >>> contains_multiple([3, 36, 8, 9, 14, 28, 11, 31, 17, 20, 2, 5, 15, 30], 0)
    False
    >>> contains_multiple([19, 30, 27, 13, 22, 18, 24, 0, 17, 10, 31, 29, 8, 26], 0)
    True
    """
    if num == 0:
        for j in li:
            if j == 0:
                return True
        return False
    
    for i in li:
        if i%num == 0:
            return True
    return False
    
def get_long_enough(li: list[str], threshold: int) -> list[str]:
    """ This function will take a list of strings and a threshold number, then
    this function will return the list, which contain only the elements that 
    length is at least equal to or more than the threshold number.
    >>> get_long_enough(['Toyota', 'BMW', 'Mitsubishi', 'Mercides'], 4)
    ['Toyota', 'Mitsubishi', 'Mercides']
    >>> get_long_enough(['Nvidia', 'AMD', 'Intel'], 3)
    ['Nvidia', 'AMD', 'Intel']
    >>> get_long_enough(['Boeing', 'Lockheed Martin'], 7)
    ['Lockheed Martin']
    >>> get_long_enough([], 2)
    []
    >>> get_long_enough(['Apple', 'Orange', 'Banana'], -1)
    ['Apple', 'Orange', 'Banana']
    """
    new_list = []
    for i in li:
        if len(i) >= threshold:
            new_list.append(i)
    return new_list
        
def all_multiples(li: list[int], num: int) -> bool:
    """ This function will take a list of integers and a number. This fuction
    will determine if all the elements in the list is multiplies of that number.
    >>> all_multiples([2,4,6],2)
    True
    >>> all_multiples([2,4,6],4)
    False
    >>> all_multiples([-2,-4,-6,-8],2)
    True
    >>> all_multiples([],2)
    True
    >>> all_multiples([0],4)
    True
    >>> all_multiples([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 0)
    True
    >>> all_multiples([6, -9, 1, 17, 8, 19, -3, 18, -10, 9, 7, -18, -16, -2, -13, 2], 0)
    False
    """
    if num == 0:
        for j in li:
            if j != 0:
                return False
        return True
    
    for i in li:
        if i%num != 0:
            return False
    return True


def getting_shorter(li: list[str]) -> bool:
    """ This funtion will take a list of strings and will determine if all the
    length of elements in the list is shorter than the one before by one or not.
    >>> getting_shorter(['tiny', 'same', 'are', 'at'])
    False
    >>> getting_shorter(['biggest', 'bigger', 'ATE', 'at'])
    True
    >>> getting_shorter(['Sword', 'Snap', 'Saw'])
    True
    >>> getting_shorter([])
    True
    """
    for i in range(len(li) - 1):
        if len(li[i]) <= len(li[i+1]):
            return False
    return True