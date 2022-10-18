def hailstone(n):
    if n==1:
        return n
    s = ""
    while n > 1:
        s = s+str(n)+" -> "
        if n%2 == 1:
            n = int(n*3+1)
        else:
            n = int(n/2)
    
    return s+"1"
 
if __name__ == "__main__":
    n = input("Enter a number: ")
    if n.isnumeric():
        n = int(n)
        print("Length of Hailstone Sequence: ", hailstone(n))
    else:
        print("Invalid input.")