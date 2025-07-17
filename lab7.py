import doctest

def swap(li: list, i: int, j: int):
    """ This function will take a list and swap the value of the taken 2 index.
    >>> lst = [0, 1, 2]
    >>> swap(lst, 1, 0)
    >>> lst
    [1, 0, 2]
    >>> lst = [0, 1, 2, 3, 4, 5]
    >>> swap(lst, 3, 5)
    >>> lst
    [0, 1, 2, 5, 4, 3]
    """
    temp = li[i]
    li[i] = li[j]
    li[j] = temp

def index_of_smallest(li: list) -> int:
    """ This function will take a list and return an index of the smallest
    value in the list.
    >>> index_of_smallest([23, 31, 55, 32, -2])
    4
    >>> index_of_smallest([-8, 67, -10, -1, 32])
    2
    >>> index_of_smallest([])
    -1
    >>> index_of_smallest([-1, 0, 1])
    0
    """
    if not li:
        return -1
    
    result = 0
    for i in range(1, len(li)):
        if li[i] < li[result]:
            result = i
    return result

FlightInfo = tuple[str, str, float]

def total_duration(li: list[FlightInfo]) -> float:
    """ This function will take a tuple list and calculate the sum of all
    hours in all flight.
    >>> total_duration([('Victoria', 'Mexico City', 5.5), ('Vancouver', 'Toronto', 4)])
    9.5
    >>> total_duration([('Bangkok', 'Tokyo', 5), ('London', 'Manchester', 1)])
    6
    """
    result = 0
    for i in range(len(li)):
        result += li[i][2]
    return result
    
def get_destinations_from(li: list[FlightInfo], Departure: str) -> list:
    """ This function will take the tuple list of flights information and 
    a string of destination. This function wll return a list of arrival city
    uniquely that are departed from the departure city.
    >>> get_destinations_from([('Victoria', 'Vancouver', 0.75), ('Vancouver', 'Toronto', 4), ('Victoria', 'Calgary', 1.5), ('Victoria', 'Vancouver', 0.5)], 'Victoria')
    ['Vancouver', 'Calgary']
    """
    New_list = []
    for i in range(len(li)):
        if Departure == li[i][0] and not li[i][1] in New_list:
            New_list.append(li[i][1])
    return New_list