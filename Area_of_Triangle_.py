from math import sqrt
a,b,c=map(int,input().split());s=(a+b+c)/2
res=sqrt(s*(s-a)*(s-b)*(s-c));print("%.2f"%res)