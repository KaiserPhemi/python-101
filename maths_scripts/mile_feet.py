# This program in Python3 calculates and prints the number of feet in 13 miles

feet_in_mile = 5280

mile_value = float(input("Kindly supply the value in miles: "))

def mile_to_feet(mile_value):

	return feet_in_mile * mile_value

print("Total value of "+str(mile_value)+" miles in feets is "+str(mile_to_feet(mile_value)))
print("")