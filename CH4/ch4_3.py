'''
จงเขียน ฟังก์ชั่นสำหรับการ encode และ decode ของ String ที่รับมาโดยให้ทำเป็นรูปแบบ Queue

รูปแบบการรับ Input โดยจะคั่นแต่ละตำแหน่งด้วย คอมม่า(',') :

    - ตำแหน่งที่หนึ่ง string ไม่จำกัดความยาวโดยที่จะไม่นับช่องว่าง(spacebar)

    - ตำแหน่งที่สอง ชุดตัวเลข(1-9)

โดยที่รูปแบบการ encode คือ การนำ String ที่รับมาเพิ่มค่า ascii เท่ากับค่าของชุดตัวเลขในตำแหน่งแรก หลังจากนั้นให้ dequeue ชุดตัวเลขออกไปไว้ข้างหลังสุด เช่น ตัวอักษรตำแหน่งแรกคือ i และชุดตัวเลขในตำแหน่งแรกคือ 2 ดังนั้นตัวอักษรที่ได้จากการ encode คือ k โดยจะทำการวนชุดตัวเลขไปเรื่อยๆจนกระทั่งทำการ encode ทุกตัวอักษรใน String ครบ ถ้าหากผลลัพธ์จากการเพิ่มหรือลดค่า ascii ไม่ใช่ตัวอักษรให้กลับมาวนในชุดตัวอักษร เช่น อักษร z ทำการ encode ด้วยเลข 2 จะได้ b และหากทำการ decode ตัวอักษร A ด้วย 2 จะได้ Y 

โดยการ decode หลังจาก encode ต้องให้คำตอบที่มีค่าเท่ากับ String เดิมก่อนทำการ encode 

***ให้ใช้วิธี enqueue และ dequeue ในการเลื่อนตำแหน่ง เท่านั้น***

โดยรูปแบบการ run ดังนี้ :

q1 = Queue(string)

q2 = Queue(number)

encodemsg(q1, q2)

decodemsg(q1, q2)
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

def encodemsg(q1,q2):
    j = 0
    k = 0
    i = 0
    while k < q1.size():
        if q1.items[i].islower():
            if (chr(ord(q1.items[i]) + int(q2.items[j]))) > 'z':    
                q1.enQueue(chr(ord(q1.items[i]) + int(q2.items[j]) - 26))
                q1.deQueue()
            else:
                 q1.enQueue(chr(ord(q1.items[i]) + int(q2.items[j])))
                 q1.deQueue()
            
        elif q1.items[i].isupper():
            if (chr(ord(q1.items[i]) + int(q2.items[j]))) > 'Z':    
                q1.enQueue(chr(ord(q1.items[i]) + int(q2.items[j]) - 26))
                q1.deQueue()
            else:
                 q1.enQueue(chr(ord(q1.items[i]) + int(q2.items[j])))
                 q1.deQueue()         
        
        j += 1
        k += 1
        if j == q2.size():
            j = 0    
        
    
    return q1.items
                
    
def decodemsg(q1,q2):
    j = 0
    k = 0
    i = 0
    while k < q1.size():
        if q1.items[i].islower():
            if (chr(ord(q1.items[i]) - int(q2.items[j]))) < 'a':    
                q1.enQueue(chr(ord(q1.items[i]) - int(q2.items[j]) + 26))
                q1.deQueue()
            else:
                 q1.enQueue(chr(ord(q1.items[i]) - int(q2.items[j])))
                 q1.deQueue()
            
        elif q1.items[i].isupper():
            if (chr(ord(q1.items[i]) - int(q2.items[j]))) < 'A':    
                q1.enQueue(chr(ord(q1.items[i]) - int(q2.items[j]) + 26))
                q1.deQueue()
            else:
                 q1.enQueue(chr(ord(q1.items[i]) - int(q2.items[j])))
                 q1.deQueue()         
        
        j += 1
        k += 1
        if j == q2.size():
            j = 0    
        
    
    return q1.items
    


String,number = input("Enter String and Code : ").split(',')
String = String.replace(' ','')
String = [i for i in String]
number = [i for i in number]

q1 = Queue(String)
q2 = Queue(number)

print('Encode message is : ',encodemsg(q1, q2))
print('Decode message is : ',decodemsg(q1, q2))

# i = 2
# if (chr(ord('z') + i) > 'z'):
#     print(chr(ord('z') + i - 26))
