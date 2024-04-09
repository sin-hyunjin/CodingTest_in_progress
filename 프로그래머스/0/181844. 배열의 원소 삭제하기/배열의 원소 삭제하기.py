def solution(arr, delete_list):
    # delete_list에 포함되지 않은 원소들로 이루어진 새로운 배열 생성
    result = [x for x in arr if x not in delete_list]
    return result
