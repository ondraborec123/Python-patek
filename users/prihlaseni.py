inputName=input("enter your name: ")
inputPass=input("enter your password: ")
fullString=inputName+";"+inputPass+"\n"
with open("uzivatele.txt", "r") as f:
    file=f.readlines()
    users=[]
    for i in file: users.append(i)
    if fullString in users: print(f"\nHello, {inputName}!")
    if fullString not in users: print("\nAccess denied!")