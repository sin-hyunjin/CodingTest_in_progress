def solution(code):
    answer = ""
    mode = True
    
    for i in range(len(code)):
        if mode:
            if code[i]!="1" and i%2==0:
                answer += code[i]
            elif code[i] == "1" :
                mode = False
        else:
            if code[i]!="1" and i%2==1:
                answer += code[i]
            elif code[i] == "1":
                mode = True
    if answer == "":
        return "EMPTY"
    
    return answer