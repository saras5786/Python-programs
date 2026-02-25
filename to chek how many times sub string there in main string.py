# To count the not of times substring repeated in main string.

def jks(sti,substi):
    count=0
    for i in range(len(sti)-len(substi) + 1):
        if sti[i:i+len(substi)] == substi:
            count+=1


    return count


sti = input("Enter main string:").strip()
substi = input("Enter sub string:").strip()
count = jks(sti, substi)
print(count)

