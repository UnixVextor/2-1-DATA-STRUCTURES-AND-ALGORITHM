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

class StackCalc():
    def __init__(self):
        self.s = Stack()
        self.isInvalid = False
        self.valueInvalid = ''

    def run(self,arg):
        if len(arg) == 1:
            self.s.push(arg[0])
            return 0
        for i in arg:
           
            if i != '+' and i != '-' and i != '*' and i != '/' and i != 'DUP' and i != 'POP' and i != 'PSH' and is_digi(i):          
                self.s.push(i)
            elif i in '+-*/DUPPOPPSH':
                pass
            else:
                self.isInvalid = True
                self.valueInvalid = i
                return 0

            if i == '+' and self.s.size() >= 2:
                self.s.push(str(int(self.s.pop()) + int(self.s.pop())))
            elif i == '-'  and self.s.size() >= 2:
                    self.s.push(str(int(self.s.pop()) - int(self.s.pop())))
            elif i == '*' and self.s.size() >= 2:
                    self.s.push(str(int(self.s.pop()) * int(self.s.pop())))
            elif i == '/' and self.s.size() >= 2:          
                    self.s.push(str(int(self.s.pop()) // int(self.s.pop())))
            elif i == 'DUP' and self.s.size() > 0:
                    self.s.push(self.s.items[-1])
            elif i == 'POP' and self.s.size() > 0:
                    self.s.pop()
            elif i == 'PSH' and self.s.size() > 0:
                    # self.s.push(self.s.items[-1])
                pass

            # print(self.s.items)
    

    def getValue(self):
        
        if not self.isInvalid and not self.s.isEmpty():
            return self.s.pop()
        elif self.s.isEmpty() and not self.isInvalid:
            return int(0)
        else:
            return "Invalid instruction: " + self.valueInvalid

def is_digi(n):
    try:
        int(n)
        return True
    except ValueError:
        return False

print("* Stack Calculator *")
arg = input("Enter arguments : ").split()
machine = StackCalc()

machine.run(arg)
print(machine.getValue())

