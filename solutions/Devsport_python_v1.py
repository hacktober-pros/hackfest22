#https://www.codechef.com/START21C/problems/DEVSPORTS
T = int(input())
l = []
for i in range(T):
    Z,Y,A,B,C = map(int,input().split())
    if (Z-Y)>=(A+B+C):
        l.append("YES")
    else:
        l.append("NO")
for i in l:print(i)
