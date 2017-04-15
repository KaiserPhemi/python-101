"""Create both a recursive function called recursive_factorial and iterative function called iterative_factorial that does the following
Accepts as parameter an Integer n
Computes the factorial of n
Returns the factorial of n
"""

"""RECURSIVE LAB"""

print "This program calculates the factorial of a  number recursively"
num = int(raw_input("Please enter a number: "))
   
def recursive_factorial(num):
    if num == 0:
        return 1
  
    else:
        return num * recursive_factorial(num-1)
print recursive_factorial(num)


"""ITERATIVE LAB"""

print "This program calculates the factorial of a  number Iteratively"

numb = int(raw_input("Please enter a number: "))

def iterative_factorial(numb):
  result = 1
  
  if numb < 0:
    print("Factorial does not exist for negative numbers")
    
  elif numb ==0:
    return result
    
  else:
    while numb >=1:
      result = result * numb
      numb= numb-1
    return result
print iterative_factorial(numb)
