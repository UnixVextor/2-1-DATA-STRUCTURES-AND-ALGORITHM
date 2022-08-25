'''
ให้น้องๆเขียนโปรแกรมโดยรับ input 2 แบบ โดยใช้ Queue ในการแก้ปัญหา



E  <value>  ให้นำ value ไปใส่ใน Queue และทำการแสดงผล ข้อมูลปัจจุบันของ Queue

D                 ให้ทำการ Dequeue ตัวที่อยู่หน้าสุดของ Queue ออก หลังจากนั้นแสดงตัวเลขที่เอาออกมา และ แสดงผลข้อมูล
                    ปัจจุบันของ Queue

***และเมื่อจบการทำงานให้แสดงผลข้อมูลปัจจุบันของ Queue พร้อมกับข้อมูลที่ถูก Dequeue ทั้งหมดตามลำดับ
***ถ้าหากไม่มีข้อมูลใน Queue แล้วให้แสดงคำว่า  Empty
'''
class Queue:
    def __init__(self):
        self.items = []

    def enQueue(self,val):
        self.items.append(val)

    def deQueue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []
    
    def peek(self):
        return self.items[0]


inp = input("Enter Input : ").split(',')
lst = []
isE = False
q = Queue()
de = Queue()
dis = ''
countEmpty = 0
for i in inp:
    lst.extend(i.split())

for i in lst:
    if isE :
        q.enQueue(i)
        # print(q.items)
        isE = not isE
        print(', '.join(q.items))

    if i == 'E' and not isE:
        isE = True
    elif i == 'D':
        p = ''
        if not q.isEmpty():
            p = q.deQueue()
            de.enQueue(p)
            dis = ', '.join(q.items)  if not q.isEmpty() else 'Empty'
            print(p + ' <- '+ dis)
        
        else:
            countEmpty += 1
            if(countEmpty < 2):
                print('Empty')
if de.isEmpty() and q.isEmpty():
    print('Empty : Empty')

elif not q.isEmpty() and not de.isEmpty():
    print(', '.join(de.items) + ' : ' + ', '.join(q.items)) 
elif not de.isEmpty() and q.isEmpty():
    print(', '.join(de.items) + ' : ' + 'Empty')
else:
    print('Empty' + ' : ' + ', '.join(q.items))

