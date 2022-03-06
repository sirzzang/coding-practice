# 시간 더 걸림
n = int(input())
numbers = input()
print(sum(map(int, numbers)))

# 왜 시간 덜 걸린담?
n = int(input())
total = 0
for number in numbers:
    total += int(number)
print(total)