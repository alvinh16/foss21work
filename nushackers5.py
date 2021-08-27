#!/usr/bin/python3.9

a = input("watt is the number?")

print ("the number is ", a)

if (int(a) % 15 == 0) :
    print ("fizzbuzz")
elif (int(a) % 5 == 0) :
    print ("Buzz")
else :
    print ("the number is ", a)
