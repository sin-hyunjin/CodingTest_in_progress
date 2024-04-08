def solution(strArr):
    result = []
    
    for i, s in enumerate(strArr):
        # 짝수번째 인덱스인 경우
        if i % 2 == 0:
            result.append(s.lower())  # 모두 소문자로 변환하여 추가
        else:  # 홀수번째 인덱스인 경우
            result.append(s.upper())  # 모두 대문자로 변환하여 추가
    
    return result