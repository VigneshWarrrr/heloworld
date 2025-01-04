num=int(input("Enter the number"))
sum=0
term=0
for i in range(1,num+1):
    if i%2==0:
        term+=i*i
    else:
        term=0
    sum+=term
print("The sum of the squares of even numbers:",sum)