#!/usr/bin/python3.9 # This program computes square root of x # import os import pandas as pd
import math

def product(op1, op2) :
    return (op1 * op2)

def quotient(numer, denor):
    return ( numer / denor )

def showans (ans) :
    print ("the answer is ", ans )

operation = input ("would u like a (p)roduct or (q)uotient? ")
if operation == "p" :
    print ("you have asked for product")
    op1 = input ("what is the 1st operand? ")
    op2 = input ("what is the 2nd operand? ")
    ans = product (float(op1), float(op2))
    showans (ans)
elif operation == "q" :
    print ("you have asked for quotient")
    numer = input ("what is the numerator? ")
    denor = input ("what is the denominator? ")
    ans = quotient (float(numer), float(denor))
    showans (ans)
else :
    print ("you have entered an invalid response")

