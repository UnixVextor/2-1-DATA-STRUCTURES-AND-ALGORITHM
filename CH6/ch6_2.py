'''
จงเขียนฟังก์ชั่นสำหรับการเรียงค่าใน List ของจำนวนเต็มโดยจะเรียงค่าจากมากไปน้อย

****ห้ามใช้ for/while และฟังก์ชั่นอื่นๆในการวนลูป ให้ใช้ recursion ในการเขียนเท่านั้น****
'''
def findmaxIndex(ll,mx =0,i = 0):
    if i == len(ll):
        return mx
    if int(ll[i]) > int(ll[mx]):
        return findmaxIndex(ll,i,i+1)
    else:
        return findmaxIndex(ll,mx,i+1)
    

def Sort(ll,r = []):
    if len(ll) == 0:
        return r
    r.append(int(ll.pop(findmaxIndex(ll))))
    return Sort(ll,r)

inp = input('Enter your List : ').split(',')
inp = [int(i) for i in inp]
print('List after Sorted : ', end='')
print(Sort(inp))