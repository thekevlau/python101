#given a dictionary of words, and an input word, find the words that are up to one character off.
#assume position therefore also matters

WORDS = ["cat", "dog", "cot", "tat", "frog", "cast", "cottage"]
def search(input_word, delta):
	matched = []
	for word in WORDS:
		#if word is shorter by more than one letter 
		if len(word) < (len(check)-delta):
			break
		#check the input against each entry 
		x = 0
		y = 0
		diff = 0
		shorter_word_size = min(len(check), len(word))
		#keep checking as long as the difference is less than 2
		#and either word isn't "finished"
		while diff < delta+1 and ((x <= shorter_word_size) or (y <= shorter_word_size)):
			#if the character is the same, keep going
			if check[x] == word[y]:
				x=x+1
				y=y+1
			if check[x] != word[y]:
				diff=diff+1
				y=y+1
		if diff < delta+1:
			break
		#survived the test
		matched.append(word)
	return matched

check = raw_input("enter word to search: ")
print "you want to look for %r" %(check)
delta = int(raw_input("delta: "))
print "and other words at most off by %r" %(delta)
print search(check, delta)