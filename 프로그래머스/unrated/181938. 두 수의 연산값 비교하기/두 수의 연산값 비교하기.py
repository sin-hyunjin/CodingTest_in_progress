def solution(a, b):
    answer = int(f'{a}{b}')
    num = 2 * a * b
    if answer >= num:
        return answer
    else:
        return num

