import math
polygon =int(input("Enter the number of sides on the polygon:"))
sides =int(input("Enter the length of one of the sides:"))
area = (polygon * sides**2)/(4*math.tan(3.14/polygon))
print(area)