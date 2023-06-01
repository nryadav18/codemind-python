n=int(input())
a=n;s=0
while n!=0:
    s=s*10+n%10;n=n//10
if s==a:
    print("True")
else:
    print("False")