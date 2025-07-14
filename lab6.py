import doctest

def sum_even_values(li: list[int]) -> int:
    """ This function will take a list and return sum of even number in the list
    >>> sum_even_values([])
    0
    >>> sum_even_values([1,2,3,4,5,6])
    12
    >>> sum_even_values([12,13,15,17,19])
    12
    >>> sum_even_values([-1,-2,-3,-4,-5,-6])
    -12
    """
    Sum = 0
    for i in li:
        if i%2 == 0:
            Sum += i
    return Sum
    
def count_above(li: list[int], threshold: int) -> list:
    """ This function will take a list and a threshold, then it will return
    an integer that indicate how many number is exceed the threshold
    >>> count_above([1,2,3,4,5,6], 3)
    3
    >>> count_above([1,2,3,4,5,6], -1)
    6
    >>> count_above([], 0)
    0
    >>> count_above([-1,-2,-3,-4], 0)
    0
    >>> count_above([99,98,97,96], 50)
    4
    """
    result = 0
    for i in li:
        if i > threshold:
            result += 1
    return result
    
def add1(li: list[int]) -> list:
    """ This function will take a list of integer and then will add up every
    element by one then return a new list
    >>> add1([1,2,3,4,5,6])
    [2, 3, 4, 5, 6, 7]
    >>> add1([0,0,0,0,0,0])
    [1, 1, 1, 1, 1, 1]
    >>> add1([])
    []
    >>> add1([-1,-2,-3,-4])
    [0, -1, -2, -3]

    """
    new_list = []
    for i in range(len(li)):
        new_list.append(li[i] + 1)
    
    return new_list
    
def are_all_even(li: list[int]) -> bool:
    """ This function will take a list of integer then will indicate if all
    the integer in the list is even or not
    >>> are_all_even([])
    True
    >>> are_all_even([2,4,6,8,10])
    True
    >>> are_all_even([2,4,6,9,10])
    False
    >>> are_all_even([-2,-4,-6,-98,-100])
    True
    """
    flag = True
    for i in li:
        if i%2 != 0:
            return False
    return True