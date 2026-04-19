with open("addinput.txt", "r") as file:
    lines = file.readlines()

t = int(lines[0].strip()) #testcases

index = 1
for _ in range(t):
    a, b = map(int, lines[index].split())
    print(a + b)
    index += 1
