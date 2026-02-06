with open("trideni_text.txt","r") as f1:
    radky=f1.readlines()
    radky.sort()
    with open("trideni_hotovo.txt","w") as f2:
        for i in radky:
            f2.write(i)