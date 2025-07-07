import doctest

def print_name_age_v1():
    """ This function will let the user input an age and a name, then print
    hello follow with their name and word based on an age
    """
    y = input("name: ")
    x = int(input("age: "))
    if(x<18):
        print("hello", y, "child")
    elif(x >= 18 and x <= 64):
        print("hello", y, "adult")
    elif(x >= 65):
        print("hello", y, "senior")
        

def print_name_age_v2():
    """ This function will let the user input an age and a name, then print
    hello follow with their name and word based on an age but this time it will
    repeat to ask an age if the number is invalid
    """
    y = input("name: ")
    x = input("age: ")
    
    if not x.isdigit() or int(x) < 0:
        print(y, 'you are lying about your age')
    else:
        x = int(x)        
        if (x<18):
            print("hello", y, "child")
        elif(x >= 18 and x <= 64):
            print("hello", y, "adult")
        elif(x >= 65):
            print("hello", y, "senior")        
            

def get_num(mini: int, prompt: str) -> int:
    """ This function will take minimum value and prompt as string to ask the user
    to input a number, then it will repeat to ask until user input a valid age
    that is more than minimum value
    """
    x = input(prompt)
    
    while not x.isdigit() or int(x) < mini:
        x = input(prompt)
    
    return int(x)
    
def print_name_age_v3():
    y = input("name: ")
    x = get_num(0, "")
    
    if(x<18):
        print("hello", y, "child")
    elif(x >= 18 and x <= 64):
        print("hello", y, "adult")
    elif(x >= 65):
        print("hello", y, "senior")    
    
            

    