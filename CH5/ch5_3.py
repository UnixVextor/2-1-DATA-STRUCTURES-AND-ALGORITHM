'''
หลังจากกฤษฎาล้างจานเสร็จ ก็ได้มาเล่นเกมส์ที่กำลังเป็นที่นิยมทั่วโลกในตอนนี้   Microsoft Flight Simulator ?  Fall Guys ?  Valorant ?  ผิดทั้งหมดกฤษฎาได้กล่าวไว้  เกมที่กำลังเป็นที่นิยมคือ Color Crush ต่างหาก   โดยเกมนี้จะเป็นการนำสีมาเรียงต่อกัน โดยสีจะหายไปก็ต่อเมื่อมีการเรียงสีเหมือนกันครบ 3 อัน เช่น  A B B B A  -> A A เนื่องจาก B เรียงติดกัน 3 ตัวทำให้ระเบิดหายไปโดยที่สีจะมีทั้งหมด 26 สี และจะถูกแทนด้วย A - Z  โดยถ้าหากมีการระเบิดตั้งแต่ 2 ครั้งขึ้นไปจะแสดง Combo ขึ้นมา

โดยเมื่อการระเบิดสิ้นสุดลงให้แสดงลำดับของสีที่เหลือจากขวาไปซ้าย
'''
class Node:
    def __init__(self, data = None):
        if data != None:
            self.data  = data
        else:
            self.data = None
        self.next = None
        
class List:
    def __init__(self):
        self.head = None
        self._size = 0
    
    def __str__(self):
        if self.isEmpty():
            return 'Empty'
        Str = self.head.data
        cur = self.head
        while cur.next != None:
            cur = cur.next
            Str += cur.data
        return Str 
    
    def append(self,item):
        if self.isEmpty():
            self.head = Node(item)
            self._size += 1
            return 
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = Node(item)
        self._size += 1
        
    def pop(self):
        if self.size() == 1:
            self.head = None
            self._size -= 1
            return
        i = 0
        cur = self.head
        while i < self.size() - 2:
            cur = cur.next
            i += 1
        ans = cur.next.data
        cur.next.data = None
        cur.next = None
        self._size -= 1
        return ans

    def size(self):
        return self._size
    
    def isEmpty(self):
        return self.size() == 0
    
    def peek(self,index):
        i = 0
        cur = self.head
        while i < index:
            cur = cur.next
            i += 1
        return cur.data

s = List()
inp = input('Enter Input : ').split()
boom = 0

for i in inp:
    s.append(i)
    if s.peek(s.size()-1) == s.peek(s.size() - 2 ) == s.peek(s.size() - 3) and s.size() > 2:
        boom += 1
        s.pop()
        s.pop()
        s.pop()
        
Str = ''
print(s.size())
if s.isEmpty():
    print(s)
else:
    for i in range(s.size()):
        Str += s.__str__()[(s.size() - 1) - i]
    print(Str)
if boom > 1:
    print(f'Combo : {boom} ! ! !')
