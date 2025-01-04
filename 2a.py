import math
a=int(input("Enter the coefficient of a:"))
b=int(input("Enter the coefficient of b:"))
c=int(input("Enter the coefficient of c:"))
dis=b*b-(4*a*c)
if a==0:
    print("The value of a cannot be zero")
else:
    if dis>0:
        r1=(-b+math.sqrt(dis))/(2*a)
        r2=(-b-math.sqrt(dis))/(2*a)
        print("The system has real and distinct roots")
        print("Root 1:",r1)
        print("Root 2",r2)
    elif dis==0:
        root=-b/(2*a)
        print("The system has real and equal roots")
        print("Root:",root)
    else:
        real_part=-b/(2*a)
        ima_part=(math.sqrt(abs(dis)))/(2*a)
        print("he imaginary roots")
        print("Root 1:",real_part,"+",ima_part,"i")
        print("Root 1:",real_part,"-",ima_part,"i")