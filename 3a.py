def add(x,y):
    return (lambda a,b:a+b)(x,y)
n1=int(input("Enter the 1st number:"))
n2=int(input("Enter the 2nd number:"))
sum=add(n1,n2)
print("The sum of the 2 numbers is=",sum)