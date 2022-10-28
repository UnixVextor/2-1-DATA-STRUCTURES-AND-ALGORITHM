'''
เขียน function insertion sort เพื่อเรียงข้อมูลใน list จากน้อยไปมาก โดยใช้ recursive

และแสดงขั้นตอนของ insertion sort ตามตัวอย่าง

***ห้ามใช้ คำสั่งloopต่างๆ เช่น for ,while หรือ Built-in Function ที่เกี่ยวกับ Sort เช่น .sort***

*** ยกเว้นให้ใช้  for ได้แค่ขั้นตอนรับ input เท่านั้น ***
'''
def insertion_index(l, curr_index, value):
    if curr_index > 0 and l[curr_index - 1] > value:
        l[curr_index] = l[curr_index - 1]
        return insertion_index(l,curr_index - 1,value)
    else:
        return curr_index

def insertion_sort(l, start = 0,length = None, progress = 0):
    if length == None:
        length = len(l)
    
    value = l[start]
    
    index = insertion_index(l,start,value)
    l[index] = value
    progress += 1
    
    if progress > 1:
        if len(l[progress:]) != 0:
            print(f"insert {value} at index {index} : {l[:progress]} {l[progress:]}")
        else:
            print(f"insert {value} at index {index} : {l[:progress]}")
    
    if start+1 < length:
        insertion_sort(l,start+1,length,progress)

if __name__ == "__main__":
    inp = list(map(int,input("Enter Input : ").split()))
    insertion_sort(inp)
    print("sorted")
    print(inp)
    