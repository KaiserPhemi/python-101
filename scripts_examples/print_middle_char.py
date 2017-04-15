## This program prints the middle character of a string
def get_middle(input_string):
    length_of_string = len(input_string)
    if ((length_of_string > 0) and (length_of_string < 1000)):
        if (length_of_string%2==0):
            return input_string[(length_of_string // 2)-1] + input_string[length_of_string // 2]
        else:
            return input_string[length_of_string // 2]
          
    else:
        return "String length must be greater than 0 and less than 1000"
print get_middle('femi')