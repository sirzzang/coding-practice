package main

// import "fmt"

func sum(arr [10000]int) int {
	s := 0
	for _, v := range arr {
		s += v
	}
	return s
}

func solution(topping []int) int {

	answer := 0

	// 완전탐색
	split := [2][10000]int{}
	for i := 0; i < len(topping); i++ {
		for _, v := range topping[:i+1] {
			if split[0][v-1] == 0 {
				split[0][v-1] = 1
			}
		}

		for _, v := range topping[i+1:] {
			if split[1][v-1] == 0 {
				split[1][v-1] = 1
			}
		}

		if sum(split[0]) == sum(split[1]) {
			answer++
		}

		split = [2][10000]int{}
	}

	return answer
}

/**
정확성  테스트
테스트 1 〉	통과 (321.07ms, 4.16MB)
테스트 2 〉	실패 (시간 초과)
테스트 3 〉	통과 (8280.37ms, 5.64MB)
테스트 4 〉	통과 (8303.63ms, 5.77MB)
테스트 5 〉	실패 (시간 초과)
테스트 6 〉	실패 (시간 초과)
테스트 7 〉	실패 (시간 초과)
테스트 8 〉	실패 (시간 초과)
테스트 9 〉	실패 (시간 초과)
테스트 10 〉	실패 (시간 초과)
테스트 11 〉	통과 (7790.33ms, 5.71MB)
테스트 12 〉	통과 (289.35ms, 3.66MB)
테스트 13 〉	실패 (시간 초과)
테스트 14 〉	실패 (시간 초과)
테스트 15 〉	실패 (시간 초과)
테스트 16 〉	실패 (시간 초과)
테스트 17 〉	실패 (시간 초과)
테스트 18 〉	실패 (시간 초과)
테스트 19 〉	실패 (시간 초과)
테스트 20 〉	실패 (시간 초과)
*/
