file1=open("file1.txt","r")
file2=open("file2.txt","w")
num=1
for line in file1:
    file2.write(str(num)+":"+line)
    num+=1
file1.close()
file2.close()
print("The contents of file1 are copied to file2")