PI = 3.14

#Credit for both pics https://www.asciiart.eu/comics
"""
#Queston 1
#Print the logo of Superman
"""
def Superman():
    print("""
  ________________
 /.,------------,.\ 
///  .=^^^^^^^\__|\\ 
\\\   `------.   .//
 `\\`--...._  `;//'
   `\\.-,___;.//'
     `\\-..-//'
       `\\//'
        "" 
         """)
"""
#Print the logo of Batman
"""
def Batman():
    print("""
          _____       _____
     ,-'``_.-'` \   / `'-._``'-.
   ,`   .'      |`-'|      `.   `.
 ,`    (    /\  |   |  /\    )    `.
/       `--'  `-'   `-'  `--'       \
|                                   
\      .--.  ,--.   ,--.  ,--.      /
 `.   (    \/    \ /    \/    )   ,'
   `._ `--.___    V    ___.--' _,'
      `'----'`         `'----'`
          """)

#Superman()
#Batman()
"""
#Queston 2
#Print both logos with spacer line
"""
def print_logo():
    print("/~~~~~~~~\\")
    Superman()
    print("/~~~~~~~~\\")
    Batman()
    print("/~~~~~~~~\\")
    Superman()
    print("/~~~~~~~~\\")
    Batman()
    print("/~~~~~~~~\\")


#print_logo()
"""
#Queston 3
#Calculate the surface area of a cylinder 
"""
def calculate_surface_area(Height, Diameter):
    Radius = Diameter / 2
    Circumference = 2 * PI * Radius
    Wall = Circumference * Height
    Circle = PI * (Radius ** 2)
    Area = (Circle * 2) + Wall
    print(f"cylinder area: {round(Area,1)}")
    
#calculate_surface_area(1.2,3.5)
