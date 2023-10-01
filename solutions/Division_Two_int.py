def divide(dividend, divisor):
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31

    if divisor == 0:
        return INT_MAX if dividend > 0 else INT_MIN
    if dividend == 0:
        return 0

    negative = (dividend < 0) ^ (divisor < 0)
    dividend = abs(dividend)
    divisor = abs(divisor)

    quotient = 0
    while dividend >= divisor:
        temp_divisor, multiple = divisor, 1
        while dividend >= (temp_divisor << 1):
            temp_divisor <<= 1
            multiple <<= 1
        dividend -= temp_divisor
        quotient += multiple

    quotient = -quotient if negative else quotient

    if quotient < INT_MIN:
        return INT_MIN
    elif quotient > INT_MAX:
        return INT_MAX
    else:
        return quotient

def main():
    try:
        dividend = int(input("Enter the dividend: "))
        divisor = int(input("Enter the divisor: "))
        result = divide(dividend, divisor)
        print("Result of division:", result)
    except ValueError:
        print("Invalid input. Please enter valid integers.")

if __name__ == "__main__":
    main()
