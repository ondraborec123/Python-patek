import random
with open("cisla.txt","w") as f:
    for i in range(10): f.write(str(random.randint(1,1000))+"\n")

abc=int(input("Zadejte delici hodnotu: "))
with open("mala.txt","w") as f1:
    with open("cisla.txt","r") as f2:
        with open("vyhovujici.txt", "w") as f3:
            radky_mala=f2.readlines()
            for i in radky_mala:
                if abc>int(i): f1.write(i)
                if abc<=int(i): f3.write(i)