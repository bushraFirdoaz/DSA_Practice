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
def printout(head):
    curr = head
    while curr is not None:
        print(curr.data, end="->")
        curr = curr.next
    print("None")
def delete(head,i):
    if i==0:
        return head.next
    curr = head
    prev = None
    cnt =0
    while curr is not None and cnt <i:
        prev = curr
        curr = curr.next
        cnt +=1
    prev.next = curr.next
    return head
head = takeinput()
i = int(input())
head = delete(head, i)
printout(head)
