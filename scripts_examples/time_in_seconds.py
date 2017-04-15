# This program expreses time in seconds only. Input is in hours, minutes and seconds

print("This program expreses time in seconds only. Input is in hours, minutes and seconds.")
print("")
hour_time = float(input("Kindly input time in hours and hit 'Enter': "))
print("")
min_time = float(input("Input the minutes value and hit 'Enter': "))
print("")
sec_time = float(input("Input the seconds value and hit 'Enter': "))

def time_conv(hour_time, min_time, sec_time):
	time_sec = ((hour_time * 3600)+(min_time*60)+sec_time)

	return time_sec

print(str(hour_time)+" hours, "+str(min_time)+" minutes, "+str(sec_time)+" seconds is "+str(time_conv(hour_time, min_time, sec_time))+" seconds expressed in seconds")