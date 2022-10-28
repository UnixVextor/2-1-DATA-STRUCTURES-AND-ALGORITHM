'''
จงเขียนฟังก์ชั่นในการหา Rank ของ input ที่รับเข้ามา โดย Rank คือการแบ่งเป็นชั้นๆตามข้อมูลของ BST โดยจะเริ่มจากค่าที่น้อยกว่าค่าใน BST ที่น้อยที่สุดจะมีค่า Rank = 0 และค่าที่อยู่ตั้งแต่ค่าที่น้อยที่สุดจนถึงตัวถัดไปจะมีค่า Rank +=1 ไปเรื่อยๆจนถึงชั้นของตัวสุดท้ายหรือตัวมากสุด เช่น



จากรูป ค่าที่น้อยที่สุดคือ -2 ดังนั้น rank(-2) จะได้ 1 แต่ rank ของค่าที่น้อยกว่า -2 จะเท่ากับ 0

และ rank(0) จะเท่ากับ 1 ส่วน rank(1) จะเท่ากับ 2 เป็นต้น
'''
class Node:
    def __init__(self, data = None, right = None,left = None):
        self.data = data
        self.right = right
        self.left = left
    
class BST:
    def __init__(self):
        self.root = None
        self.rank = 0
        
    def insert(self,data):
        self.root = BST._insert(self.root,data)
        return self.root

    
    def _insert(node: 'Node',data):
        if node == None:
            return Node(data)
        
        if data > node.data:
            node.right = BST._insert(node.right,data)
        else:
            node.left = BST._insert(node.left,data)
        return node
    
    
    def findRank(self,node, data):
        if node != None:
                self.findRank(node.left,data)
                if data >= node.data:
                    self.rank += 1
                else:
                    return self.rank
                self.findRank(node.right,data)
        return self.rank
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node.data)
            self.printTree(node.left, level + 1)

T = BST()
root = None
inp = input('Enter Input : ').split('/')
f = int(inp[1])
lst = [int(i) for i in inp[0].split()]

for i in lst:
    root = T.insert(i)

T.printTree(root)
rank = T.findRank(root,f)
print('--------------------------------------------------')
print('Rank of {0} : {1}'.format(f,rank))
    
    
    