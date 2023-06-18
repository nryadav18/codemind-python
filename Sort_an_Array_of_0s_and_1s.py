n=int(input())
lst=[]
s=map(int,input().split())
for i in s:
    lst.append(i)
lst.sort()
for i in lst:
    print(i,end=' ')