# implement algo to determine is a string has all unique chars.
#then do it wihtout additional data structures

str_array = [sa;fjasd;foaiejf]

#with other datastructure
def nonRepeating (str_array):
	new_array = [];
	for char in str_array:
		for char in new_array:
			if char is not in new_array:
				new_array.append(char);
			if char is in new_array:
				return false
	return true


#withonlyone...inplace?
def nonRepeating (str_array):
	#swap things around?
	#can't do a counter..
	#sort and 
	str_array.sort();
	for char in str_array:
		if char == char.next:
			return false
	return true


