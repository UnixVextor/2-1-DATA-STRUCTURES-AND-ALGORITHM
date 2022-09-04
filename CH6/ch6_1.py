'''
****** ห้ามใช้ For , While  ( ให้ฝึกเอาไว้ เนื่องจากถ้าเจอตอนสอบจะได้ 0 )

ให้เขียน Recursive หาค่า Min ของ Input
'''
def mini(ll,index):
    if index == 0:
        return ll[index]
    else:
        return min(ll[index],mini(ll,index - 1))

inp = input('Enter Input : ').split()
inp = [int(i) for i in inp]
print('Min :', mini(inp,len(inp)-1))