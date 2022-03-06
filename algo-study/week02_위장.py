def solution(clothes):
    
    # 의상 종류별 의상 개수 저장
    clothes_dict = {}
    for clothe in clothes:
        c_type = clothe[-1]
        if c_type in clothes_dict:
            clothes_dict[c_type] += 1
        else:
            clothes_dict[c_type] = 1
    
    # 경우의 수
    answer = 1
    for v in clothes_dict.values():
        answer *= (v+1)

    return answer-1

'''
다른 풀이
- counter로 의상 개수 세 주기
- reduce 함수 사용: 마지막 파라미터 없을 경우 iterable[0]이 초깃값
'''
def solution(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer