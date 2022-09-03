'''
ให้ตรวจสอบว่า linked list มีการวนซ้ำหรือไม่ และ แสดงผลลัพธ์ตามตัวอย่าง

โดยมีการรับ input ดังนี้

1. append ->   A <int> คือ เพิ่มข้อมูลต่อท้าย linked list

2. set_next -> S <index1(int):index2(str)> คือการ set node.next ของ node index ที่1 ให้ชี้ไป node index ที่2

ซึ่งหากไม่มี  node index ที่1 ใน linked list ให้แสดง error และหากไม่มี node index ที่2 ใน linked list ให้ทำการ append nodeใหม่เข้าไปใน linked list โดยมี value = index2
'''
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = 0
        self._size = 0
        self.CountLoop = 0
    
    def append(self, item):
        if self.isEmpty():
            self.head = Node(item)
            self._size += 1
            return   
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = Node(item)
        self._size += 1
    
    def __str__(self):
        if self.isEmpty():
            return 'Empty'
        Str = self.head.data
        cur = self.head
        i = 0
        while cur.next != None:
            if i < self.size():
                Str += '->'
            cur = cur.next
            Str += cur.data
            i += 1
        return Str
    
    def set_next(self,index1,index2):
        if self.isEmpty():
            return 'Error! {list is empty}'
        if index1 > self.size() - 1:
            return 'Error! {index not in length}: ' + str(index1)
        if index2 > self.size() - 1:
            self.append(str(index2))
            return 'index not in length, append : ' + str(index2)
            
        if index1 < index2:
           i = 0
           cur = self.head
           ptr = self.head
           while i < index2:
               if i < index1:
                   cur = cur.next
               ptr = ptr.next
               i += 1
           cur.next = ptr
           return f'Set node.next complete!, index:value = {index1}:{cur.data} -> {index2}:{ptr.data}'
        
        if index1 > index2:
            self.CountLoop += 1
            i = 0
            cur = self.head
            ptr = self.head
            while i < index1:
                if i < index2:
                    ptr = ptr.next
                cur = cur.next
                i += 1
            return f'Set node.next complete!, index:value = {index1}:{cur.data} -> {index2}:{ptr.data}'
        if index1 == index2:
           self.CountLoop += 1
           i = 0
           cur = self.head
           while i < index1:
              cur = cur.next
              i += 1   
           return f'Set node.next complete!, index:value = {index1}:{cur.data} -> {index2}:{cur.data}'
        
    def size(self):
        return self._size

    def isEmpty(self):
        return self._size == 0

s = LinkedList()
inp = input('Enter input : ').split(',')
for i in inp:
    if i[0] == 'A':
        s.append(i[2:])
        print(s)
    elif i[0] == 'S':
        print(s.set_next(int(i[2]),int(i[4])))

if s.CountLoop > 0:
    print('Found Loop')
else:
    print('No Loop')
    print(s)    
