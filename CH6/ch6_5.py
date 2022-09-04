'''
เขียนโปรแกรมที่แสดงผลดังตัวอย่าง

****ห้ามใช้คำสั่ง for, while, do while*****

หมายเหตุ ฟังก์ชันมี parameter ได้ไม่เกิน 2 ตัว
'''
    
def Draw(i = 0,j=0):
    global inp
    if inp > 0:  
        print('_' * i,end='')
        print('#' * j)    
        inp -= 1
        Draw(i-1,j+1)

    elif inp < 0:
        print('_' * i,end='')
        print('#' * j)
        inp += 1
        Draw(i+1,j-1)

global i
global j
inp = int(input('Enter Input : '))
if inp > 0:
    i = inp - 1
    j = 1 
    Draw(i,j)
elif inp < 0:
    i = 0
    j = (inp * -1)
    Draw(i,j)
else:
    print('Not Draw!')