inp_num = int(input("Please enter a number: "))


def prime_check(inp_num):
	p_check = (inp_num**2)+inp_num+41

	if(p_check % 2 == 0):

		return (str(p_check)+" is not a prime number")
	
	else:
		return (str(p_check)+" is a prime number")

print(prime_check(inp_num))