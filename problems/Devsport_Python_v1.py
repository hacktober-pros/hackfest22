TestCases = int(input())
for i in range(TestCases):
    input_digit_list = list(map(int, input().split(" ")))

    initial_amt = input_digit_list[0] * 10 + input_digit_list[0]
    spent_amt = input_digit_list[1] * 10 + input_digit_list[1]
    amt_left = initial_amt - spent_amt

    ride1_cost = input_digit_list[2] * 10 + input_digit_list[2]
    ride2_cost = input_digit_list[3] * 10 + input_digit_list[3]
    ride3_cost = input_digit_list[4] * 10 + input_digit_list[4]
    tot_ride_cost = ride1_cost + ride2_cost + ride3_cost
    
    if amt_left - tot_ride_cost >= 0:
        print("YES")
    else:
        print("NO")