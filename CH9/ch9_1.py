'''
เขียน function bubble sort เพื่อเรียงข้อมูลใน list จากน้อยไปมาก โดยใช้ recursive

***ห้ามใช้ คำสั่งloopต่างๆ เช่น for ,while หรือ Built-in Function ที่เกี่ยวกับ Sort เช่น .sort***

*** ยกเว้นให้ใช้  for ได้แค่ขั้นตอนรับ input เท่านั้น ***

'''
def bublesort(l,m = None,n=None):
    if n is None and m is None:
        n = len(l)
        m = len(l)
        
    if n == 1 or m == 1:
        if m != 1:
            n = m - 1
        return
     
    if n > 1:
        if l[len(l) - n] > l[len(l) - n + 1]:
            l[len(l) - n], l[len(l) - n +1] = l[len(l) - n + 1],l[len(l) - n]
        bublesort(l,m,n - 1)  
    bublesort(l,m-1,n)
    return l     

if __name__ == "__main__":
    inp = [int(i) for i in input("Enter Input : ").split()]
    sort = bublesort(inp)
    print(sort)

