# 햄버거 만들기

## Python

- [Solution1](python/solution1.py): 시간 초과
    - 먼저 쌓인 재료부터 빼야 하므로 deque 이용: `popleft` 시간복잡도 O(1)
    - 기본적으로 `ingredient` 배열에 있는 모든 원소 한 번씩 다 검사해야 하기 때문에 O(n)
    - 검사하는 와중에 `stack`과 `burger` 리스트를 비교해야 하는 건 좋지 못함
    - 어차피 O(n)으로 가려면
        1. 훑는 동시에 햄버거 리스트가 있는지 탐색하는 건 어떨까
        2. `burger` 리스트 비교 말고 다른 방식으로 비교하는 건 어떨까
- [Solution2](python/solution2.py)
    - [Solution1](python/solution1.py)에서 비교 방식만 리스트에서 문자열로 바꿨을 뿐인데 통과됨
- [Solution3](python/solution3.py): 시간 초과
    - 애초에 [Soluton1](python/solution1.py)에서 deque을 이용할 필요가 없었으며, `len(stack) >= 4` 검사를 하지 않아도 되었음
    - 그런데 시간 초과. `stack = stack[:-4]` 이 부분이 문제일까?
- [Solution4](python/solution4.py)
    - 리스트 슬라이싱해서 재할당하는 부분을 `pop`으로 바꿨더니 통과
    - 결과적으로 위의 풀이들에서는 `stack = stack[:-4]` 이 부분이 문제였을 수도 있지 않을까?
- [Solution5](python/solution5.py)
    - 애초에 재료, 햄버거 모두 문자열로 만들어서 찾고자 하는 햄버거 문자열이 있으면 빼내면 되지 않을까?
    - `String.replace()` 메서드 사용
        - 원본 문자열을 바꾸지 않으므로, 바꾼 문자열 재할당 해줘야 함
        - `String.replace()` 메서드 써 버리면, 찾은 문자열 모두 바꿔 버림
            - [1, 1, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1]의 경우, 3개가 만들어 져야 하는데, "1231" 모두 바꿔서 1개 밖에 못 찾음
- [Solution5](python/solution6.py): 시간 초과
    - [Solution4](python/solution5.py)에서 `String.replace()` 메서드 세 번째 파라미터 `count`를 이용

<br>

## Java

- [Solution1](java/Solution1.java): Python [Solution4](python/solution4.py)와 동일한 로직
    - Stack 자료구조 이용하는 과정에서 autoboxing 발생
    - `Stack.subList()` 메서드 이용 시 파이썬에서와 달리 startIndex를 -4로 설정하면 `ArrayOutOfBoundsException` 발생
    - 햄버거 만들 수 있는지 굳이 ArrayList를 이용해서 비교해야 할까?
- [Solution2](java/Solution2.java): 시간 초과
    - [Solution1](java/Solution1.java)에서 비교 시 String을 이용해 보고자 함. [Python Solution2](python/solution2.py) 아이디어의 적용 의도
    - `String`을 계속 사용하면 새로운 객체가 생성되므로, `StringBuilder`를 이용해 동일한 논리를 적용하고자 했는데, 시간 초과
        - `indexOf`, `delete` 메서드를 사용한 로직 구현이 별로 좋지 않은가?

<br>

## TODO
- [ ] Python 리스트 비교 vs. 문자열 비교, 리스트 비교 부담이 얼마나 되는지
- [ ] Python 리스트 슬라이싱해서 다시 할당하는 거가 pop에 비해 부담인가?
- [ ] Python `str.replace` 메서드 효율성?
- [ ] Java `ArrayList` 동치 어떻게 판단? `equals` 확인
- [ ] Java `StringBuilder` `indexOf`, `delete` 메서드 구현?

