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

def findValueInStck(lst,n):
    for i  in range(len(lst)):

        if lst[i] == n:
            return True

    return False
        

def fie(lst):
    for i in lst:
        print(i)

print("******** Parking Lot ********")

m,s,o,n = input("Enter max of car,car in soi,operation : ").split()
soi = Stack()
m,n = int(m),int(n)
s = s.split(',')
s = [int(i) for i in s]



for i in s:
    soi.push(i)
    if i == 0:
        soi.pop()

if o == 'arrive' and soi.size() < m:
    if findValueInStck(soi.items,n) == True:
        print('car '+str(n)+' already in soi')
    else:
        soi.push(n)
        print('car '+str(n) +' arrive! : Add Car '+ str(n))

elif o == 'depart' and soi.size() > 0:
    soi_pop = Stack()
    if findValueInStck(soi.items,n):
        for i in range(soi.size() - (soi.items.index(n))):
            soi_pop.push(soi.pop())

        for i in reversed(soi_pop.items):
            if i != n:
                soi.push(i)
        print('car '+str(n)+' depart ! : Car '+str(n)+' was remove') 
    elif findValueInStck(soi.items,n) == False:
        print('car '+str(n)+' cannot depart : Dont Have Car '+str(n))


elif soi.size() >= m:
    print("car " + str(n) + ' cannot arrive : Soi Full')     

elif soi.size() <= 0:
    print('car '+str(n) + ' cannot depart : Soi Empty')

print(soi.items)
