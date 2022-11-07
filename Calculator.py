#!/usr/bin/env python
# Peri
# 2021.11.03
# Lab Exercise 4
# Calculator.py
# Using Mu 1.1.0.beta.3
# This program asks a user for two numbers and an operation
# and displays the results.

def calculator():
    # Ask user for operation
    operation = input("Please select one option: add/subtract/multiply/divide ")
    # Check if input is valid
    if operation.lower() in("add", "subtract", "multiply", "divide"):
        print("You chose to", operation.lower())
        # Ask for numbers
        first_num = float(input("What is the first number? "))
        second_num = float(input("What is the second number? "))
        # Decide which operation to do
        if operation.lower() == "add":
            print(first_num, "+", second_num, "=", first_num + second_num)
        elif operation.lower() == "subtract":
            print(first_num, "-", second_num, "=", first_num - second_num)
        elif operation.lower() == "multiply":
            print(first_num, "*", second_num, "=", first_num * second_num)
        elif operation.lower() == "divide":
            # Catch a divide by zero error
            ## I learned this in my last semester course
            try:
                (first_num, "/", second_num, "=", first_num / second_num)
            except ZeroDivisionError:
                print("You can't divide by zero!")
                calculator()
    else:
        print("The option you chose (",operation.lower(),") is not valid.")
        print("Please try this program again.")
        calculator()

def again():
    # Ask user if they'd like to do another equation
    again = input("Do you want to do another? (Y/N) ")
    # Check if input is valid
    if again.lower() in("y", "n", "yes", "no"):
        if again.lower() in("y", "yes"):
            calculator()
        elif again.lower() in("n", "no"):
            print("Goodbye!")
    else:
        ## This throws an error if I enter an invalid character
        ## instead of prompting me to enter something valid ( ಠ ͜ʖಠ)
        print("The option you chose (",again.lower(),") is not valid.")
        again()

def main():
    ## I can't get this to repeat more than once?? (￣ε￣)
    calculator()
    again()

if __name__ == "__main__":
    main()