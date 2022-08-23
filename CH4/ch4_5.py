class Queue:
    def __init__(self,inp = None):
        if (inp == None):
            self.items = []
        else:
            self.items = inp
    def enQueue(self,val):
        self.items.append(val)

    def deQueue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []
    
    def peek(self):
        return self.items[0]
    

class Stack():
    def __init__(self):
        self.items = []
        
    def push(self,i):
        self.items.append(i)
    
    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

def checklast(lst,option):
    if option == -1:
        return True if (lst[-1] == lst[-2]) and (lst[-2] == lst[-3]) else False
    elif option == 1:
        return True if (lst[0] == lst[1]) and (lst[1] == lst[2]) else False

inp = input('Enter Input (Normal, Mirror) : ').split()
Mirror = Stack()
Normal = Stack()
boomMirror = Queue()
temp = Queue()
afterMirrorBoom = False
MirrorBoom = False
countNormal = 0
countMirror = 0
countFailInterrupt = 0

for i in reversed(inp[1]):
    Mirror.push(i)
    if Mirror.size() > 2:
        if checklast(Mirror.items,-1):
            boomMirror.enQueue(i)
            Mirror.pop()
            Mirror.pop()
            Mirror.pop()
countMirror = boomMirror.size()

for i in inp[0]:
    Normal.push(i)
    # print(boomMirror.items, Normal.items, boomMirror.size(), countNormal, countFailInterrupt) 
    if Normal.size() > 2:
        if checklast(Normal.items,-1) and not afterMirrorBoom and not boomMirror.isEmpty():
            afterMirrorBoom = True
            temp.enQueue(Normal.pop())
            Normal.push(boomMirror.deQueue())
            Normal.push(temp.deQueue())
            
        if checklast(Normal.items,-1) and afterMirrorBoom:
            afterMirrorBoom = False
            Normal.pop()
            Normal.pop()
            Normal.pop()
            countFailInterrupt += 1
        elif afterMirrorBoom == True:
            afterMirrorBoom = False
        elif checklast(Normal.items,-1) and boomMirror.isEmpty():
            Normal.pop()
            Normal.pop()
            Normal.pop()
            countNormal += 1 
      


# Display
print('NORMAL :\n' + str(Normal.size()))
if Normal.isEmpty():
    print('Empty')
else:
    print(''.join(reversed(Normal.items)))

print(str(countNormal) + ' Explosive(s) ! ! ! (NORMAL)')
if countFailInterrupt != 0:
    print('Failed Interrupted ' + str(countFailInterrupt) + ' Bomb(s)')

print('------------MIRROR------------')
print(': RORRIM')
print(Mirror.size())
if Mirror.isEmpty():
    print('ytpmE')
else:
    print(''.join(reversed(Mirror.items)))
print('(RORRIM) ! ! ! (s)evisolpxE ' + str(countMirror))

