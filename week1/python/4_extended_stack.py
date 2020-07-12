#stack implementation from geeksforgeeks
# 
#  Class to make a Node 
class Node: 
	#Constructor which assign argument to nade's value 
	def __init__(self, value): 
		self.value = value 
		self.next = None
	

class Stack: 
	# Stack Constructor initialise top of stack and counter. 
	def __init__(self): 
		self.top = None
		self.count = 0
		self.maximum = None
		
	def getMax(self): 
		if self.top is None: 
			return "Stack is empty"
		else: 
			print(self.maximum)



	# Method to check if Stack is Empty or not 
	def isEmpty(self): 
		# If top equals to None then stack is empty 
		if self.top == None: 
			return True
		else: 
		# If top not equal to None then stack is empty 
			return False

	# This method returns length of stack	 
	def __len__(self): 
		self.count = 0
		tempNode = self.top 
		while tempNode: 
			tempNode = tempNode.next
			self.count+=1
		return self.count 

	# This method returns top of stack	 
    
	#This method is used to add node to stack 
	def push(self,value): 
		if self.top is None: 
			self.top = Node(value) 
			self.maximum = value 
			
		elif value > self.maximum : 
			temp = (2 * value) - self.maximum 
			new_node = Node(temp) 
			new_node.next = self.top 
			self.top = new_node 
			self.maximum = value 
		else: 
			new_node = Node(value) 
			new_node.next = self.top 
			self.top = new_node 
		#print("Number Inserted: {}" .format(value)) 
	
	#This method is used to pop top of stack 
	def pop(self): 
		if self.top is None: 
            
			print( "Stack is empty") 
		else: 
			removedNode = self.top.value 
			self.top = self.top.next
			if removedNode > self.maximum: 
				#print ("Top Most Element Removed :{} " .format(self.maximum)) 
				self.maximum = ( ( 2 * self.maximum ) - removedNode ) 
			

				
			
	
# Driver program to test above class 
stack = Stack() 

for _ in range(int(input())):
    q = input().split()

    if q[0]=='max':
        stack.getMax()
    elif q[0]=='push':
        stack.push(int(q[1]))
    else:
        stack.pop()