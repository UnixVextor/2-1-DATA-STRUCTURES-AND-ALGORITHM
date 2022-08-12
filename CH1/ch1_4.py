'''
Chapter : 1 - item : 4 - สนุกไปกับการวาดรูป(1)
 
เขียนภาษา Python เพื่อวาดรูปหัวใจ ซึ่งจะรับ 
input เป็นขนาดของรูปหัวใจ โดย input จะมีค่าตั้งแต่ 2 ขึ้นไป
'''
def Top_Heart(inp) :
   for i in range(inp-1):   # บรรทัด
    for j in range(inp-1-i):  # จุด "." เซท 1
        print(".", end="")
    print("*", end="")
    if i != 0:  # เช็คว่า เช็คว่าเป็นบรรทัดที่ 1 หรือไหม ถ้าไม่ พิมพ์ บวก
        for k in range((i*2)-1):  # พิมพ์บวกตามจำนวน
            print("+", end="")
        print("*", end="")      # Loop เช็คว่า พิมพ์บวกหรือไหม
      #  /////////////////////////////// #
    for j in range(((inp*2)-3)-2*i):
        print(".", end="")         # จุด "." เซท 2
        #  /////////////////////////////// #
    print("*", end="")
    if i != 0:  # เช็คว่า เช็คว่าเป็นบรรทัดที่ 1 หรือไหม ถ้าไม่ พิมพ์ บวก
        for k in range((i*2)-1):  # พิมพ์บวกตามจำนวน
            print("+", end="")
        print("*", end="")
    for j in range(inp-1-i):  # จุด "." เซท 3
        print(".", end="")
    print()
         
def Mid_Heart(inp) :
    print("*", end="")
    for j in range((inp*2)-3):
        print("+", end="")
    print("*", end="")
    for j in range((inp*2)-3):
        print("+", end="")
    print("*")

def Bottom_Heart(inp) :
    for Row in range((inp*2)-2):
        print("."*(Row+1), end="")
        print("*", end="")
        print("+"*((4*inp-5)-((Row+1)*2)), end="")
        if ((4*inp-5)-((Row+1)*2)) > 0 :
            print("*", end="")
        print("."*(Row+1))
        

if __name__ == "__main__":
    print("*** Fun with Drawing ***")
    inp = int(input("Enter input : "))
    Top_Heart(inp)
    Mid_Heart(inp)
    Bottom_Heart(inp)