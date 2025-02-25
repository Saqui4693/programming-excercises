# import necessary libraries
import math

def main():
    # ask the user to enter name and age
    name = input("Enter your Name: ")
    age = int(input("Enter your Age: "))  

    # print message with name and age
    print(f"Hello {name}, you are {age} years old.")

    # call function check age
    check_age(age)

    # calculate sum of numbers from 1 to age
    total_sum = sum_of_numbers(age)
    print(f"The total of all numbers from 1 to {age} is {total_sum}")

    # Ask for a number and check if it is even or odd
    num = int(input("Enter a number: "))
    result = even_or_odd(num)
    print(f"This number is {result}.")

# function to check if the user is 18 or older
def check_age(age):
    if age >= 18:  # check if the user is 18 or older
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote.")

# function to calculate the sum of all numbers from 1 to age
def sum_of_numbers(age):
    total = 0
    for i in range(1, age + 1):  # loop to iterate through the range of numbers
        total += i
    return total

# function to check if a number is even or odd
def even_or_odd(num):
    if num % 2 == 0:
        return "Even"  
    else:
        return "Odd"  

if __name__ == "__main__":
    main()
