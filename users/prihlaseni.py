inputName=input("enter your name: ")
inputPass=input("enter your password: ")
fullString=inputName+";"+inputPass+"\n"
with open("uzivatele.txt", "r") as f:
    file=f.readlines()
    if fullString in file: print(f"\nHello, {inputName}!")
    if fullString not in file: print("\nAccess denied!")