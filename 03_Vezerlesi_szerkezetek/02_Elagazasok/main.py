import random


def main() -> None:
    # Szelekciók (elágazások): Olyan vezérlési szerkezetek, ahol feltétel(ek)hez kötjük az utasítások végrehajtását

    # Elágazások fajtái:
    # - egy ágú (if)
    # - kétágú (if-else)
    # - többágú (if-elif-elif- ... -elif-else)
    # - többágú mintaillesztéssel (match-case, a Python 3.10 verziótól, a switch-case szerkezet megfelelője)

    # Példa egyágú (if) szelekcióra:
    print("Szám abszolút értéke")
    inputX: int = int(input("x= "))
    absX: int = inputX
    if inputX < 0:
        # absX = -inputX  # Előjelváltás
        absX = inputX * -1
    print(f"Abs({inputX}) = {absX}")

    # Példa kétágú (if-else) elágazásra
    print("\nPáros-páratlan meghatározása")
    inputSzám: int = int(input("szam= "))
    if inputSzám % 2 == 0:
        print("A szám páros!")
    else:
        print("A szám páratlan!")

    # Példa többágú (if-elif-else) elágazásra (else "ág" elhagyható):
    print("\nOsztályzat szöveges megfelelője")
    érdemjegy: int = int(input("Kérem az osztályzatot [1-5]: "))
    if érdemjegy == 1:
        print("Elégtelen")
    elif érdemjegy == 2:
        print("Elégséges")
    elif érdemjegy == 3:
        print("Közepes")
    elif érdemjegy == 4:
        print("Jó")
    elif érdemjegy == 5:
        print("Jeles")
    else:  # Az else ág opcionális, azaz elhagyható
        print("Ez nem osztályzat!")

    # Példa mintaillesztésre (match-case), ami a más nyelvekből ismert switch-case megfelelője.
    # FIGYELEM: csak a Python 3.10 (2021) verziótól használható!
    # A match után álló kifejezés értékét hasonlítjuk össze a case ágak mintáival,
    # az ELSŐ illeszkedő ág utasításai hajtódnak végre (break utasításra nincs szükség).
    print("\nOsztályzat szöveges megfelelője (match-case szerkezettel)")
    érdemjegy2: int = int(input("Kérem az osztályzatot [1-5]: "))
    match érdemjegy2:
        case 1:
            print("Elégtelen")
        case 2:
            print("Elégséges")
        case 3:
            print("Közepes")
        case 4:
            print("Jó")
        case 5:
            print("Jeles")
        case _:  # az aláhúzás (_) a "minden más eset" mintája, az if-elif-else else ágának felel meg
            print("Ez nem osztályzat!")

    # Egy ágban több minta is felsorolható a | (vagy) jellel:
    print("\nOsztályzat minősítése (több minta egy ágban)")
    match érdemjegy2:
        case 1 | 2:
            print("Gyenge eredmény")
        case 3 | 4:
            print("Közepes eredmény")
        case 5:
            print("Kiváló eredmény")
        case _:
            print("Ez nem osztályzat!")

    # Rövidített (shorthand) kétágú elágazás, amit feltételes operátor funkcióját is betöltheti:
    # Véletlen egész számok generálása a random osztály (modul) randint() függvényével:
    # Használat elött a random modult importálni kell: import random
    a: int = random.randint(10, 20)
    b: int = random.randint(10, 20)
    ki: str
    ki = 'A' if a > b else 'B'
    print(ki)
    c: int = 12 if a != b else 24
    # A fenti értékadás C# feltételes operátorral:
    # c = a != b ? 12 : 24
    print(c)  # 12

    # A pass utasítást akkor használjuk, ha később szeretnék egy igaz-hamis ág (blokk) utastásait megadni,
    # de kerülni szeretnénk a szintaktikai hibákat
    if b > a:
        pass
    else:
        pass


if __name__ == "__main__":
    main()
