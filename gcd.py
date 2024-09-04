a=int(input("enter a value"))
b=int(input("enter b value"))

for i in range(min(a,b),0,-1):
    if a%i==0 and b%i==0:
      print(i)
