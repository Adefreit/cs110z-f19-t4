import math

# This version of the distance formula just calculates the answer
def distance_formula_v1(x1, y1, x2, y2):
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)

# This version of the distance formula RETURNS the answer
def distance_formula_v2(x1, y1, x2, y2):
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return distance

print(distance)
    
