def decimalToBinary(num,count):
    if len(bin(num).replace("0b", "")) < count:
        s = count - len(bin(num).replace("0b",""))
        return ('0'*s) + str(bin(num).replace("0b", ""))
    else:
        return bin(num).replace('0b','')
'''
****** ห้ามใช้ For , While  ( ให้ฝึกเอาไว้ เนื่องจากถ้าเจอตอนสอบจะได้ 0 )

เขียน Recursive เพื่อหาว่าเลขตั้งแต่ 0 จนถึง ( 2^(input) ) - 1 นั้นมีตัวอะไรบ้าง  หากเป็นเลขติดลบให้แสดงผลเป็น Only Positive & Zero Number ! ! ! 

*** ตัวอย่างเช่น ถ้าหาก input = 2 ก็ต้องแสดงผลลัพธ์เป็น 00 , 01 , 10 , 11
'''

def printBinary(n,i=0):
    t = (2**n) - 1
    if i <= t:
        print(decimalToBinary(i,n))
        printBinary(n,i+1)   

if __name__ == '__main__':
    inp = int(input('Enter Number : '))
    if inp >= 0:
        printBinary(inp)
    else:
        print('Only Positive & Zero Number ! ! !')