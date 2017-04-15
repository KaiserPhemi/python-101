# This program calculates the area of a triangle base on the Heron formula

side_a = float(input("Please enter the value for side 'a':"))
side_b = float(input("Please enter the value for side 'b':"))
side_c = float(input("Please enter the value for side 'a':"))
print("")
def heron_area(side_a, side_b, side_c):
	semi_peri = (side_a + side_b + side_c)/2

	h_area = (semi_peri*(semi_peri-side_a)*(semi_peri-side_b)*(semi_peri-side_c))**(1/2)

	return h_area

print("Area of triangle using Heron formula is "+str(heron_area(side_a, side_b, side_c)))
print("")