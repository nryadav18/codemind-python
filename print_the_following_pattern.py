n=int(input())
c=0
for i in range(1,n+1):
    for j in range(1,n+1):
        print(chr(65+c),end=' ')
    print()
    c+=1