myStack = []


def isEmpty(myStack):
    if len(myStack) == 0:
        print('Stack is empty')
        return True
    else:
        return False



def isFull(myStack,capacity):
    if len(myStack) == capacity:
        print('Stack is full')
        return True
    else:
        return False



def push(item,myStack):
    boolean = isFull(myStack,capacity)
    if boolean == True:
        print("Push ไม่ได้ stack เต็ม")
    else:
        myStack.append(item)



def pop(myStack):
    boolean = isEmpty(myStack)
    if boolean == True:
        print("pop ไม่ได้เพราะ stack ว่าง")
    else:
        myStack.pop()



def topOfStack(myStack):
    boolean = isEmpty(myStack)
    if boolean == True:
        print("หาค่า top ไม่ได้เพราะ stack ว่าง")
    else:
        print(myStack[-1])


def display(myStack):
    print("ค่าทั้งหมดใน stack  : {}".format(myStack))



capacity = int(input("Stack size : "))
myStack = []*capacity

while True:
    choice = int(input("what do you want to do ?\n1.push : จัดเก็บข้อมูลใน Stack\n2.pop : ดึงข้อมูลที่จัดเก็บไว้ตำแหน่งบนสุดของ Stack ออก\n3.top of stack : แสดงข้อมูลที่ัดเก็บในตำแหน่งบนสุดของ Stack\n4.display : แสดงข้อมูลที่จัดเก็บใน Stack\n :: "))
    if choice == 1:
        item = int(input("ป้อนค่า Item ที่ต้องการ: "))
        push(item,myStack)
    elif choice == 2:
        pop(myStack)
    elif choice == 3:
        topOfStack(myStack)
    elif choice == 4:
        display(myStack)
    else:
        break