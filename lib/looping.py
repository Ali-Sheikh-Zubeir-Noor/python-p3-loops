#!/usr/bin/env python3

def happy_new_year():
    for count in range (10, 0 , -1):
        print (count)
        print("Happy New Year!")

    

def square_integers(int_list):
    int_list = [int * int for int in int_list]
    return int_list
    


def fizzbuzz():
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0 :
            print("FizzBuzz")
        elif number % 3 == 0 :
            print ("Fizz")
        elif number % 5 == 0 :
            print ("Buzz")
        else :
            print(number)
        

