def solution(myString, pat):
    # 문자열 myString에서 "A"를 "B"로, "B"를 "A"로 바꾼다.
    new_string = myString.replace("A", "x").replace("B", "A").replace("x", "B")
    
    # pat이 존재하는지 확인
    for i in range(len(new_string) - len(pat) + 1):
        if new_string[i:i+len(pat)] == pat:
            return 1
    return 0