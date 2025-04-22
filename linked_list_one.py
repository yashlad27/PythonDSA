class Node:
	""" A node in a linked list """
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	""" A singly linked list implementation """
	def __init__(self):
		self.head = None

	def append(self, data):
		""" Add a new node with the given data to the end of the list """
		new_node = Node(data)

		# if the list is empty, make the new node the head
		if not self.head:
			self.head = new_node
			return

		# otherwise traverse to the end and append
		current = self.head
		while current.next:
			current = current.next
		current.next = new_node

	def prepend(self, data):
		""" Add a new node with given data to the beginning of the list """
		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node

	def delete(self, data):
		""" Delete the first node with the given data """
		if not self.head:
			return 

		# if head is the node to delete
		if self.head.data == data:
			self.head = self.head.next
			return 

		# search for the node to delete
		current = self.head
		while current.next and current.next.data != data:
			current=current.next

		# if found, delete it
		if current.next:
			current.next = current.next.next

	def display(self):
		""" Print the linked list """
		elements = []
		current = self.head
		while current:
			elements.append(current.data)
			current = current.next
		return elements

# usage:
ll = LinkedList()
ll.append(1)
ll.append(3)
ll.append(5)
ll.append(7)
ll.append(9)
ll.append(0)

print(f"Linked list: {ll.display()}")

ll.delete(5)
print(f"After deleting 5: {ll.display()}")
