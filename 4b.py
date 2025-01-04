name=input("Enter your name")
if name.isalpha()==False:
    print("Invalid input")
else:
    pan=input("Enter you Pan")
    if len(pan)==10 and pan[0:5].isalpha()==True and pan[5:9].isdigit()==True and pan[9].isalpha()==True:
        print("Name:",name)
        print("PAN:",pan)
    else:
        print("Invalid input")