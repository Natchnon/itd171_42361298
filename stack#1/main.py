myStack = []*8
total = 0

def isEmpty(myStack):
    if len(myStack) == 0:
        print('Stack is empty')
        return True
    else:
        return False



def isFull(myStack):
    if len(myStack) == 8:
        print('Stack is full')
        return True
    else:
        return False


def push(myStack):
    boolean = isFull(myStack)
    if boolean == True:
        print("can't push because is full ! ")
    else:
        myStack.append(item)

def pop(myStack):
    boolean = isEmpty(myStack)
    if boolean == True:
        print("can't pop because is empty ! ")
    else:
        myStack.pop()


while True:
    choice = int(input("what do you want to do\n1.Push\n2.pop\n::"))
    if choice == 1:
        item = int(input("please input Item : "))
        push(myStack)
    elif choice == 2:
        pop(myStack)
    else:
        for x in myStack:
            total = total + x
        print('total in my stack is {}'.format(total))
        break