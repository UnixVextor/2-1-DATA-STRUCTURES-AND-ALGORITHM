'''
จงเขียนฟังก์ชันเพื่อหาผลรวมของ 3 พจน์ใดๆใน Array ที่มีผลรวมเท่ากับ 0 
สำหรับ Array ที่มีข้อมูลข้างในเป็นจำนวนจริง ***Array ต้องมีความยาวตั้งแต่ 3 จำนวนขึ้นไป***
'''
def threesum(num):
    num.sort()
    result = []
    for i in range(0,len(num)):
        for j in range(i+1,len(num)):
            for k in range(j+1,len(num)):
                if num[i] + num[j] + num[k] == 0 and [num[i],num[j],num[k]] not in result:
                    result.append([num[i],num[j],num[k]])
    
    return result
 

List = list(input("Enter Your List : ").split())
List = [int(i) for i in List]
if len(List) > 2:
    print(threesum(List))
else:
    print("Array Input Length Must More Than 2")