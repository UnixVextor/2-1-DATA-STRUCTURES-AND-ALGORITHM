'''
ให้นักศึกษาเขียนโปรแกรมภาษา Python โดยใช้ Function ในการหาตำแหน่ง คู่ กับ คี่ จาก List และ String

def odd_even(type, data, mode):
    //Code Here

โดยที่รูปแบบการรับ Input ตำแหน่งแรกจะเป็นตัวบอกว่าเป็น String หรือ List ถ้าใส่ S = String ถ้าใส่ L = List

Input ตำแหน่งที่สองเป็นค่าใน String หรือ List ที่นำเข้ามา

Input ตำแหน่งที่สามเป็นการบอกว่าจะแสดงตำแหน่งคู่หรือคี่ ถ้าใส่ Odd = คี่ ถ้าใส่ Even = คู่
'''
def odd_even(arr,s):
    global back
    if isinstance(arr,(list)):
        back = []
    elif isinstance(arr,(str)):
        back = ''
    if s == 'Odd' and isinstance(arr,(str)):
        for i in range(0,len(arr),2):
            back += arr[i]
        return back
    elif s == 'Even' and isinstance(arr,(str)):
        for i in range(1,len(arr),2):
            back += arr[i]
        return back

    if s == 'Odd' and isinstance(arr,(list)):
        for i in range(0,len(arr),2):
            back.append(arr[i])
        return back
    elif s == 'Even' and isinstance(arr,(list)):
        for i in range(1,len(arr),2):
            back.append(arr[i])
        return back



print("*** Odd Even ***")
x = input("Enter Input : ").split(',')
global arr
if x[0] == 'S':
    arr = ''
    arr = x[1]
elif x[0] == 'L':
    arr = []
    arr = x[1].split(' ')  

# print(arr)  
# print(type(arr))
print(odd_even(arr,x[2]))