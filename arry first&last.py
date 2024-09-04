num=int(input("enter the number"))
count=0
while num!=0:
    if count==0:
        last=num%10
        count+=1
    first=num%10
    num=num//10
print(first+last)
