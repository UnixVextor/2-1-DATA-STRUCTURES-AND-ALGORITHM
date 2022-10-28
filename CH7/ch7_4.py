'ให้น้องรับ input เข้ามาและสร้าง Binary Search Tree ต่อมาให้แสดงผลแบบ Preorder , Inorder , Postorder และ Breadth First Search ตามลำดับ'
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

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
    
    def printInorder(self):
        BST.inOrder(self.root)
    
    def inOrder(node: 'Node'):
        if(node != None):
            BST.inOrder(node.left)
            BST.visit(node)
            BST.inOrder(node.right)
    
    def printPreorder(self):
        BST.preOrder(self.root)

    def preOrder(node:'Node'):
        if node != None:
            BST.visit(node)
            BST.preOrder(node.left)
            BST.preOrder(node.right)        
    
    def printPostOrder(self):
        BST.postOrder(self.root)
    
    def postOrder(node: 'Node'):
        if node != None:
            BST.postOrder(node.left)
            BST.postOrder(node.right) 
            BST.visit(node)
    
    def printBreadth(self):
        BST.breadth(self.root)
    
    def breadth(node:'Node'):
        q = Queue()
        q.enQueue(node)
        while(q.isEmpty() == False):
            n = q.deQueue()
            BST.visit(n)
            if n.left is not None:
                q.enQueue(n.left)
            if n.right is not None:
                q.enQueue(n.right)
               
    def visit(node: 'Node'):
        print(node.data,end=' ')

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
T.printTree(root)
print('Preorder : ',end='')
BST.printPreorder(T)
print()
print('Inorder : ',end='')
BST.printInorder(T)
print()
print('Postorder : ',end='')
BST.printPostOrder(T)
print()
print('Breadth : ',end='')
BST.printBreadth(T)
