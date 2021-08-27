#!/usr/bin/python3.9

def hypotehnus (a, b) :
    asquare = a ** 2
    bsquare = b ** 2
    return ((asquare + bsquare) ** 0.5)

side1 = input ("please give side 1 of triangle ")
side2 = input ("please give side 2 of triangle ")
hyp = hypotehnus(float(side1), float(side2))
print ("the value of hypothenus is ", hyp)