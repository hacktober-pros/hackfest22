'''
x=12
y=16
'''
def mcd(a,b):
    if a<b:
        aux=a
        a=b
        b=aux
    while b!=0:
        res=b
        b=a%b
        a=res
    print("answer is:",res)
if __name__ == "__main__":
    mcd(x,y)

