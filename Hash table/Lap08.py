Keys = [None]*11

while True:
    key = int(input('โปรดป้อนค่า (Key) ที่มีค่ามากกว่าหรือเท่ากับ 0 : '))
    item = input('โปรดป้อนข้อมูล (Name) ชื่อพนักงานเพื่อจัดเก็บข้อมูลในตารางแฮช : ')
    if key <= -1 :
        break
    else:
        address = key % 11
        if Keys[address] == None:
            Keys[address] = item
            print('address = ', address)
        else:
            i = 1
            while True:
                address = ((key+(i**2))%11)
                if Keys[address] != None: 
                    i += 1
                    continue
                else:
                    Keys[address] = item
                    print('address = ',address)
                    break

print('index ที่มีการจัดเก็บในตารางแฮช')
for i,x in enumerate(Keys):
    print(f"Index = {i},ข้อมูลที่จัดเก็บคือ {x if x != None else ' '}")
