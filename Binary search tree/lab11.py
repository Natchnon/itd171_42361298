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
    
    def findMaximumValue(self):
        if self.rightChild == None:
            return self.data
        return self.rightChild.findMaximumValue()
    
    def findMinnimumValue(self):
        if self.leftChild == None:
            return self.data
        return self.leftChild.findMinnimumValue()


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
mylist = []
print('โปรดป้อนข้อมูลจำนวนเต็ม 10 ตัวเพื่อจัดเก็บในต้นไม้ค้นหาแบบทวิภาค')
while len(mylist) < 10:
    data = int(input('Number: '))
    if data in mylist:
        continue
    else:
        bst.insert(data)
        mylist.append(data)
print('ผลลัพธ์จากการท่องไปในต้นไม้แบบทวิภาคแบบ Pre-order คือ' )
bst.PreOrder(bst)
print(f'\nจำนวนเต็มที่น้อยที่สุดที่จัดเก็บในต้นไม้คนหาแบบทวิภาคคือ {bst.findMinnimumValue()}')


