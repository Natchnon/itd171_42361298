myStack = []*6
string = '---------------------------------------------------------------'

def isEmpty(myStack):
    if len(myStack) == 0:
        print('{}\nstack empty !\n{}'.format(string,string))
        return True
    else:
        return False

def isFull(myStack):
    if len(myStack) == 6:
        print('{}\nstack full\n{}'.format(string,string))
        return True
    else:
        return False

def push(item,myStack):
    status = isFull(myStack)
    if status == True:
        print("{}\ncan't push\n{}".format(string,string))
    else:
        myStack.append(item)

def pop(myStack):
    status = isEmpty(myStack)
    if status == True:
        print("{}\ncan't pop\n{}".format(string,string))
    else:
        myStack.pop()

def display(myStack):
    status = isEmpty(myStack)
    if status == True:
        print("{}\ncan't display min max\n{}".format(string,string))
    else:
        print(min(myStack),max(myStack))

while True:
    choice = int(input('1.push\n2.pop\n3.display min max\nplease input what u want : '))
    if choice == 1:
        item = int(input("number : "))
        push(item,myStack)
        print(string)
    elif choice == 2:
        pop(myStack)
        print(string)
    elif choice == 3:
        display(myStack)
        print(string)
    else:
        break