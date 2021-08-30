#!/usr/bin/python3.9
# This program computes square root of x
import os
x = os.getcwd()
y= os.listdir()
z = len(y)

print ("the current working directory is : ", x)
# print ("the contents of this directory is", y)
for  n in range (0, z) :
    print (y[n])

print ("there are, ", str(z), " files.")
