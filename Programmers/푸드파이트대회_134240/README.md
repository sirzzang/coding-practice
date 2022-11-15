# 푸드파이트대회

## Java
- Int -> String, String -> Int
- 문자열 반복
- [Soluton1](java/Solution1.java)
    - `String` 객체 계속해서 생성됨
    - 반대로 붙이기 위해 `forward`, `backward`를 구현할 필요가 있을까?
- [Solution2](java/Solution2.java)
    - `StringBuffer` 이용
    - 반대로 붙이기 위해 `StringBuffer`의 `reverse` 이용해 보려 하였으나, 원본 객체 변경됨
- [Solution3](java/Solution3.java)
    - 반대로 붙이기 위해 기존 `StringBuffer` 문자열에 `0`을 붙인 값을 변수에 저장해둔 후, `StringBuffer`의 `reverse` 메서드 이용
    - 그러나 결과적으로 `String`에 `String`을 이어 붙인 셈