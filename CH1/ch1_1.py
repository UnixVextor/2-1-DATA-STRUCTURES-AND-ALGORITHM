'''
รับจำนวนเต็ม 3 จำนวนจากแป้นพิมพ์
เก็บในตัวแปร h, m และ s ซึ่งแทนจำนวน ชั่วโมง นาที และ วินาที

แล้วแสดงผลเป็น วินาที
แสดงผลตามตัวอย่าง
'''
print("*** Converting hh.mm.ss to seconds ***")
print("Enter hh mm ss :",end=' ')
hh,mm,ss = input().split()
calculateToSeconds = int(ss) + (int(mm) * 60) + (int(hh) * 3600)
str_calculateToSeconds = str(calculateToSeconds)

if int(mm) >= 60 or int(mm) < 0:
    print("mm(" + mm + ') is invalid!')
elif int(ss) >= 60 or int(ss) < 0:
    print('ss(' + ss + ') is invalid!')
else:
    hh = hh if int(hh) > 10 else '0' + hh
    mm = mm if int(mm) > 10 else '0' + mm
    ss = ss if int(ss) > 10 else '0' + ss
    if(len(str_calculateToSeconds) >= 3):
        print(str(hh) + ':' + str(mm) + ':' + str(ss) + ' = ' + str_calculateToSeconds[:len(str_calculateToSeconds) - 3] + ',' + str_calculateToSeconds[len(str_calculateToSeconds) - 3:len(str_calculateToSeconds)] + " seconds")
    else :
        print(str(hh) + ':' + str(mm) + ':' + str(ss) + ' = ' + str_calculateToSeconds + " seconds")