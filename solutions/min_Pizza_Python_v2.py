import math
tt = int(input())
for i in range(tt):
    l = list(map(int, input().split()))
    number_of_pizza=math.ceil(l[0]*l[1]/44)
    print(number_of_pizza)
