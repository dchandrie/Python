import math
a = float(input("Value of a : "))
b =float(input("Value of b : "))
c = float(input("value of c : "))
def quad():
    square_Value= b**2-4*a*c
    square_root = math.sqrt(square_Value)
    quad1 = (-b+square_root)/(2*a)
    quad2 = (-b-square_root)/(2*a)
    if square_Value <0:
        print("error: imaginary number",square_Value)
    else:
        print(quad1, quad2)
quad()