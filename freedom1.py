#!/usr/bin/python3.9
# This program computes square root of x # import os import pandas as pd
# import math

def freedom (designate):
    switcher = {
        0: "The freedom to run the program as you wish, for any purpose",
        1: "The freedom to study how the program works, and change it so it does your computing as you wish",
        2: "The freedom to redistribute copies so you can help others",
        3: "The freedom to distribute copies of your modified versions to others",
    }

    return switcher.get(designate, "no more freedoms!!")

freenum = input("please give day 0-3 ")
print ("you have given, ", freenum,  freedom (int(freenum)))


