import math
for x in range(int(input())):
    n,k=[int(d) for d in input().split()]
    if n>k and n%k==0:
        print(n//k)
    else:
        l=math.lcm(n,k)
        print(l//k)