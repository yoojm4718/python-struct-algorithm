def med3(a, b, c):
    if (b >= a and a >= c) or (c >= a and a >= b):
        return a
    elif (a > b and b > c) or (c > b and b > a):
        return b
    else:
        return c

a = int(input("정수 a의 값을 입력하세요: "))
b = int(input("정수 b의 값을 입력하세요: "))
c = int(input("정수 c의 값을 입력하세요: "))

print(f"중앙값은 {med3(a, b, c)}입니다.")