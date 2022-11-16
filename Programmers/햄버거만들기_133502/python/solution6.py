def solution(ingredient):
    answer = 0
    ingredients = "".join([str(i) for i in ingredient])
    burger = "1231"
    while ingredients.find(burger) >= 0:
        answer += 1
        ingredients = ingredients.replace(burger, "", 1)
    return answer

'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (5372.90ms, 33.9MB)
테스트 4 〉	실패 (시간 초과)
테스트 5 〉	실패 (시간 초과)
테스트 6 〉	실패 (시간 초과)
테스트 7 〉	실패 (시간 초과)
테스트 8 〉	실패 (시간 초과)
테스트 9 〉	통과 (7885.59ms, 38.4MB)
테스트 10 〉	통과 (7.22ms, 10.5MB)
테스트 11 〉	통과 (3744.22ms, 30.7MB)
테스트 12 〉	실패 (시간 초과)
테스트 13 〉	통과 (0.00ms, 10.2MB)
테스트 14 〉	통과 (0.01ms, 10.2MB)
테스트 15 〉	통과 (0.01ms, 10.2MB)
테스트 16 〉	통과 (0.01ms, 10.1MB)
테스트 17 〉	통과 (0.00ms, 10.1MB)
'''