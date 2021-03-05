class queue:
    def __init__(self,n):
        self.n = n
        self.queue = [0] * n
        self.front = -1
        self.rear = -1



    def enQueue(self):
        if self.rear == self.n-1:
            print("full Queue")
        else:
            if self.front == -1:
                item = int(input("please input Item : "))
                self.front = 0
                self.rear = 0
                try:
                    self.queue[self.rear] = item
                except :
                    print("can't")
                
            else:
                item = int(input("please input Item : "))
                try:
                    self.queue[self.rear+1] = item
                    self.rear = self.rear + 1
                except :
                    print("can't")



    def deQueue(self):
        if self.rear-self.front+1 < 1:
            print("Free space Queue")
        else:
            if self.front == self.rear:
                self.queue.clear()
                self.front = -1
                self.rear = -1
                print("Free space Queue")
            else:
                self.queue[self.front] = 0
                self.front = self.front + 1



    def display(self):
        if self.front == -1:
            print("No element to show")
            print('front = ',self.front,', rear = ',self.rear)
        else:
            for i in self.queue:
                print(i)
            print('front = ',self.front,', rear = ',self.rear)
    
    
    def final(self):
        total = 0
        i = 0
        average = 0
        for x in self.queue:
            if x != 0:
                total = total + x
                i += 1
        average = total / i
        print("total = {}\nAverage= {}".format(total,average))



n = int(input("โปรดระบุขนาดของ Queue : "))
q = queue(n)
line = "----------------------------------------------------------------"



while True:
    print("โปรดระบุทางเลือกในการดำเนินการกับ Queue\n1. enqueue: รับข้อมูลจำนวนเต็มเก็บใน queue\n2. dequeue: ดึงข้อมูลจาก queue 1 ช่อง\n3. display: แสดงข้อมูลที่จัดเก็บทางจอภาพ\n{}".format(line))
    choice = int(input("ทางเลือกในการดำเนินการ : "))
    if choice == 1:
        q.enQueue()
    elif choice == 2:
        q.deQueue()
    elif choice == 3:
        q.display()
    else:
        q.final()
        break