def solution(numer1, denom1, numer2, denom2):
    boonmo = 0
#     최소공배수
    for i in range(max(denom1, denom2), (denom1 * denom2) + 1): 
        if i % denom1 == 0 and i % denom2 == 0:
            boonmo = int(i)
            break
            
    boonja = int((boonmo / denom1) * numer1 + (boonmo / denom2) * numer2)
    
#     최대공약수
    for n in range(min(boonja,boonmo),0,-1): 
        if boonmo%n == 0 and boonja%n == 0:
            boonmo /= n
            boonja /= n
            break
    
    
    answer = [int(boonja), int(boonmo)]
    
    return answer