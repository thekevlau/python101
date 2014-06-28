#trie

class trie:
	class __node:
		def __init__(self, value):
			#store the string
			self.value = value
			#maps an edge (char) to a child node
			self.dict={}
			#this would need to be a dynamically sized array...
			#self.pointer = pointer[]
		#implement pointers using linkedlist?	
		
		def __str__(self):
			resultString = self.value
			#while not null, traverse
			#when you get to the null char, return the word at that value
			#while char in self.dict != None:
				#next			

			#if its not in the keys list, return
			if (not self.dict.keys()):
				return resultString
			#
			resultString=resultString + "\n Connected to: "
			for char in self.dict.keys():
				resultString = resultString + char + "\t"
			return resultString


		def getValue(self):
			return self.value

		def getDict(self):
			return self.dict

		def setNext(self, char, node):
			self.dict[char]=node

		def getNext(self, char):
			if (char in self.dict):
				return self.dict[char]


	
	def __init__(self, words):

		self.startNode = trie.__node("")
		for word in words:
			currNode = self.startNode
			for char in word:
				prevNode = currNode
			##dont get it
				if (not prevNode.getNext(char)):
					currNode = Node(prevNode.getstring()+char)
					prevNode.setNext(char, currNode)
				else:
					currNode=prevNode.getNext(char)

	#method returns if string is present in trie or not
	def wordStartsWith(self, string):
		currNode = self.startNode
		#direct comparison against 
		for letter in string:
			if (not currNode.getNext(letter)):
				return False
			else:
				currNode = currNode.getNext(letter)
		return True

	


















