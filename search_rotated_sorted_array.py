#array of n integers; rotated an unknown number of times; find a given element in the array's index in the array
#assume it was initially sorted in ascending order and then rotated some unknown number of times


searching_for = 3
sample = [4, 5, 1, 2, 3]

#binary search tree. WHAT
#if the element to the left is greater, search it. (essentially find the one)

#divide into half. each of those is still sorted! 



def check(searching_for, sample):
	found = False
	start = 0
	end = len(sample)-1

	while not found:
		pivot = len(sample)/2
		index = start + pivot

		if sample[pivot] == searching_for:
			return pivot

		left = sample[:pivot]
		right = sample[pivot:]

		if searching_for >= left[0] and searching_for <= left[-1]:
			sample = left
			end = middle

		if searching_for >= right[0] and searching_for <= right [-1]:
			sample = right
			start = middle
		
		else:
			return -1

to_find = int(raw_input("number: "))
print check(to_find, [1, 2, 3, 4, 5])




#assuming chronologically ordered numbers (all of them):

if searching_for > sample[0]:
	print abs(sample[0]-searching_for)
if searching_for < sample[0]:
	print len(sample) - (sample[0]-searching_for)
