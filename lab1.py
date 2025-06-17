def print_my_info():
    """
    This function is used to give the info of me
    """
    name = 'Nico'
    age = 19
    fav_num = 57 #Favorite Number
    result = fav_num/age
    print(f"My name is {name}")
    print(f"My favourite number is {fav_num}")
    print(f"I am {age} years old")
    print(f"Here is some math: {fav_num}/{age} is {result}")
    

def print_sum():
    """
    Thuis function is used to calculate and print the sum of 23.2 and 82.4
    """    
    result = 23.2 + 82.4
    print(result)
    

def func (n: int):
    if n != -9:
        print('D')
        if n < 4:
            print('M')
    else:
        print('Z')
    print("/~~~~~~~~\\")



func('i')

    