num = int(input("enter a number to check if it is divisible by 2 and 3: "))
print(num)
if (num%2 == 0):
    if(num%3 == 0):
        print(f"number{num} is divisible both by 2 and 3")
    else:
        print(f"number{num} is only divisible by 2")
else:
    print(f"number{num} is not divisible both by 2 and 3")        
