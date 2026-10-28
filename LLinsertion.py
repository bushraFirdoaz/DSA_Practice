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
def length(head):
    cnt =0
    curr = head
    while curr is not none:
        cnt +=1
        curr = curr.next
    return cnt
def insert(head, i, data):
    if i<0 and i>length(head):
        return head
    newNode = Node(data)

    if i==0:
        newNode.next = head
        return newNode
    cnt =0
    curr = head
    while cnt<i-1:
        
        curr = curr.next
        cnt+=1
    newNode.next = curr.next
    curr.next = newNode

    return head
def printout(head):
    curr = head
    while curr is not None:
        print(curr.data, end="->")
        curr = curr.next
    print("None")
head = takeinput()
i, data = map(int, input().split())
head = insert(head, i, data)
printout(head)
