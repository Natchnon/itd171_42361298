class circularQueue:
    def __init__(self, n):
        self.n = n
        self.queue = [None] * n
        self.front = -1
        self.rear = -1



    def enqueue(self):
        if (self.rear+1)% self.n == self.front:
            print('Circular queue เต็ม')
        else:     
            if self.front == -1:         
                item = (input("please input Item : "))      
                self.rear = self.rear + 1
                self.queue[self.rear] = item
                self.front = 0
            else:              
                item = (input("please input Item : "))
                self.rear = (self.rear + 1)% self.n
                self.queue[self.rear] = item



    def dequeue(self):
        if (self.front == -1):
            print('ไม่สามารถดึงข้อมูลจาก Circular queue ได้เพราะ Circular queue ว่าง')
        else:
            if self.front == self.rear:
                self.queue[self.front]= '-'                
                self.front = -1
                self.rear = -1 
            else: 
                self.queue[self.front]= '-'
                self.front = (self.front+1) % self.n      



    def display(self):
        if(self.front == -1):
            print('No element in the circular queue')
        else:         
            for i in range(0, self.n):
                if self.queue[i] == None:
                    print(' - ', end = " ")
                else:
                    print(self.queue[i], end = " ")
            print( ) 



    def nextList(self):
        if (self.front == -1):
            print('ไม่สามารถดึงข้อมูลจาก Circular queue ได้เพราะ Circular queue ว่าง')
        else:
            print('รายชื่อคนต่อไป {}'.format(self.queue[self.front]))
n = int(input("โปรดระบุขนาดของ circular Queue : "))
q = circularQueue(n)



while True:
    print("""โปรดระบุทางเลือกในการดำเนินการกับ circular Queue
1. enqueue: รับข้อมูลชื่อลูกค้าเก็บใน circular queue
2. dequeue: ลบข้อมูลชื่อลูกค้าจาก circular queue 1 ราย
3. display: แสดงข้อมูลชื่อลูกค้าที่จัดเก็บทั้งหมดใน circular queue ทางจอภาพ
4. แสดงข้อมูลชื่อลูกค้ารายต่อไปทางจอภาพ""")
    choice = int(input("ทางเลือกในการดำเนินการ : "))
    if choice == 1:
        q.enqueue()
    elif choice == 2:
        q.dequeue()
    elif choice == 3:
        q.display()
    elif choice == 4:
        q.nextList()
    else:
        print("สิ้นสุดการทำงาน")
        break
