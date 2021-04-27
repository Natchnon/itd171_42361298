class Node:
    def __init__(self):
        self.data = None
        self.leftChild = None
        self.rightChild = None


    def PreOrder(self,tree):
        if tree:
            print(tree.data, end = '  ')
            self.PreOrder(tree.leftChild)
            self.PreOrder(tree.rightChild)
    

    def PostOrder(self, tree):
        if tree:
            self.PostOrder(tree.leftChild)
            self.PostOrder(tree.rightChild)
            print(tree.data, end = '  ')


    def InOrder(self, tree):
        if tree:
            self.InOrder(tree.leftChild)
            print(tree.data, end = '  ')
            self.InOrder(tree.rightChild)

    
    def insert(self, data):
        if self.data == None:
            self.data = data
        elif data < self.data:
            if self.leftChild == None:
                self.leftChild  = Node()
                self.leftChild.data  = data
            else:
                self.leftChild.insert(data)
        elif data > self.data:
            if self.rightChild == None:
                self.rightChild  = Node()
                self.rightChild.data  = data
            else:
                self.rightChild.insert(data)


bst = Node()

myList = []
n = int(input('โปรดป้อนค่า n เพื่อใช้ในวนซ้ำรับจำนวนเต็ม\nn = '))
while len(myList)+1 != n:
    item = int(input('Number = '))
    if item in myList:
        print('ข้อมูลซ้ำ')
    else:
        myList.append(item)
        bst.insert(item)

print('ทางเลือกในการท่องไปในต้นไม้ค้นหาแบบทวิภาค\n1. แบบ Pre-Order\n2. แบบ In-Order\n3. แบบ Post-Order')
while True:
    choice = int(input('โปรดระบุทางเลือกในการท่องไปในต้นไม้แบบทวิภาค : '))
    if choice == 1:
        bst.PreOrder(bst)
        break
    elif choice == 2:
        bst.InOrder(bst)
        break
    elif choice == 3:
        bst.PostOrder(bst)
        break
    else:
        continue