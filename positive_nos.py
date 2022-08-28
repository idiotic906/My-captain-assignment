

li=[]
n=int(input("Enter size of list "))
for i in range(0,n):
    e=int(input("Element of list:"))
    li.append(e)

print("\n Positive numbers are:")
for i in range(n):
    if(li[i]>= 0):
        print(li[i], end = ' ')


