'''
สมมติว่านักศึกษาแอบชอบคนๆหนึ่งอยู่ โดยที่นักศึกษาและคนๆนั้นจะมีกิจกรรมและสถานที่ที่ไปแตกต่างกันในแต่ละวัน
ให้นักศึกษาเขียนโปรแกรมที่จะหาว่าสิ่งที่นักศึกษาและคนๆนั้นทำในแต่ละวันจะทำให้ได้คบกันหรือไม่ โดยใช้ Queue

กิจกรรม                                       สถานที่
0 = กินข้าว(Eat)                           0 = ร้านอาหาร(Res.)
1 = เล่นเกม(Game)                      1 = ห้องเรียน(ClassR.)
2 = ทำโจทย์ datastruc(Learn)      2 = ห้างสรรพสินค้า(SuperM.)
3 = ดูหนัง(Movie)                        3 = บ้าน(Home)

โดยการรับ Input จะประกอบด้วย

กิจกรรม:สถานที่(ของนักศึกษาและของคนๆนั้น) โดยในแต่ละวันจะคั่นด้วยเครื่องหมาย ,

เช่น วันที่ 1 นักศึกษาไปกินข้าวที่ร้านอาหาร และ คนๆนั้นไปนั่งทำโจทย์ datastruc ที่ร้านอาหาร 
       วันที่ 2 นักศึกษาไปเล่นเกมที่บ้าน และ คนๆนั้นไปดูหนังที่ห้างสรรพสินค้า
จะได้ว่า 0:0 2:0,1:3 3:2

***มีการคิดคะแนนดังนี้***

·       กิจกรรมเดียวกันแต่คนละสถานที่         +1

·       สถานที่เดียวกันแต่ทำกิจกรรมต่างกัน    +2

·       กิจกรรมเดียวกันและสถานที่เดียวกัน    +4

·       ไม่เหมือนกันเลย                                   - 5

หากมีคะแนนมากกว่าหรือเท่ากับ 7 จะถือว่าได้คบกัน แต่ถ้าคะแนนน้อยกว่า 7 แต่มากกว่า 0 เป็นคนคุย น้อยกว่านั้นถือว่าเป็นได้แค่เพื่อน

โดยในแต่ละขั้นตอนให้แสดงผลดังตัวอย่าง
'''
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

def rm(lst,prev,after):
    result = []
    for i in lst:
        j = i.replace(prev,after)
        result.extend(j)
    return result

def printDetail(lst,str,Data1=None,Data2=None):
    for i in range(lst.size()):  
        if i == 0:
            print(str,end='')
            
        if Data1 != None and Data2 != None:    
            if i % 2 == 0:
                print(Data1[lst.items[i]] + ':',end='')
            else:
                if i == lst.size() - 1:
                    print(Data2[lst.items[i]],end='')
                else:
                    print(Data2[lst.items[i]] + ', ',end='')
        else:
            if i % 2 == 0:
                print(lst.items[i] + ':',end='')
            else: 
                if i == lst.size() - 1:
                    print(lst.items[i],end='')
                else: print(lst.items[i] + ', ',end='')
    

inp = input("Enter Input : ").split(',')

mq = Queue()
yq = Queue()
k = rm((rm(inp,' ','')),':','')
IsSameAct = False
IsSameLocat = False
score = 0
j = 0
Data1 = {'0':'Eat','1':'Game','2':'Learn','3':'Movie'}
Data2 = {'0':'Res.','1':'ClassR.','2':'SuperM.','3':'Home'}
for i in range(len(k)):
    if j < 2 and j >= 0:
        mq.enQueue(k[i])
        if j == 1:
            j = -3  
    else:
        yq.enQueue(k[i])        
    j += 1

printDetail(mq,'My   Queue = ')
print()
printDetail(yq,'Your Queue = ')
print()
printDetail(mq,'My   Activity:Location = ',Data1,Data2)
print()
printDetail(yq,'Your Activity:Location = ',Data1,Data2)
print()

for i in range(mq.size()//2):
    if mq.deQueue() == yq.deQueue():
        IsSameAct = True
    if mq.deQueue() == yq.deQueue():
        IsSameLocat = True
    
    if IsSameAct and IsSameLocat:
        score += 4
        IsSameAct = False
        IsSameLocat = False
        
    elif IsSameAct and not IsSameLocat:
        score += 1
        IsSameAct = False
        IsSameLocat = False
    elif not IsSameAct and IsSameLocat:
        score += 2
        IsSameAct = False
        IsSameLocat = False
    else:
        score -= 5
        IsSameAct = False
        IsSameLocat = False
        
if score >= 7:
    print('Yes! You\'re my love! : Score is ' + str(score) +'.')
elif score < 7 and score > 0:
    print('Umm.. It\'s complicated relationship! : Score is ' + str(score) +'.')
else:
    print('No! We\'re just friends. : Score is ' + str(score) +'.')
    
