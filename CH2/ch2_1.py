'''
จงเขียนฟังชั่นแปลง เลขอารบิกเป็นเลขโรมัน และ เลขโรมันเป็นอารบิกโดยที่

M=1000    CM=900    D=500    CD=400,

C=100    XC=90    L=50    XL=40,

X=10    IX=9    V=5    IV=4    I=1

เช่น 197 = 100 + 90 +7 = 100 + 90 + 5 + 1 + 1 = C XC V I I
'''
RomanSymbol = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
RomanValue = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
roman_dict ={'I': 1, 'V': 5,
             'X': 10, 'L': 50,
             'C': 100, 'D': 500,
             'M': 1000}
class translator:

    def deciToRoman(self, num):
        List = []
        count = 0
        while num > 0:
            for i in range(len(RomanSymbol)):

                if num // RomanValue[i] != 0:
                    count = num // RomanValue[i]
                    num -= RomanValue[i] * (num//RomanValue[i])
                    for j in range(count):
                        # print(RomanSymbol[i])
                        List.extend(RomanSymbol[i])
                    # print(count)
                    # print(num)
        
        return ''.join(List)


    def romanToDeci(self, s):
        global roman_dict
        roman_back = list(reversed(list(s)))
        value = 0
        
        right_val = roman_dict[roman_back[0]]  
        for numeral in roman_back:
            left_val = roman_dict[numeral]

            if left_val < right_val:
                value -= left_val
            else:
                value += left_val
            right_val = left_val
        return value

    
        

num = int(input("Enter number to translate : "))

print(translator().deciToRoman(num))

print(translator().romanToDeci(translator().deciToRoman(num)))