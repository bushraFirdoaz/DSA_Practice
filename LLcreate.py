class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def takeinput():
    ipl = list(map(int, input().split()))
    head = None
    tail = None
    for data in ipl:
        if data ==-1:
            break
        newNode = Node(data)
        if head is None:
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = newNode
            
    return head
def printout(head):
    curr = head
    while curr is not None:
        print(curr.data, end="->")
        curr = curr.next
    print("None")
head = takeinput()
printout(head)