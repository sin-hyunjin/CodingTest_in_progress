str = input()
def str1(n) :
    str2=""
    for s in str :
        if s.islower() == True :
            str2 += s.upper()
        else :
            str2 += s.lower()
    return str2

print(str1(str))
