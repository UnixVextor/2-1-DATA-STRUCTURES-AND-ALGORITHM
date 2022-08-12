'''
ตึกลึกลับแห่งหนึ่งเมื่อเดินไปข้างหลังจะมีคนบอกรหัสลับมาจงสร้างฟังชั่นคำนวณรหัส
โดยรหัสจะประกอบไปด้วย english word that have repeat character
เช่น bon("ball") = 48 หรือ bon("aah") = 4
'''
def bon(w):
    temp = w[0]
    count = 0
    repeat = ''
    i = 0 
    while i != len(w):
        if temp == w[i]:
            count += 1
        else:
            temp = w[i]
            i -= 1
            count = 0
        if count > 1:
            return (ord(temp) - 96)*4
        i += 1


secretCode = input("Enter secret code : ")
print(bon(secretCode))
# bon(secretCode)
# print(ord("a"))