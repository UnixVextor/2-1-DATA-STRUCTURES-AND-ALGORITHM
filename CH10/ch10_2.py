'''
ให้น้องเขียนโปรแกรมหาค่าที่น้อยที่สุดที่มากกว่าค่าที่ต้องการจะหา ถ้าหากไม่มีให้แสดงว่า No First Greater Value โดยตัวเลขของทั้ง 2 list รับประกันว่าไม่เกิน 1000000

***** อธิบาย Test Case 2:
Left : [3, 2, 7, 6, 8]         Right : [5, 6, 12]
1. หาค่าที่น้อยที่สุดที่มากกว่า 5 จาก list (Left) จะได้เป็น 6
2. หาค่าที่น้อยที่สุดที่มากกว่า 6 จาก list (Left) จะได้เป็น 7
3. หาค่าที่น้อยที่สุดที่มากกว่า 12 จาก list (Left) จะเห็นว่าไม่มีค่าที่มากกว่า 12 จะแสดงเป็น No First Greater Value
'''
def FGV(l,r):
    for i in r:
        minGrater = 1000000
        for j in l:
            if j > i:
                minGrater = min(minGrater,j)
        if minGrater == 1000000:
            print('No First Greater Value')
        else:
            print(minGrater)

inp = input("Enter Input : ").split('/')
l,r = list(map(int,inp[0].split())), list(map(int,inp[1].split()))
FGV(l,r)