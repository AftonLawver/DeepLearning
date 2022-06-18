import math


def degrees_to_radians(degrees:int):
    return (degrees * math.pi)/180

result = degrees_to_radians(90)
print(result)