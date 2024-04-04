def solution(names):
    result = []
    
    # 리스트를 5명씩 묶어서 처리
    for i in range(0, len(names), 5):
        result.append(names[i])
    
    return result