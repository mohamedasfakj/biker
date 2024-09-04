#write a prgb to calculate the power without using POW function nd **.(using for loop)

def calculate_power(base,power):
    result=1
    for i in range(power):
        result*=base
    return result                          
base=int(input("enter the base number"))
power=int(input("enter the power"))

result=calculate_power(base,power)
print("result",result)