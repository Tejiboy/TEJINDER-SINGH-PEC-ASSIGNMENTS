import math

def triangle_area(a, b, c):
    # calculate the semi-perimeter
    s = (a + b + c) / 2

    # apply Heron's formula
    area = math.sqrt(s * (s-a) * (s-b) * (s-c))
    
    # check for impossible sides
    if (area > 0) and (a + b > c) and (b + c > a) and (c + a > b):
        return area
    else:
        return "Impossible combination of sides"

# Input from user
a = float(input("Enter side 1: "))
b = float(input("Enter side 2: "))
c = float(input("Enter side 3: "))

# Function call
print("Area of triangle: ", triangle_area(a, b, c))
