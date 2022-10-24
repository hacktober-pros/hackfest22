# cook your dish here
test = int(input())
while(test):
    test = test - 1
    arr = list(map(int, input().split())) #Taking input.
    N = arr[0]
    X = arr[1]
    slice = 44
    
    if (int((N*X)/slice)<(N*X)/slice):
        print(int(((N*X)/slice) + 1))
    else:
        print(int((N*X)/slice))
