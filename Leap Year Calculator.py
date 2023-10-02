#!/usr/bin/env python 3

Year = int(input("Which year do you want to check? "))
if Year % 4 == 0:
    if Year % 100 == 0:
        if Year % 400 == 0:
            print("Leap Year")
        else:
            print("Not a Leap Year")
    else:
        print("Leap Year")
else:
    print("Not a Leap Year")
