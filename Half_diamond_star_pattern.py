n=int(input())
if n<=100 and n>=3:
    for i in range(1,n):
        for j in range(1,i+1):
            print("*",end='')
        print("")
    for i in range(1,n+1):
        for n in range(i,n+1):
            print("*",end='')
        print("")
else:
    print("The pattern is not possible")