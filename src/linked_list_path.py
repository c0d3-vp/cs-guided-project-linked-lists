class LinkedListNode:
    # constuctor
    def _init_(self, value):
        self.value = value
        #t the "arrow"
        self.next = None

# initialize a few linkedlistNodes
x = LinkedListNode('X')
y = LinkedListNode('Y')
z = LinkedListNode('Z')

# connect the LinkedListNodes together
x.next = y
y.next = z

# define a function that prints every node in the linked list starting with the input nore
def print_ll(node):

    current = node
    while current is not None:
        print(curent.value)
        current = current.next
print_ll(y)