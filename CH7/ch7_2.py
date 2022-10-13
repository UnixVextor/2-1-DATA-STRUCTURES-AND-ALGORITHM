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
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
            
    def getMin(self):
        cur = self.root
        while cur.left != None:
            cur = cur.left
        return cur.data
    
    def getMax(self):
        cur = self.root
        while cur.right != None:
            cur = cur.right
        return cur.data

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
T.printTree(root)
print('-'*50)
print('Min :',T.getMin())
print('Max :',T.getMax())
