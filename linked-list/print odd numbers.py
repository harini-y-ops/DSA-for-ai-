#Create a nodes and only print the odd numbers 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

n1 = Node(4)
n2 = Node(7)
n3 = Node(10)
n4 = Node(13)

n1.next = n2
n2.next = n3
n3.next = n4

temp = n1
while temp:
    if temp.data % 2 == 1:
        print(temp.data, end=" → ")
    
    temp = temp.next

print("None")
