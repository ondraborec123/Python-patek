import random
pocetHer=int(input("""╔═══════ KAMEN NUZKY PAPIR ══════╗
║    Kolik her si chces zahrat?  ║
╚═══════════════════════╣ """))
odehraneHry=0
lost,win,draw=0,0,0
while odehraneHry!=pocetHer:
    odehraneHry+=1
    pc=random.randint(1,3)
    ja=int(input("""
    [1] Kamen
    [2] Nuzky
    [3] Papir
    
    >> """))
    if ja==1: select="kamen"
    if ja==2: select="nuzky"
    if ja==3: select="papir"
    if ja==1 and pc==2:
        print("\n\nVybral jsi kamen, ja vybral nuzky, vyhral jsi!")
        win+=1
    if ja==1 and pc==3:
        print("\nVybral jsi kamen, ja vybral papir, prohral jsi!")
        lost+=1
    if ja==2 and pc==3:
        print("\nVybral jsi nuzky, ja vybral papir, vyhral jsi!")
        win+=1
    if ja==2 and pc==1:
        print("\nVybral jsi nuzky, ja vybral kamen, prohral jsi!")
        lost+=1
    if ja==3 and pc==1:
        print("\nVybral jsi papir, ja vybral kamen, vyhral jsi!")
        win+=1
    if ja==3 and pc==2:
        print("\nVybral jsi papir, ja vybral nuzky, prohral jsi!")
        lost+=1
    if ja==pc:
        print(f"\nVybrali jsme oba {select}, remiza!")
        draw+=1
if pocetHer<=9: print(f"""
╔═══════════════════════╗
║ VYSLEDKY              ║
║   Pocet her: {pocetHer}        ║
║   Vyhry: {win}            ║
║   Prohry: {lost}           ║
║   Remizy: {draw}           ║
╚═══════════════════════╝""")
if pocetHer>=10: print(f"""
╔═══════════════════════╗
║ VYSLEDKY              ║
║   Pocet her: {pocetHer}
║   Vyhry: {win}
║   Prohry: {lost}
║   Remizy: {draw}
╚═══════════════════════╝""")