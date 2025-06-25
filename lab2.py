import math

"""
This function will print the longer word
"""
def print_longer(one: str, two: str):
    x = len(one)
    y = len(two)
    
    if(x >= y):
        print(one)
    elif(y > x):
        print(two)
    
"""
This function will print the real roots of the quadratic equation
"""
def print_real_roots(a: float, b: float , c: float):
    if a == 0 :
        print("ERROR")
    elif (b**2) - (4 * a * c) < 0 :
        print("NO REAL ROOTS")
    else:
        x = (-b + (math.sqrt((b**2) - (4 * a * c))))/(2*a)
        y = (-b - (math.sqrt((b**2) - (4 * a * c))))/(2*a)
        print(f"{x:.3f}, {y:.3f}")
    
    

"""
This function will print the zodiac sign according to Month and Day
"""
def print_zodiac_sign(Month: str, day: int):
    if((Month == 'January' and day >= 20) or (Month == 'February' and day <=18)):
        print("Aquarius")
    elif((Month == 'February' and day >= 19) or (Month == 'March' and day <=20)):
        print("Pisces")
    elif((Month == 'March' and day >= 21) or (Month == 'April' and day <=19)):
        print("Aries")
    elif((Month == 'April' and day >= 20) or (Month == 'May' and day <=20)):
        print("Taurus")
    elif((Month == 'May' and day >= 21) or (Month == 'June' and day <=20)):
        print("Gemini")
    elif((Month == 'June' and day >= 21) or (Month == 'July' and day <=22)):
        print("Cancer")
    elif((Month == 'July' and day >= 23) or (Month == 'August' and day <=22)):
        print("Leo")
    elif((Month == 'August' and day >= 23) or (Month == 'September' and day <=22)):
        print("Virgo")
    elif((Month == 'September' and day >= 23) or (Month == 'October' and day <=22)):
        print("Libra")
    elif((Month == 'October' and day >= 23) or (Month == 'November' and day <=21)):
        print("Scorpio")
    elif((Month == 'November' and day >= 22) or (Month == 'December' and day <=21)):
        print("Sagittarius")
    elif((Month == 'December' and day >= 22) or (Month == 'January' and day <=19)):
        print("Capricorn")
    else:
        print("Invalid Input")