def shellsort(myList):
    gapSize = 7 // 2
    while gapSize > 0:
        for i in range(gapSize,7):
            temp = myList[i]
            x = i
            while x >= gapSize and myList[x - gapSize] > temp:
                myList[x] = myList[x - gapSize]
                x -= gapSize
            myList[x] = temp
        gapSize //= 2
print('โปรดป้อนข้อมูลการจัดเก็บใน List')
myList = [(int(input('Input : '))) for x in range(7)]
print('\nข้อมูลที่จัดเก็บใน List ก่อนเรียงลำดับจากน้อยไปมาก คือ\n',*myList)
shellsort(myList)
print('\nข้อมูลที่จัดเก็บใน List ที่เรียงลำดับข้อมูลจากน้อยไปมากด้วยขั้นตอนวิธีแบบ Shell Sort คือ\n',*myList)
