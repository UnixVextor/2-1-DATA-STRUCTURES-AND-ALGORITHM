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

def checklast(lst):

    return True if (lst[-1] == lst[-2]) and (lst[-2] == lst[-3]) else False


inp = input('Enter Input : ').split()
# inp = ['B','A','X','A','A','A']

# print(checklast(inp))
combo = 0

S = Stack()

for i in inp:
    
    S.push(i)
    if S.size() > 2:
        if checklast(S.items):
            S.pop()
            S.pop()
            S.pop()
            combo += 1

print(S.size())
if(S.size() == 0):
    print("Empty")
else:
    print(''.join(S.items[::-1]))
if combo > 1:
    print('Combo : ' + str(combo) + ' ! ! !')