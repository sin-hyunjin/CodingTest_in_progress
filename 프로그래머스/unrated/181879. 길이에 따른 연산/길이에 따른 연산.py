def solution(num_list):
    answer = 1
    answer0 = 0
    if len(num_list) > 10:
        for i in num_list:
            answer0 += i
        return answer0
    else :
        for i in num_list:
            answer *= i
        return answer