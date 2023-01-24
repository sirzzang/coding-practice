package main

// import "fmt"

func sum(arr [10000]int) int {
	s := 0
	for _, v := range arr {
		s += v
	}
	return s
}

func count(topping []int, result *[10000]int, doneChan chan bool) {
	for _, v := range topping {
		if result[v-1] == 0 {
			result[v-1] = 1
		}
	}
	doneChan <- true
}

func solution(topping []int) int {

	answer := 0

	// 완전탐색
	split := [2][10000]int{}
	for i := 0; i < len(topping); i++ {

		cheolsu := make(chan bool)
		brother := make(chan bool)

		go count(topping[:i+1], &split[0], cheolsu)
		<-cheolsu

		go count(topping[i+1:], &split[1], brother)
		<-brother

		// for _, v := range(topping[:i+1]) {
		//     if split[0][v-1] == 0 {
		//         split[0][v-1] = 1
		//     }
		// }

		// for _, v := range(topping[i+1:]) {
		//     if split[1][v-1] == 0 {
		//         split[1][v-1] = 1
		//     }
		// }

		if sum(split[0]) == sum(split[1]) {
			answer++
		}

		split = [2][10000]int{}
	}

	return answer
}

/**
정확성  테스트
테스트 1 〉	통과 (390.78ms, 5.62MB)
테스트 2 〉	실패 (시간 초과)
테스트 3 〉	실패 (시간 초과)
테스트 4 〉	실패 (시간 초과)
테스트 5 〉	실패 (시간 초과)
테스트 6 〉	실패 (시간 초과)
테스트 7 〉	실패 (시간 초과)
테스트 8 〉	실패 (시간 초과)
테스트 9 〉	실패 (시간 초과)
테스트 10 〉	실패 (시간 초과)
테스트 11 〉	실패 (시간 초과)
테스트 12 〉	통과 (383.07ms, 5.53MB)
테스트 13 〉	실패 (시간 초과)
테스트 14 〉	실패 (시간 초과)
테스트 15 〉	실패 (시간 초과)
테스트 16 〉	실행 중단
테스트 17 〉	실행 중단
테스트 18 〉	실행 중단
테스트 19 〉	실행 중단
테스트 20 〉	실행 중단
*/
