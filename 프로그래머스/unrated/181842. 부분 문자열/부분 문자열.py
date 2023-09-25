def solution(str1, str2):
    answer = 0
    isFound = str1 in str2
    if isFound:
        answer = 1

    return answer