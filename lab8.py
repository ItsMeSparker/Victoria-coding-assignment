import os
import math

person_info = tuple[str, int]
#filename = 'lab8-name-age-copy.txt'
#blankfile = 'blankfile.txt'

def file_to_person_list(filename: str) -> list[person_info]:
    """ This function will take a filename and will return the tuple list of
    person information (name and age).
    """
    result = []
    file_handle = open(filename, 'r')
    for line in file_handle:
        name, age = line.strip().split()
        result.append((name, int(age)))
    file_handle.close()
    return result

def get_average_age(person_info: list[person_info]) -> int:
    """ This function will take a tuple list of name and age and will calculate
    the average age of the sample.
    """
    Sum = 0
    if len(person_info) == 0:
        return 0    
    for person in range(len(person_info)):
        
        Sum += person_info[person][1]
    return math.floor(Sum/len(person_info))

def get_above_age(person_info: list[person_info], threshold: int) -> \
    list[person_info]:
    """ This function will take tuple list and threshold number, then this
    function will return the tuple list of only people who age exceed threshold.
    """
    result = []
    for person in range(len(person_info)):
        if person_info[person][1] > threshold:
            result.append(person_info[person])
    return result
    
def to_file(person_info: list[person_info], filename: str):
    """ This function will take a tuple list and will overwtite the file with
    a tuple seperate by comma line by line.
    """
    file_handle = open(filename, 'w')
    for person in person_info:
        file_handle.write(person[0] + ',' + str(person[1]) + '\n')
    file_handle.close()

def write_names_above_avg_age(input_file: str, output_file: str):
    """ This function will use every function priviously. it will take a input
    file and output file path to take information of people, find their average
    age, filter them for only the one who are older than avarage age, and 
    overwrite their infomaation in an output file.
    """
    person_info = file_to_person_list(input_file)
    average_age = get_average_age(person_info)
    person_info = get_above_age(person_info, average_age)
    to_file(person_info, output_file)