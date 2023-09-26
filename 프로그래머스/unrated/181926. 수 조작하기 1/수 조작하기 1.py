# def solution(n, control):
#     for i in control:
#         if i in "w" :
#             n += 1
#         if i in "s" : 
#             n -= 1
#         if i in "d" :
#             n += 10
#         if i in "a" :
#             n -= 10
#     return n
def solution(n, control):
    answer = n
    c = { 'w':1, 's':-1, 'd':10, 'a':-10}
    for i in control:
        answer += c[i]
    return answer