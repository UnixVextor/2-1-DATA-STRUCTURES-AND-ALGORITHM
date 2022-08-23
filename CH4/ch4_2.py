
class Queue:
    def __init__(self):
        self.items = []

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

inp,time = input("Enter people and time : ").split()
inp = [i for i in inp]
time = int(time)
people = Queue()
cashier1 = Queue()
cashier2 = Queue()
timeChaier1 = 0
timeChaier2 = 0

people.items = inp

for i in range(time):
    
    if(timeChaier1 == 3):
        cashier1.deQueue()
        timeChaier1 = 0
    
    if(timeChaier2 == 2):
        cashier2.deQueue()
        timeChaier2 = 0


    if cashier1.size() < 5 and not people.isEmpty():
        cashier1.enQueue(people.deQueue())
    elif cashier1.size() >= 5 and not people.isEmpty():
        cashier2.enQueue(people.deQueue())



    if not cashier1.isEmpty() :  timeChaier1 += 1
    if not cashier2.isEmpty() :  timeChaier2 += 1

    print(i+1, people.items, cashier1.items, cashier2.items)



# print(people.items)
