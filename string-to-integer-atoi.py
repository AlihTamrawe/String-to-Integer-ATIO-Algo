class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        signNumber = 1
        dig = 0
        lengthString = len(s)
        if s.count("+") >1 :
            for i in range(s.find("+"),lengthString):
                if s[i] == '+' and i<lengthString-1:
                    if i == s.find("+")+1:
                        return 0
        if s.count("-") >1:
            for i in range(s.find("-"),lengthString):
                if s[i] == '-':
                    if i == s.find("-")+1:
                        return 0
        acu = 0
        ze = 0
        if s.find("-") != lengthString-1 :
            if s.find("-") >-1 and s.find("+") ==-1:
                signNumber = -1
                for i in range(0,s.find("-")):
                    if s[i]=='0' :
                        print("ze")
                        ze = 1
                    if s[i].isnumeric() and not s[i]=='0'  :
                        acu += 1
                        signNumber = 1
                if ze ==1 and acu == 0 :
                    return 0
                for i in range(s.find("-")+1 ,lengthString):
                    print(s[i])
                    if s[i] == ' ':
                        return 0
                    else:
                        break
        if s.find("+") != lengthString-1 :
            if s.find("+") >-1 and s.find("-") ==-1:
                signNumber = 1
                if s.find("+") != 0:
                    for i in range(0,s.find("+")):
                        if s[i]=='0' :
                            return 0
                    
                

        if s.find("+")>-1 :
            for i in range(s.find("+")+1 ,lengthString):
                    if s[i] == ' ':
                        return 0
                    else:
                        break

        if s.find("-") >-1  and s.find("+") > -1:
            if abs(abs(s.find("-"))-abs(s.find("+"))) ==1  :
                print(s.find("-") , " ", s.find("+"))
                return 0
            if abs(s.find("-"))<abs(s.find("+")):
                signNumber = -1
            
        
        re = 0
        pos = 0
        index = 0
        for num in s:
            if num =="+" or  num =="-"  :
                if re > 0 :
                    print(num , " ", re)
                    break
            if  num == " " and  not re==0 :
                break
            index+=1
            if num == "." :
                break
            if num.isnumeric():
                re += int(num)
                if re>0:
                    dig+=1
                else:
                    pos = index
            else:
                if  num !="-" and num != " "and num !="+":
                    
                    if num.isalpha() and re>0 :
                        break
                    if dig == 0:
                        break


        dig = pow(10,dig-1)


        print("dig")


        result = 0
        index = 0
        f = False
        for num in s:
            index +=1
            if num =="+" or  num =="-"  :
                if result > 0 :
                    print(num , " ", result)
                    break
            if  num == " " and  dig == 1 and not result == 0 :
                return 0
            if  num == " " and  not result==0 :
                break
            if num == ".":
                break
            if num.isalpha() :
                break
            if result <= 0 and f and  num == " " :
                return 0
            
            if result <= 0 and num == "0":
                print("zero")
                f=True
                continue
            if num.isnumeric() and index>pos :
                x = int(num)
                x = x*dig
                result +=x
                dig/=10
        if result> 2147483647:
            if signNumber == -1:
                result = 2147483648
            else:
                result = 2147483647


        return result*signNumber
