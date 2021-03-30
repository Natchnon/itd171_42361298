Keys = [None]*13

while True:
    key = int(input("โปรดป้อมค่า Key ที่มีจำนวนเต็มบวก : "))
    data = input('โปรดป้อนข้อมูล (data) ที่เป็นข้อความเพื่อจัดเก็บในตารางแฮช : ')
    print('')
    if key <= -1 :
        break
    else:
        address = key%13
        if Keys[address] != None:
            print('จัดเก็บข้อมูลในตารางแฮชไม่ได้เพราะ Collistion')
        else:
            Keys[address] = data
print('index ที่มีการจัดเก็บในตารางแฮช')
for i in Keys:
    if i != None:
        print(f"Index = {Keys.index(i)} ข้อมูลที่จัดเก็บคือ {i}")