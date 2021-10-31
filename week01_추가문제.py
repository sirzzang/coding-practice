def binary_search(array, target):
    array.sort() # 정렬
    
    left = 0
    right = len(array)-1
    
    while left <= right:
        mid = (left + right)//2 # 가운데 인덱스
        if array[mid] == target: # 찾는 값을 만나면 반환
            return mid 
        elif array[mid] > target: # 가운데 값이 더 크면 왼쪽 구간으로 이동
            right = mid-1 
        else: # 가운데 값이 더 작으면 오른쪽 구간으로 이동
            left = mid+1
    
    return None # 찾는 값이 없을 때


if __name__ == '__main__':
    print(binary_search([-12, -2, 3, 10, 120], 3))
    print(binary_search([-12, -2, 3, 10, 120], 10))


