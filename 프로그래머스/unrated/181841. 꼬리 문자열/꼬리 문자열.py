def solution(str_list, ex):
    tail_string = ""  # 꼬리 문자열 초기화

    for string in str_list:
        if ex not in string:
            tail_string += string  # ex를 포함하지 않는 문자열을 꼬리 문자열에 추가

    return tail_string