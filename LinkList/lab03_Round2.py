class Node:
    def __init__(self,info = None):
        self.info = info
        self.next = None

class SlinkedList:
    def __init__(self):
        self.head = None
        self.next = None

    def AtTheBegining(self, data):
        if self.head != None:
            NewNode = Node(data)
            NewNode.next = self.head
            self.head = NewNode
        else:
            NewNode = Node(data)
            NewNode.next = None
            self.head = NewNode
            self.tail = NewNode

    def AtTheEnd(self,data):
        if self.head == None:
            NewNode = Node(data)
            NewNode.next = None
            self.head = NewNode
            self.tail = NewNode
        else:
            NewNode = Node(data)
            NewNode.next = None
            self.tail.next = NewNode
            self.tail = NewNode

    def listPrint(self):
        i = 1
        Status = self.head
        print('='*30)
        print('head = ',self.head.info)
        while Status is not None:
            print('i = ',i,'info = ',Status.info)
            Status = Status.next
            i+=1
        print('tail = ',self.tail.info)
        print('='*30)

listA = SlinkedList()
listB = SlinkedList()

print("โปรดป้อนตัวแปรตัวเลขจำนวนเต็มเพื่อสร้าง Sigly Linked List A โดยโปรแกรมจะหยุดการวนซ้ำเมื่อตัวเลขำนวนที่ผู้ใช้ป้อนมีค่าเป็น 999")

while True:
    data = int(input("DataA = "))
    if data == 999:
        print("โปรดป้อนตัวแปรตัวเลขจำนวนเต็มเพื่อสร้าง Sigly Linked List B โดยโปรแกรมจะหยุดการวนซ้ำเมื่อตัวเลขำนวนที่ผู้ใช้ป้อนมีค่าเป็น 999")
        break
    else:
        listA.AtTheEnd(data)
while True:
    data = int(input("DataB = "))
    if data == 999:
        while listA.head:
            temp = listA.head.info
            listB.AtTheBegining(temp)
            listA.head = listA.head.next
        listB.listPrint()
        break
    else:  
        listB.AtTheEnd(data)
