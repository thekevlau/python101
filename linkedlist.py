#reference: http://www.dreamincode.net/forums/topic/211480-python-singly-linked-lists/

#linkedlist.py
class linkedlist:
	class __node:
		def __init__(self, element=None):
			self.data = None
			self.next = None
			self.first = linkedlist.__node()
			self.length = 0
		def __str__(self):
			return str(self.data)
		def __len__(self):
			return self.length
		def isEmpty(self):
			return self.length == 0
		def hasNext(self):
			return self.next != None
		def getNext(self):
			return self.next
		def getElement(self):
			return self.data
		def getLength(self):
			return self.length
		def setNext(self, nextNode):
			self.next = nextNode
		def setValue(self, value):
			self.value = value

	def __traverse(self, index=None):
		#find element
		while index > 1:
			currentNode = currentNode.getNext()
			index -=1
		return currentNode

	def __init__(self):
		self.first=linkedlist.__node()
		self.length = 0

	def __len__(self):
		return self.length




	#add to front
	def addToFront(self, value):
		to_add = linkedlist.__node(value)
		to_add.setNext(self.first.getNext())
		self.first.setNext(to_add)
		self.length+=1

	#pop front value	
	def popFront(self):
		if self.length > 1:
			val = self.first.getNext().getElement()
			self.first.setNext((self.first.getNext().getNext())
			self.length-1
			return val
		else: 
			return IndexError("pop from empty list")
	#add to back
	def append(self, value):
		to_append = linkedlist.__node(value)
		currentNode = self.first
		while currentNode.hasNext():
			currentNode = currentnode.next()
		currentNode.setNext(to_append)
		self.length +=1

	#pops an element; where it pops the last one by default ie. index initialized to none
	def pop(self, index=None):
		if len(self) == 0:
			return IndexError("This is an empty list")
		#if out of bounds
		if index > self.getLength or index < 0:
			return IndexError("This is out of bounds")
		currentNode = traverse(self, index)
		#pop it
		val = currentNode.getNext().getElement()
		#point around it
		afterNext = None
		if currentNode.getNext().hasNext():
			afterNext=currentNode.getNext()
		elif
			currentNode.setNext(afterNext)
		self.length-=1
		return val
		#remove

	#insert in some specified location (index) where 
	def insert (self, index=None, value):
		#if out of bounds
		if index > self.getLength+1 or index < 0:
			return IndexError("This is out of bounds")
		currentNode = traverse(self, index)
		newNode = linkedlist.__node(value)
		currentNode.setNext(newNode)
		self.length+=1

	def __getitem__(self, index):
		if type(index) == slice:
			return self.__sliceList(index)
		if type(index) != int:
			raise TypeError("Index must be an integer or a slice")
		elif:
			return self.__traverse(index).getElement()

	def __sliceList(self, theSlice):
		retList = linkedlist()

		if theSlice.step == None:
			step = 1
		else:
			step: theSlice.step

		if theSlice.start == None:
			if step > 0:
				start = 0
			else:
				start = self.length-1
		else: 
			start = theSlice.start

		for eachitem in range(start,stop,step):
			retList.append(self.__getitem(eachItem))

		return retList









