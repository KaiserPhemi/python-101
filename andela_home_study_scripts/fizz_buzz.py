"""Create a function fizzBuzz to return 'Fizz', 'Buzz', 'FizzBuzz', or the argument it receives, 
all depending on the argument of the function, a number that is divisible by, 3, 5, or both 3 and 5, respectively.

When the number is not divisible by 3 or 5, the number itself should be returned.
"""
#FIZZBUZZ

print("")
print("This program prints 'Fizz' 'Buzz' or 'FizzBuzz' depending on the input")
print("")
print("")
number = int(input("Please enter a number that is a multiple of either 3 or 5: "))
print("")

"Code will run if input is a number"
try:
    def fizzbuzz(number):

        if number <= 0:
            return "Number must be greater than zero"

        elif number % 3 == 0 & number % 5 == 0:
            return 'FizzBuzz'

        elif number % 5 == 0:
            return 'Buzz'

        elif number % 3 == 0:
            return 'Fizz'

        else:
            return str(number) + " is not a multiple of 3 or 5"


    print(fizzbuzz(number))
    print("")

except ValueError:
    print("")
    print("Input is not a number. Please try again: ")
