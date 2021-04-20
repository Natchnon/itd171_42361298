def insertionSort(myList):
    for index in range(1, len(myList)):
            key = myList[index]
            temp = index - 1      
            while temp >= 0 and key < myList[temp]:
                myList[temp + 1] = myList[temp]
                temp = temp - 1
            myList[temp + 1] = key
n = int(input('โปรดระบุขนาดของ List : '))
myList = []*n
print('โปรดป้อนข้อมูลที่จัดเก็บใน List')
myList = [(int(input('Input : '))) for x in range(n)]
print('ข้อมูลที่จัดเก็บใน List ก่อนเรียงลำดับจากน้อยไปมาก คือ\n',*myList,end='')
insertionSort(myList)
print('\nข้อมูลที่จัดเก็บใน List ที่เรียงลำดับข้อมูลจากน้อยไปมากด้วยขั้นตอนวิธีแบบ insertion Sort คือ\n',*myList,end='')