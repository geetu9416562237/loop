n=int(input("enter a number: "))
num=n
sum=0
while num>0:
    j=1
    fac=1
    rem=num%10
    while j<=rem:
        fac=fac*j
        j=j+1
    sum=sum+fac
    num=num//10
if n==sum:
    print("strong number")
else:
    print("Not strong")



