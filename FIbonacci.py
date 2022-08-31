n=int(input("Enter no of elements in the sequence:"))
n1 = 0
n2 = 1
count = 0
if n<=0:
    print("Not valid")
if n==1:
    print(n1)
if n==2:
    print(n1)
if n>2:
    print("FIbonacci sequence:")
    print(n1)
    print(n2)
    for i in range(2,n):
            e = n1 + n2
            n1 = n2
            n2 = e
            print(e)
