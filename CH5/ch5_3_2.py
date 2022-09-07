'''
ให้น้องรับ Linked List มา 2 ตัว จากนั้นนำ 2 Linked List มาต่อกัน โดย L2 จะมาต่อ L1 แบบกลับหลัง
'''
class Node():
    def __init__(self,data = None , Next = None,prev = None):
        self.data = data
        self.next = Next 
        self.prev = prev

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None 
        self._size = 0
    
    def push(self,data):
        node = Node(data)
        if self.isEmpty():
            self.head = node
            self.tail = node
            return
        head = self.head
        while head.next != None:
            head = head.next
        node.prev = head        
        head.next = node
        self.tail = node
        self._size += 1           
    
    def __str__(self):
        s = ''
        node = self.head
        while node.next != None:
            s = s + ' ' + node.data
            node = node.next
        s =  s + ' ' + node.data
        return s 
            
    def isEmpty(self):
        return self.head == None
    
    def size(self):
        return self._size
    
    def Merge(self,b):
        head = self.head
        tail = b.tail
        while head.next != None:
            head = head.next
        head.next = Node(tail.data,None,head)
        while tail.prev != None:
            tail = tail.prev
            head = head.next
            head.next = Node(tail.data,None,head)

inp = input('Enter Input (L1,L2) : ').split()
L1 = inp[0].split('->')
L2 = inp[1].split('->')
a = LinkedList()
b = LinkedList()

for i in L1:
    a.push(i)
for i in L2:
    b.push(i)
print(f'L1    :{a}')
print(f'L2    :{b}')
a.Merge(b)
print(f'Merge :{a}')