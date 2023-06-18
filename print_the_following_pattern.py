n=int(input())
c=0
for i in range(n,0,-1):
    for j in range(i):
        print(chr(65+n-c-1),end=' ')
    print()
    c+=1