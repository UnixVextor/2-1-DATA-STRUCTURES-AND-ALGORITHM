'''
รับ input จำนวนเต็มสองจำนวน หากผลคูณของทั้งสองจำนวนมีค่าเกิน 1000 
ให้ show ผลรวมของจำนวนทั้งสอง แต่หากผลคูณมีค่าน้อยกว่าหรือเท่ากับ 1,000 ให้ show ผลคูณของจำนวนทั้งสอง
'''
print("*** multiplication or sum ***")
num1,num2 = input("Enter num1 num2 : ").split()

if int(num1) * int(num2) > 1000:
    print("The result is " + str(int(num1) + int(num2)))
else :
    print("The result is " + str(int(num1) * int(num2)))