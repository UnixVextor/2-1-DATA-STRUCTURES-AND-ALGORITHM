'''
ให้เรียงลำดับ input ที่รับเข้ามาจากน้อยไปมาก โดยเรียงลำดับจากตัวอักษรที่มีอยู่ในแต่ละ string โดยตัวอักษรจะมีแค่ a - z เท่านั้น และในแต่ละ string จะมี alphabet เพียงแค่ 1 ตัวเท่านั้น

****** ห้ามใช้ Built-in Function ที่เกี่ยวกับ Sort ให้น้องเขียนฟังก์ชัน Sort เอง
'''
def findAlphabet(str):
    for i in range(len(str)):
        if str[i] >= 'a' and str[i] <= 'z':
            return ord(str[i])

def Sort(l):
    n_l = list()
    for i in range(len(l)):
        n_l.append(findAlphabet(l[i]))
    for j in range(1, len(n_l)):
        iEle = n_l[j]
        iELe = l[j]
        for k in range(j, -1 ,-1):
            if iEle < n_l[k-1] and k > 0:
                n_l[k] = n_l[k-1]
                l[k] = l[k-1]
            else:
                n_l[k] = iEle
                l[k] = iELe
                break
    return n_l,l

        
inp = input("Enter Input : ").split()
x,y = Sort(inp)
# print(x)
for i in y:
    print(i, end = ' ')

        