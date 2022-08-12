'''
อยากให้นักศึกษาช่วยหาลำดับการ Countdown จาก Input ที่รับเข้ามา โดยลำดับการ Countdown จะเป็นเลขเรียงลำดับ เช่น 2->1 , 3->2->1 โดยจะสิ้นสุดด้วย 1 เสมอ

โดยผลลัพธ์ให้แสดง List ของ จำนวนลำดับที่เจอ และ แต่ละลำดับเป็นอย่างไร
'''
print("*** Fun with countdown ***")
List = list(map(int,input("Enter List : ").split()))
ListInside = list() 
List2 = list()
result = []
i = 0
temp = List[0]
while i != len(List):
    if temp == List[i]:
        temp -= 1
        ListInside.extend(str(List[i]))
    else:
        temp = List[i]
        i -= 1
        ListInside = []

    
    if temp == 0:
        ListInside = [int(i) for i in ListInside]
        List2.append(ListInside)
        ListInside = []

    i += 1
result.append(List2)
result.insert(0,len(List2))
print(result)