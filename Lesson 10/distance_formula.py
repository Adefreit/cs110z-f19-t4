import math

def distance_formula(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

# Here is some code to test the distance formula
# NOTICE HOW IT IS BELOW THE FUNCTION?  You need to define the
# function before you can use it!
x_coord_1 = 0
y_coord_1 = 0
x_coord_2 = 10
y_coord_2 = 0

d = distance_formula(x_coord_1, y_coord_1, x_coord_2, y_coord_2)
print(d)