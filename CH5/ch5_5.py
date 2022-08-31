class Node:
    def __init__(self, value = None,next = None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)

def createLL(LL):
    head = Node()
    cur = head
    cur.value = LL.pop(0)
    while len(LL) != 0:
        cur.next = Node(LL.pop(0))
        cur = cur.next
    return head

def printLL(head):
    l = []
    cur = head
    # print(cur.value)
    if cur.value == None:
        cur = cur.next
    l.append(str(cur))
    while True:
        cur = cur.next
        l.append(str(cur))
        if cur.next == None:
            break
    return ' '.join(l)

def SIZE(head):
    cur = head
    i = 1
    while cur.next != None:
        cur = cur.next
        i += 1
    return i

def bottomUp(head,b,size):
    before = head
    cur = head
    indexTocut = int(size * (b/100))
    if indexTocut > 1:
        while True:
            cur = cur.next
            indexTocut -= 1
            if indexTocut == 1:
                head = cur.next
                cur.next = None
                break
    else:
        head = cur.next
        cur.next = None
    
    cur = head
    while True:
        if cur.next != None and cur.value != None:
            cur = cur.next
        else:
            break 
    cur.next = before
    
    return head

def riffle(head,r,size):
    indexTocut = int(size * (r/100))
    if int(r/10) == 0 or int(r/10) == 10:
        return head

    first = head
    second = None
    
    node = head
    if indexTocut > 1:
        while True:
            indexTocut -= 1
            if indexTocut == 0:
                second = node.next
                node.next = None
                break
            node = node.next
    else:
        second = node.next
        node.next = None
    
    firstNode = first
    secondNode = second
    
    head = Node()
    result = head
    while True:
        result.value = firstNode.value
        if firstNode.next != None:
            result.next = Node()
        else:
            result.next = secondNode
            break
        
        if firstNode.next != None:
            firstNode = firstNode.next
        result = result.next
        
        result.value = secondNode.value
        if secondNode.next != None:
            result.next = Node()
        else:
            result.next = firstNode
            break
        
        if secondNode.next != None:
            secondNode = secondNode.next   
        result = result.next
    
    return head

def deriffle(head,r,size):
    indexToCut = min(size - int(size * (r/100)), int(size * (r/100)))
    if indexToCut == 0:
        return head
    
    firstHead = Node()
    secondHead = Node()
    firstNode = firstHead
    secondNode = secondHead
    
    node = head
    while True:
        firstNode.value = node.value
        if indexToCut > 1:
            firstNode.next  = Node()
            firstNode = firstNode.next
        node = node.next
        
        secondNode.value = node.value
        if indexToCut > 1:
            secondNode.next = Node()
            secondNode = secondNode.next
        node = node.next
        
        indexToCut -= 1
        if node == None:
            break
        elif indexToCut  == 0:
            if r >= 50:
                firstNode.next = node
            else:
                secondNode.next = node
            break
    tail = firstHead
    while True:
        if tail.next == None:
            break
        tail = tail.next
    tail.next = secondHead
    
    return firstHead

def debottomUp(head,b,size):
    indexTocut = size - int(size * (b/100))
    first = head
    second = head
    if indexTocut > 1:
        while True:
            first = first.next
            indexTocut -= 1
            if indexTocut == 1:
                head = first.next
                first.next = None
                break
    else:
        head = first.next
        first.next = None
    
    first = head
    if first.next != None:
        while True:
            first = first.next
            if first.next == None:
                break
    first.next = second
    return head    
    

def scarmble(head, b, r, size):
    head = bottomUp(head,b,size)
    print('BottomUp {0:.3f} % : {1}'.format(b,printLL(head)))
    head = riffle(head,r,size)
    print('Riffle {0:.3f} % : {1}'.format(r,printLL(head)))
    head = deriffle(head,r,size)
    print('Deriffle {0:.3f} % : {1}'.format(r,printLL(head)))
    head = debottomUp(head,b,size)
    print('Debottomup {0:.3f} % : {1}'.format(b,printLL(head)))
    
    return head


inp1, inp2 = input('Enter Input : ').split('/')
print('-' * 50)
h = createLL(inp1.split())
for i in inp2.split('|'):
    print("Start : {0}".format(printLL(h)))
    k = i.split(',')
    if k[0][0] == "B" and k[1][0] == "R":
        h = scarmble(h, float(k[0][2:]), float(k[1][2:]), SIZE(h))
    elif k[0][0] == "R" and k[1][0] == "B":
        h = scarmble(h, float(k[1][2:]), float(k[0][2:]), SIZE(h))
    print('-' * 50)