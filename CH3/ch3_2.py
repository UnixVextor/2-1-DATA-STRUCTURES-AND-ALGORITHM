from ntpath import join


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

    def peek(self):
        return self.items[self.size()-1]

def checkParentasis(lst):
    s = Stack()
    error = 0
    for i in lst:
        if i in '{[()]}':
            if i in '{[(':
                s.push(i)
                
            else:
                if s.size() > 0 and not Match(str(s.peek()),i):
                    s.pop()
                    error = 1
                elif s.size() > 0 and Match(str(s.peek()),i) and error != 1:
                    s.pop()
                elif s.size() == 0 and i in ')]}' and error != 1:
                    error = 2
                    

    if s.size() > 0:
        error = 3
    return error,s.size(),''.join(s.items)


def Match(l,r):
    left = '{(['
    right = '})]'
    return left.index(l) == right.index(r)



lst = input("Enter expresion : ")
c,size,lst_str = checkParentasis(lst)
if c == 0:
    print(lst + ' MATCH')
elif c == 1:
    print(lst + ' Unmatch open-close')
elif c == 2:
    print(lst + ' close paren excess')
elif c == 3:
    print(lst + ' open paren excess   ' + str(size) + ' : ' + lst_str)