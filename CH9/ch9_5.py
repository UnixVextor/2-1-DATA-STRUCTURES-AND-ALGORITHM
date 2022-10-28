'''
ให้น้องรับ input มา 2 อย่างโดยคั่นด้วย /

1. ด้านซ้าย เป็นผลลัพธ์
2. ด้านขวา เป็น list ของจำนวนเต็ม

โดยผลลัพธ์ให้แสดงเป็น subset ของ input ด้านขวาที่มีผลรวมได้เท่ากับ input ด้านซ้าย และมี Pattern การแสดงผลลัพธ์ดังนี้

1. ให้เรียงลำดับจากขนาดของ subset จากน้อยไปมาก
2. ถ้าหาก subset มีขนาดเท่ากันให้เรียงลำดับจำนวนเต็มใน subset จากน้อยไปมาก

ถ้าหากไม่มี subset ไหนที่ผลรวมเท่ากับ input ด้านซ้าย ให้แสดงว่า No Subset



****** ห้ามใช้ Built-in Function ที่เกี่ยวกับ Sort ให้น้องเขียนฟังก์ชัน Sort เอง และห้าม Import
'''
ans = []
selec = []
def subset(m,n,compare,l):
    if m == n:
        lst = []
        sum = 0
        for i in range(len(selec)):
            if selec[i] == 1:
                lst.append(l[i])
                sum += l[i]
            
        if sum == compare:
            ans.append(lst)
        return
    selec[m] = 0
    subset(m+1,n,compare,l)
    selec[m] = 1
    subset(m+1,n,compare,l)
        
def select_sort(inp):
    for i in range(len(inp)):
        min_idx = i
        for j in range(i+1,len(inp)):
            if inp[j] < inp[min_idx]:
                min_idx = j
        inp[min_idx],inp[i] = inp[i], inp[min_idx]
    return inp
      
def select_sort_with_len(inp):
    for i in range(len(inp)):
        min_idx = i
        for j in range(i+1,len(inp)):
            if len(inp[j]) < len(inp[min_idx]):
                min_idx = j
        inp[min_idx],inp[i] = inp[i], inp[min_idx]
    return inp

        
def select_sort_samelen(inp):
    for i in range(len(inp)):
        min_idx = i
        for j in range(i+1,len(inp)):
            if len(inp[j]) == len(inp[min_idx]):
                if compareValuem_more_n(inp[min_idx], inp[j]):
                    min_idx = j
        inp[min_idx],inp[i] = inp[i], inp[min_idx]
    return inp

def compareValuem_more_n(m,n):
    for i in range(len(m)):
        if m[i] > n[i]:
            return True
        elif m[i] < n[i]:
            return False
    return False

if __name__ == "__main__":
    # inp = "2/-2 3 1 -1 0 -3 2".split("/")
    inp = input("Enter Input : ").split('/')
    r_inp = list(map(int, inp[1].split()))
    r_inp = select_sort(r_inp)

    selec = [0]*len(r_inp)
    subset(0,len(r_inp),int(inp[0]),r_inp)
    
    for x in select_sort_samelen(select_sort_with_len(ans)):
        print(x)
    if len(ans) == 0:
        print("No Subset")
