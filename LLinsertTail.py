class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def created():
    ip = list(map(int, input().split()))
    head = None
    tail = None
    for data in ip:
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
def insert_tail(head, data):
    newNode = Node(data)
    if head is None:
        return newNode
    curr = head
    while curr.next is not None:
        curr = curr.next
    curr.next = newNode
    return head
def printout(head):
    curr = head
    while curr is not None:
        print(curr.data, end = "->")
        curr = curr.next
    print("None")
head = created()
printout(head)
data = int(input())
head = insert_tail(head, data)
printout(head)