t = int(input("Enter No of iterations or testcases:"))

for i in range(t):
    try:
        a,b=input("Enter a,b:").split()
        print(int(a)//int(b))
    except (ZeroDivisionError, ValueError) as e:
        print("Error:",e)
