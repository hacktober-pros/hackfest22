test = int(input())
while(test):
    test = test - 1
    arr = list(map(int, input().split())) #Taking input.
    Z = arr[0]
    Y = arr[1]
    A = arr[2]
    B = arr[3]
    C = arr[4]
    
    Total = Z - Y - A - B - C
    
    if (Total >= 0):
        print('YES')
    else:
        print("NO")
    
