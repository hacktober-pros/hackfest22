import math
def getFactors(n):
    factors = []
    for i in range(1, min(n+1,99999)):
       if n % i == 0:
            factors.append(i)
    return factors

def costNumber(num,a,b,c,d,e,f,g):
    sum=a+b+c+d+e+f+g
    #print(sum)
    sum_digits={'0':sum-g,'1':b+c,'2':sum-(f+c),'3':sum-(f+e),'4':sum-(a+e+d),'5':sum-(b+e),'6':sum-b,'7':a+b+c,'8':sum,'9':sum-e}
    summing=[]
    num=str(num)
    if len(num)>1:
        num=list(num)
    #print(num)
    for i in num:
        summing.append(sum_digits.get(i))
    
    #print(summing)
    final_sum=0  
    for i in range(len(summing)):
        final_sum=final_sum+summing[i]
   
    return final_sum
  

#  Read the number of tests
T = int(input())
for _ in range(T):
    # Read the data for this test
    n, a, b, c, d, e, f, g = map(int, input().split())
    # Generate the list of factors
    factors=getFactors(n)
    # Go through the factors finding the minimum cost
    min_cost = math.inf
    for i in factors:
        cost = costNumber(i, a, b, c, d, e, f, g)
        #print(cost)
        #print(cost)
        if cost < min_cost:
            min_cost = cost
    # And print the minimum factor
    print(min_cost)

    
