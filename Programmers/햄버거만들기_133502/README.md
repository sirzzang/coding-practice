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


## TODO
- [ ] Python 리스트 비교 vs. 문자열 비교, 리스트 비교 부담이 얼마나 되는지

