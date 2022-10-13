'ให้น้องๆรับ input เป็น postfix จากนั้นให้แปลงเป็น Expression Tree , Infix และ Prefix  โดย Operator จะมีแค่ + - * /'
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class Stack():
    
    def __init__(self):
        self.item = []
    
    def push(self,data):
        self.item.append(data)
    
    def pop(self):
        return self.item.pop()
    
    def isEmpty(self):
        return self.item == []
    
    def size(self):
        return len(self.item)

    def top(self):
        return self.item[-1]
    
class BST:
     def __init__(self):
        self.root = None
        # self.temp = None

     def insert(self, data):
        self.root = BST._insert(self.root,data)
        return self.root
    
     def _insert(node: 'Node',data):
        if isinstance(data,Node) and node == None:
            return data 
        elif node == None:
            return Node(data)
        
        if node.right is None:
            node.right = BST._insert(node.right,data)
        elif node.left is None:
            node.left = BST._insert(node.left,data)
        return node
    
     def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
     
     def infix(self):
            BST.inOrder(self.root)         
        
     def inOrder(node: 'Node'):
         if (node != None):
             if node.data  in '+-*/': 
                print('(',end='')
             BST.inOrder(node.left)
             print(node.data,end='')
             BST.inOrder(node.right)
             if node.data in '+-*/':
                print(')',end='')
    
     def prefix(self):
         BST.preOrder(self.root)
    
     def preOrder(node:'Node'):
         if (node != None):
            print(node.data,end='')
            BST.preOrder(node.left)
            BST.preOrder(node.right)

        
    
inp = input('Enter Postfix : ')
s = Stack()
for i in inp:
    T = BST()
    if i not in '+-*/':
        s.push(i)
    elif s.size() > 1 and  i in '+-*/':
        root = T.insert(i)
        root = T.insert(s.pop())
        root = T.insert(s.pop())
        s.push(root)
print('Tree :')
T.printTree(root)
print('--------------------------------------------------')
print('Infix : ',end='')
BST.infix(T)
print()
print('Prefix : ',end='')
BST.prefix(T)
    