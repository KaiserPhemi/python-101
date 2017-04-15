#total_list = ['kaiser', 'phemi', 'olori', 'funke', 'femi', 'phemi', 'jide', 'lapasco', 'stinky', 'prolifik', 'emperor', 'femi', 'akinwa', 'segun', 'victor', 'kaiser', 'kaiser', 'femi', 'segun', 'victor'] 

#This creates a dictionary that finds the total occurence of a name in a list
def name_register(total_list):
	name_count_dict = {}
	for name in total_list:
		name_count_dict[name] = name_count_dict.get(name, 0)+1
		# if name not in name_count_dict:
		# 	name_count_dict[name] = 1
		# else:
		# 	name_count_dict[name] += 1
	return name_count_dict

## Builds a list of names from users input
def build_name_list():
	name_list = []
	name_input = ""

	length_of_list = int(raw_input("Enter length of name list: "))
	
	for length in range(length_of_list):
		name_input = str((raw_input("Enter name %s: " %(length+1))).strip())
		name_list.append(name_input)
	return name_list


print name_register(build_name_list())



