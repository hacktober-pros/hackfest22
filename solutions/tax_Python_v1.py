tt = int(input())
for i in range(tt):
    income = int(input())
    if income > 100100:
        income -= 1010
    print(income)

test = int(input())
while(test):
    test = test - 1
    arr = list(map(int, input().split())) #Taking input.
    Z = arr[0]
    
    if (Z> 100):
        print(f'{Z-10}')
    else:
        print(Z)
    
