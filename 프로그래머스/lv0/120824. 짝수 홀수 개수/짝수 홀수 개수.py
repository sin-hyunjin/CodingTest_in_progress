def solution(num_list):
    s = 0
    k = 0
    for i in num_list:
        if i%2 == 0:
            s += 1
            answer = [s,k]
        else:
            k += 1
            answer = [s,k]
            
    return answer