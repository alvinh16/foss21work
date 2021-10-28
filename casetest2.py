#!/usr/bin/python3.9
# This program computes square root of x # import os import pandas as pd
# import math

def dow (designate):
    switcher = {
        0: "sunday",
        1: "monday",
        2: "tuesday",
        3: "wednesday",
        4: "thursday",
        5: "friday",
        6: "saturday"
    }
    return switcher.get(designate, "invalid day of week")

daynum = input("please give day 0-6 ")
print ("you have given, ", daynum,  dow (int(daynum)))


