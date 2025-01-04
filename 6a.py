filename=input("Enter the file name")
fd=open(filename,"r")
counts=dict()
for line in fd:
    words=line.split()
    for w in words:
        if w in counts:
            counts[w]+=1
        else:
            counts[w]=1
print(counts)