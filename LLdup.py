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
def duplicate(head):
    t1 = head
    while t1:
        t2 = t1.next
        while t2 and t1.data == t2.data:
            t2 = t2.next
        t1.next = t2
        t1 = t2
    return head
def printout(head):
    curr = head
    while curr is not None:
        print(curr.data, end="->")
        curr = curr.next
    print("None")
head = takeinput()
head = duplicate(head)
printout(head)