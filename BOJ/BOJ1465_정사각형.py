class Point:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)


class Square:
    def __init__(self, p1, p2, p3, p4):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4

    def is_square(self):

        # 12, 13이 90도를 이루는 경우
        if distance(self.p1, self.p2) == distance(self.p1, self.p3)\
            and distance(self.p1, self.p4) == 2 * distance(self.p1, self.p2):
            return int(distance(self.p2, self.p3) == \
                       2 * distance(self.p2, self.p4))

        # 12, 14가 90도인 경우
        if distance(self.p1, self.p2) == distance(self.p1, self.p4)\
            and distance(self.p1, self.p3) == 2 * distance(self.p1, self.p2):
            return int(distance(self.p2, self.p4) == \
                       2 * distance(self.p2, self.p3))

        # 13, 14가 90도인 경우
        if distance(self.p1, self.p3) == distance(self.p1, self.p4)\
            and distance(self.p1, self.p2) == 2 * distance(self.p1, self.p3):
            return int(distance(self.p3, self.p4) == \
                       2 * distance(self.p2, self.p3))

        return 0


def distance(a, b):
    return (a.x - b.x) ** 2 + (a.y - b.y) ** 2 # 제곱근 하면 실수로 계산되어서 틀릴 수도

if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        p1 = input().split()
        p1 = Point(p1[0], p1[1])
        p2 = input().split()
        p2 = Point(p2[0], p2[1])
        p3 = input().split()
        p3 = Point(p3[0], p3[1])
        p4 = input().split()
        p4 = Point(p4[0], p4[1])
        s = Square(p1, p2, p3, p4)
        print(s.is_square())