num = int(input("Enter a Number: "))

if(num%2 == 0):
    if(num%3==0):
        print("Number is divisible by 2 and 3 both.")
    else:
        print("Number is divisible by 2 only.")
else:
    print("Number is not Divisible any")