def add(a, b):
    return a + b

t = int(input())  # number of test cases

for _ in range(t):
    a, b = map(int, input().split())
    print(add(a, b))
