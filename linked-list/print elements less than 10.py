#print elements less than 10 using a linked list 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

n1 = Node(5)
n2 = Node(3)
n3 = Node(6)
n4 = Node(11)
n5 = Node(12)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
temp = n1
while temp:
    if temp.data<10:
        print(temp.data, end=" → ")
    temp = temp.next

print("None")
