'''
ให้น้องเขียน Hashing โดยมีการทำงานดังนี้

1. หา index ของ Table จากผลรวมของ ASCII จากค่า key จากนั้นนำมา mod ด้วยขนาดของ Table
2. หากเกิด Collision ให้ทำการขยับค่า index แบบ Quadratic Probing
3. ถ้าหากเกิด Collision จนถึงค่าที่กำหนดแล้ว ให้ทำการ Discard Data นั้นทิ้งทันที
4. หาก Table นั้นมี Data เต็มแล้วให้แสดงคำว่า This table is full !!!!!! หากเคยแสดงคำนี้ไปแล้วไม่ต้องแสดงอีก (แสดงเพียง 1 ครั้ง)

อธิบาย Input
แบ่ง Data เป็น 2 ชุดด้วย /
    -   ด้านซ้ายหมายถึง ขนาดของ Table และ MaxCollision ตามลำดับ
    -   ด้านขวาหมายถึง Data n ชุด โดย Data แต่ละชุดแบ่งด้วย comma โดยใน Data แต่ละชุดจะแบ่งเป็น key กับ value ตามลำดับ
'''
class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)

class hash:

    def __init__(self,tableSize,maxCollision):
        self.tableSize = [None] * tableSize
        self.maxCollision = maxCollision
    
    def sumofASCII(self,str):
        s = 0
        for i in str:
            s += ord(i)
        return s
    
    def isFull(self):
        for i in range(len(self.tableSize)):
            if self.tableSize[i] == None:
                return False
        print('This table is full !!!!!!')
        return True
    
    def insert(self,key,value):
        indexKey = self.sumofASCII(key) % len(self.tableSize)
        next = indexKey
        countCollision = 0
        i = 1
        while(1):
            if self.isFull():
                break
            if countCollision == self.maxCollision:
                print('Max of collisionChain')
                break
            if self.tableSize[next] == None:
                self.tableSize[next] = Data(key,value)
                break
            print(f'collision number {countCollision+1} at {next}')
            countCollision += 1
            next = (indexKey + pow(i,2)) % len(self.tableSize)
            i += 1
    
    def printHashing(self):
        for i in range(len(self.tableSize)):
            print(f"#{i+1}	{self.tableSize[i]}")
        print('---------------------------')

print(' ***** Fun with hashing *****')
inp = input("Enter Input : ").split('/')
tableSize, MaxCollision = map(int,inp[0].split())
inp = inp[1].split(',')
H = hash(tableSize,MaxCollision)
for i in range(len(inp)):
    if H.isFull() == True:
        break
    s = inp[i].split()
    H.insert(s[0],s[1])
    H.printHashing()