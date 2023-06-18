n=int(input())
lst=[]
s=map(int,input().split())
for i in s:
    lst.append(i)
se=set(lst)
for i in se:
    print(i,end=' ')