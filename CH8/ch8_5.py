'''
บริษัทแห่งหนึ่งมีรถตู้ K คันที่ลูกค้าสามารถเช่าไปใช้งานได้ โดยรถตู้แต่ละคันมีรหัสประจำตัวรถเป็นหมายเลขจำนวนเต็มบวกตั้งแต่ 1 จนถึง K ข้อกำหนดในการเลือกรถตู้ให้ลูกค้ามีอยู่ว่า ลูกค้าจะต้องทำการจองรถตู้ก่อน โดยคำสั่งจองจะต้องระบุจำนวนวันที่จะใช้ จากนั้นผู้จองจะได้รถตู้ที่ว่างให้ใช้เร็วที่สุดเท่าที่จะหาได้จากรถตู้ทั้งหมด

ในกรณีที่มีรถตู้ว่างให้ใช้เร็วที่สุดมากกว่า 1 คัน คันที่มีรหัสประจำรถน้อยกว่าจะถูกเลือกก่อน เช่นถ้าหากมีรถตู้ที่ว่างให้ใช้เร็วที่สุด 3 คัน  ซึ่งมีรหัสประจำรถเป็น 5 , 7 และ 20 รถตู้ที่มีหมายเลข 5 จะถูกเลือกก่อน นอกจากนี้การจองจะให้ความสำคัญกับคำสั่งจองที่มาก่อนเสมอ สำหรับการจองแต่ละครั้ง ผู้จองจะได้รับคำตอบกลับมาว่าได้ใช้รถตู้หมายเลขใด  โดยในตอนแรกรถตู้ทุกคันจะว่างและพร้อมใช้งานทั้งหมด

อธิบาย Input โดย Input จะแบ่งเป็น 2 ฝั่งด้วย /
-  ฝั่งซ้ายเป็น K ซึ่งหมายถึงเลขประจำตัวรถ โดยเริ่มตั้งแต่ 1 ถึง K
-  ฝั่งขวาเป็น List จำนวนวันที่จองรถตู้ของลูกค้าที่สั่งจองเข้ามา



คำใบ้ :  Min Heap
'''
class Node():
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
    
    def __str__(self):
        return str(self.data)


class BST():
    
    def __init__(self):
        self.root = None
        
    def insert(self,data):
        self.root = BST._insert(self.root,data)
        return self.root
    
    def _insert(node: 'Node' , data):
        if node == None:
            return Node(data)

        if node.left == None:
            node.left = BST._insert(node.left,data)
        else:
            node.right = BST._insert(node.right,data)
        return node
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node.data)
            self.printTree(node.left, level + 1)


k, inp = input("Enter Input : ").split("/")
inp = [int(i) for i in inp.split(' ')] 
van = dict()
root = None
for i in range(int(k)):
    van.update({i+1:0})

j = 1

while len(inp) > 0:
    T = BST()
    Sort = sorted(van.items(), key = lambda kv: (kv[1],kv[0]))
    # print(Sort)
    for i in Sort:
        root = T.insert(list(i))
    
    van[root.data[0]] += inp[0]
    # print(root.data[0])
    
    print(f'Customer {j} Booking Van {root.data[0]} | {inp.pop(0)} day(s)')
    j += 1
    