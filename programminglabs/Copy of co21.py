n=10
factorial=1
if n<0:
    print("Sorry, factorial does not exists for negetive numbers")
elif n==0:
    print("The factorial of 0 is 1")
else:
    for i in range(1,n+1):
        factorial=factorial*i
    print("The factorial of ",n," is ",factorial)
