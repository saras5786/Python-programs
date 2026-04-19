def compute_average(a, b):
    return (a + b) // 2

t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    print(compute_average(a, b))
