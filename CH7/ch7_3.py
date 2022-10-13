'ให้น้องรับ input เป็น list กับ k และจากนั้นให้สร้าง Binary Search Tree จาก list ที่รับเข้ามา และหาว่าใน Binary Search Tree นั้นมีกี่ Node ที่มีค่าน้อยกว่าหรือเท่ากับ k'
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = BST._insert(self.root,data)
        return self.root
    
    def _insert(node: 'Node',data):
        if node == None:
            return Node(data)
        
        if data < node.data:
            node.left = BST._insert(node.left,data)
        else:
            node.right = BST._insert(node.right,data)
        return node
    
    def countBelow(node:'Node',k):
        n = 0
        if node == None:
            return 0
    
        if node.data <= k:
            n += 1
        if k <= node.data:
            n += BST.countBelow(node.left,k)
        else:
            n += BST.countBelow(node.right,k)
            n += BST.countBelow(node.left,k)
        return n
        
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp = input('Enter Input : ').split('/')
k = int(inp[1])
lstinp = [int(i) for i in inp[0].split()]
for i in lstinp:
    root = T.insert(i)
T.printTree(root)
print('--------------------------------------------------')
print(BST.countBelow(root,k))

