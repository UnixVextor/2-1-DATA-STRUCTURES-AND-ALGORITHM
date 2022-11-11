'''
ให้น้องๆเขียนการทำ Rehashing ด้วยเงื่อนไขดังนี้
1. Table เต็มถึงระดับที่กำหนด ( Threshold (%) )
2. เมื่อเกิดการ Collision ถึงจำนวนที่กำหนด

หากเกิดการ Rehashing ให้ทำการขยาย Table เป็นค่า prime ถัดไปที่มากกว่าเดิม 2 เท่า เช่น หาก Table ตอนแรกมีขนาด 4 และเกิดการ Rehashing  ตัว Table ใหม่จะมีขนาดเป็น 11 เนื่องจาก 2 เท่าของ 4 คือ 8  และค่า prime ที่มากกว่า 8 และใกล้ 8 มากที่สุดคือ 11

การ Hash หากเกิดการ Collision ให้ใช้ Quadratic Probing ในการแก้ปัญหา Collision

อธิบาย Input
แบ่ง Data เป็น 2 ชุดด้วย /
    -   ด้านซ้ายหมายถึง ขนาดของ Table , MaxCollision และ Threshold (สูงสุด 100 %) ตามลำดับ
    -   ด้านขวาหมายถึง Data n ชุด โดย Data แต่ละชุดแบ่งด้วย spacebar และ Data แต่ละตัวเป็นจำนวนเต็มศูนย์หรือบวกเท่านั้น และไม่มี Data ซ้ำกันเด็ดขาด
'''
class Data:
    def __init__(self, key, value = 0):
        self.key = key
        self.value = value

    # def __str__(self):
    #     return "({0}, {1})".format(self.key, self.value)
    def __str__(self):
        return str(self.key) 
    
class hash:
    
    def __init__(self, TableSize = 0, MaxCollision = 0,Threshold = 0):
        self.TableSize = [None] * TableSize
        self.MaxCollision = MaxCollision
        self.Threshould = Threshold
        self.dataSize = 0
        self.member = []
    
    def overThreshold(self):
        return True if ((self.dataSize/len(self.TableSize)*100) >= self.Threshould) else False  

    def primeNumber(slef,a):
        
        if a > 1:
            n = a
            while(1):
                for i in range(2,n):
                    if n-1 == i:
                        return n
                    if n % i == 0:
                        n += 1
                        break
                
   
    def isFull(self):
        for i in range(len(self.TableSize)):
            if self.TableSize[i] == None:
                return False
        print('This table is full !!!!!!')
        return True 
    
    
    def Reshape(self):
        new_Table = [None] * self.primeNumber(len(self.TableSize) * 2)
        for i in self.member:
            if i != None:
                if new_Table[i % len(new_Table)] == None:
                    new_Table[i % len(new_Table)] = i
                else:
                    countCollision = 0
                    j = 1
                    next = i % len(new_Table)
                    while(1):
                        if new_Table[next] == None:
                            new_Table[next] = i
                            break
                        print(f'collision number {countCollision+1} at {next}')
                        countCollision += 1
                        next = (i + pow(j,2)) % len(new_Table)
                        j+=1
        self.TableSize = new_Table
    
    def insert(self,val):
        indexval = val % len(self.TableSize)
        next = indexval
        i = 1
        countCollision = 0
        self.dataSize += 1
        while(1):
            
            if self.overThreshold():
                print('****** Data over threshold - Rehash !!! ******')
                self.Reshape()
                indexval = val % len(self.TableSize)
                next = indexval
                i = 1
                
            if self.TableSize[next] == None:
                self.member.append(val)
                self.TableSize[next] = Data(val)
                break
            print(f'collision number {countCollision+1} at {next}')
            countCollision += 1
            next = (indexval + pow(i,2)) % len(self.TableSize)
            i += 1
            if countCollision == self.MaxCollision:
                print('****** Max collision - Rehash !!! ******')
                self.Reshape()
                indexval = val % len(self.TableSize)
                next = indexval
                i = 1
    
    def printHashing(self):
        for i in range(len(self.TableSize)):
            print(f"#{i+1}	{self.TableSize[i]}")
        print('----------------------------------------')

print(' ***** Rehashing *****')
inp = input("Enter Input : ").split('/')
TableSize , MaxCollision, Threshold = map(int,inp[0].split())
H = hash(TableSize,MaxCollision,Threshold)
# print(Threshold)
print('Initial Table :')
H.printHashing()

for i in inp[1].split():
    print(f'Add : {i}')
    H.insert(int(i))
    H.printHashing()
