'''
เขียน function Straight Selection Sort เพื่อเรียงข้อมูลใน list จากน้อยไปมาก โดยใช้ recursive

และแสดงขั้นตอนของ Straight Selection Sort ตามตัวอย่าง

***ห้ามใช้ คำสั่งloopต่างๆ เช่น for ,while หรือ Built-in Function ที่เกี่ยวกับ Sort เช่น .sort***

*** ยกเว้นให้ใช้  for ได้แค่ขั้นตอนรับ input เท่านั้น ***
'''
def FindMaxIndex(l, m, n):
    if m == n:
        return m
    k = FindMaxIndex(l,m+1,n)
    
    return (m if l[m] > l[k] else k)
    
def SelectionSort(l, i, index = 0):
    if i == index:
        return -1
    
    k = FindMaxIndex(l,index,i-1)
    
    if k!= i-1:
        l[i-1],l[k] = l[k], l[i-1]
        print("swap {1} <-> {0} : {2}".format(l[i-1],l[k],l))
        
    SelectionSort(l,i-1,index)

if __name__ == "__main__":
    inp = list(map(int,input("Enter Input : ").split()))
    SelectionSort(inp, len(inp))
    print(inp)
    
    