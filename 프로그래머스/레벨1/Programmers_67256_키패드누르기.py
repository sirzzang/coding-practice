def distance(_from: tuple, _to: tuple) -> int:
    return abs(_from[0] - _to[0]) + abs(_from[1] - _to[1])

def solution(numbers, hand):
    keypad = {
        1: (0, 0),
        2: (0, 1),
        3: (0, 2),
        4: (1, 0),
        5: (1, 1),
        6: (1, 2),
        7: (2, 0),
        8: (2, 1),
        9: (2, 2),
        '*': (3, 0),
        0: (3, 1),
        '#': (3, 2)
    }
    answer = ''
    L, R = keypad['*'], keypad['#']
    for number in numbers:
        # 왼쪽 열
        if number in [1, 4, 7]:
            L = keypad[number]
            answer += 'L'
        # 오른쪽 열
        elif number in [3, 6, 9]:
            R = keypad[number]
            answer += 'R'
        # 가운데 열
        else:
            L_distance = distance(L, keypad[number])
            R_distance = distance(R, keypad[number])
            # 왼손 엄지손가락이 이동하는 게 더 빠른 경우
            if L_distance < R_distance:
                L = keypad[number]
                answer += 'L'
            # 오른손 엄지손가락이 이동하는 게 더 빠른 경우
            elif L_distance > R_distance:
                R = keypad[number]
                answer += 'R'
            # 두 엄지손가락까지 거리가 같은 경우
            else:
                if hand == 'left':
                    L = keypad[number]
                    answer += 'L'
                else:
                    R = keypad[number]
                    answer += 'R'        
        
    return answer