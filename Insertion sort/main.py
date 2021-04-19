n = int(input('โปรดระบุขนาดของ List : '))
myList = []*n

print('โปรดป้อนข้อมูลที่จัดเก็บใน List')

for x in range(n):
    myList.append(int(input('Input : ')))

print('ข้อมูลที่จัดเก็บใน List ก่อนเรียงลำดับจากมากไปน้อย คือ')

for x in myList:
    print(x,end=' ')
print(' ')

def insertionSort(myList):
    for index in range(1, len(myList)):
            key = myList[index]
            temp = index - 1      
            while temp >= 0 and key < myList[temp]:
                myList[temp + 1] = myList[temp]
                temp = temp - 1
            myList[temp + 1] = key

insertionSort(myList)
print('ข้อมูลที่จัดเก็บใน List ที่เรียงลำดับข้อมูลจากมากไปน้อยด้วยขั้นตอนวิธีแบบ insertion Sort คือ')
for x in myList:
    print(x,end=' ')