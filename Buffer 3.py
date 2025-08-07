#find hcf
while True:
    q=int(input("enter number: "))
    p=int(input("enter number: "))
    r=int(input("enter number: "))
    x=(p,q,r)
    low=min(x)
    high=max(x)
    a=()
    for i in range (1,low+1):
        if q%i==0 and p%i==0 and r%i==0:
            a=(i)
    print ("hcf= ", a)