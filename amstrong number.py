num=int(input("Enter an number:"))
temp=num
length=len(str(num))

total=0

while num > 0:
    digit = temp%10
    total=total + num**length
    num=num//10


if temp==total:
    print("Amstrong number")

else:
    print("Not an amstrong number")
