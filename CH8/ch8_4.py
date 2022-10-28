'''
Jean รักษาการผู้บัญชาการของกองอัศวิน Favonius แห่ง Mondstadt ต้องการทราบถึงขุมพลังของอัศวินในแต่ละกลุ่มภายในเมือง Mondstadt แห่งนี้จึงจะทดสอบความแข็งแกร่งของขุมกำลังที่มี โดยจะทำการจัดวางกำลังอัศวินภายในเมือง Mondstadt ดังตัวอย่างต่อไปนี้
                พลัง    :   5  4  4  3  2  2  2
                ลำดับ  :   0  1  2  3  4  5  6
จากข้อมูลข้างต้นประกอบด้วยอัศวินทั้งหมด 7 คน เรียงตามลำดับตั้งแต่ลำดับที่ 0 ถึง 6 และพลังของอัศวินแต่ละคนมีข้อกำหนดดังนี้
    -  อัศวินลำดับที่ n จะมีลูกน้องในสังกัดอยู่ลำดับที่ 2n+1 และ 2n+2 (ลูกน้องของลูกน้องของอัศวินลำดับที่ n ถือว่าเป็นลูกน้องของอัศวินลำดับที่ n ด้วย)
    -  ค่าพลังของอัศวินมีค่าตั้งแต่ 0 - 5
    -  กลุ่มของอัศวินกลุ่มที่ i จะมีสมาชิกคือ อัศวินลำดับที่ i และลูกน้องของอัศวินลำดับที่ i (รวมลูกน้องของลูกน้องของอัศวินด้วย)
    -  พลังของกลุ่มอัศวินลำดับที่ i เป็นพลังรวมของสมาชิกของอัศวินทั้งหมดในกลุ่ม เช่น
            -  อัศวินกลุ่มที่ 1 หมายถึง กลุ่มของอัศวินลำดับที่ 1 ซึ่งมีสมาชิกประกอบด้วย อัศวินลำดับที่ 1, 3 และ 4 และค่าพลังรวมของอัศวินกลุ่มที่ 1 เท่ากับ 4 + 3 + 2 = 9
            -  อัศวินกลุ่มที่ 2 หมายถึง กลุ่มของอัศวินลำดับที่ 2 ซึ่งมีสมาชิกประกอบด้วย อัศวินลำดับที่ 2 , 5 และ 6 และค่าพลังรวมของอัศวินกลุ่มที่ 2 เท่ากับ 4 + 2 + 2 = 8

ดังนั้นเมื่อนำพลังของอัศวินกลุ่มที่ 1 และ 2 มาเทียบกัน จะได้ว่าพลังรวมของอัศวินกลุ่มที่ 1 นั้นมากกว่าพลังรวมของอัศวินกลุ่มที่ 2
Jean ต้องการทราบว่าค่าพลังรวมของอัศวินภายในเมือง Mondstadt เป็นเท่าใด และถ้าเปรียบเทียบระหว่างอัศวินแต่ละกลุ่มแล้วค่าของพลังรวมของอัศวินในกลุ่มใดมีค่ามากกว่ากัน
'''
class Node:
    def __init__(self, data = None, right = None,left = None):
        self.data = data
        self.right = right
        self.left = left
class Queue:
    def __init__(self):
        self.item = []
    
    def enQueue(self,data):
        self.item.append(data)
    
    def deQueue(self):
        return self.item.pop(0)
    
    def size(self):
        return len(self.item)

    def isEmpty(self):
        return  self.item == []

class BST:
    def __init__(self):
        self.root = None
        
    def insert(self,data):
        self.root = BST._insert(self.root,data)
        return self.root

    
    def _insert(node: 'Node',data):
        if node == None:
            return Node(data)
        if node.left == None:
            node.left = BST._insert(node.left,data)
        else:
            node.right = BST._insert(node.right,data)
        return node
    
    def comparison(node: 'Node', num1 , num2):
        q = Queue()
        q.enQueue(node)
        i = -1
        r1 = 0
        r2 = 0
        while q.isEmpty() == False:
            n = q.deQueue()
            i += 1
            if i == num1 or i == (num1*2 +1) or i == (num1*2 + 2):
                r1 += n.data
            if i == num2 or i == (num2*2 + 1) or i == (num2*2 + 2):
                r2 += n.data
            if n.left is not None:
                q.enQueue(n.left)
            if n.right is not None:
                q.enQueue(n.right)
        if r1 > r2:
            return print("{0}>{1}".format(num1,num2))
        elif r1 == r2:
            return print("{0}={1}".format(num1,num2)) 
        else:
            return print("{0}<{1}".format(num1,num2))
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node.data)
            self.printTree(node.left, level + 1)

T = BST()
lst = input("Enter Input : ").split('/')
data = [int(i) for i in lst[0].split()]
sum = 0
for i in data:
    root = T.insert(i)
    sum += i
print(sum)
for i in lst[1].split(','):
    BST.comparison(root,int(i[0]),int(i[2]))     
    