'''
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.3MB)
테스트 2 〉	통과 (0.02ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.3MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.07ms, 10.3MB)
테스트 6 〉	통과 (0.07ms, 10.2MB)
테스트 7 〉	통과 (0.05ms, 10.3MB)
테스트 8 〉	통과 (0.04ms, 10.3MB)
테스트 9 〉	통과 (0.02ms, 10.3MB)
테스트 10 〉	통과 (0.08ms, 10.3MB)
테스트 11 〉	통과 (0.02ms, 10.3MB)
테스트 12 〉	통과 (0.05ms, 10.3MB)
테스트 13 〉	통과 (0.07ms, 10.3MB)
테스트 14 〉	통과 (0.08ms, 10.4MB)
테스트 15 〉	통과 (0.02ms, 10.3MB)
'''


def solution(genres, plays):
    answer = []

    # 장르별 노래 고유 번호, 재생 횟수 저장
    songs_dict = {}
    for i, v in enumerate(genres):
        if v in songs_dict:
            songs_dict[v].append((i, plays[i]))
        else:
            songs_dict[v] = [(i, plays[i])]

    # 장르 총 재생 횟수에 따라 저장한 dict 정렬
    sorted_by_genre = sorted(songs_dict.values(),
                             key=lambda x: list(map(sum, zip(*x)))[-1],
                             reverse=True)

    # 노래 수록
    for s in sorted_by_genre:
        # 장르에 속한 노래가 1개인 경우
        if len(s) == 1:
            answer.append(s[0][0])
            continue

        # 노래 재생 횟수에 따라 정렬 후 2개까지만 수록
        s.sort(key=lambda x: x[1], reverse=True)
        answer.append(s[0][0])
        answer.append(s[1][0])
    return answer
