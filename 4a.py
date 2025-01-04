msg=input("Enter the message:")
for i in range(len(msg)):
    letter=msg[i]
    print((chr(ord(letter)+3)),end='')
