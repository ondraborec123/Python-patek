with open("uzivatele.txt", "a") as f:
    name=input("Enter your name: ")
    password=input("Enter your password: ")
    print(f"Successfully created new user: {name}")
    f.write(f"{name};{password}\n")