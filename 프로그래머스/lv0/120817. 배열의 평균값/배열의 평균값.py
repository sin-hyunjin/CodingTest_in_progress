def solution(numbers):
    answer = sum(numbers)/len(numbers)
    decimal =int((answer*10)%10)
    if decimal == 5 or decimal == 0:
        return answer
    else:
        return round(answer,0)
    return answer