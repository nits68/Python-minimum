def main() -> None:
    # A Python programozási nyelv fontosabb operátorai
    # ==================================================
    # w3s: https://www.w3schools.com/python/python_operators.asp

    # 1. Aritmetikai operátorok
    # =========================
    a: int = 17
    b: int = 5
    print('Aritmetikai operátorok')
    print(f'{a} + {b} = {a + b}')  # összeadás
    print(f'{a} - {b} = {a - b}')  # kivonás
    print(f'{a} * {b} = {a * b}')  # szorzás
    print(f'{a} / {b} = {a / b}')  # osztás, az eredmény mindig float
    print(f'{a} // {b} = {a // b}')  # egészosztás (maradék nélkül, lefelé kerekít)
    print(f'{a} % {b} = {a % b}')  # osztás maradéka (modulo)
    print(f'{a} ** {b} = {a ** b}')  # hatványozás (a-nak a b-edik hatványa)

    # Negatív számoknál az egészosztás és a modulo mindig lefelé kerekít:
    print(f'{-a} // {b} = {-a // b}')  # -4 (nem -3!)
    print(f'{-a} % {b} = {-a % b}')  # 3 (nem -2!)

    # 2. Rövidített (összetett) értékadó operátorok
    # ==============================================
    # A "vál = vál op érték" alak helyett "vál op= érték" is írható:
    print('\nRövidített értékadás')
    c: int = 10
    c += 3  # c = c + 3
    print(f'c += 3  -> {c}')
    c -= 4  # c = c - 4
    print(f'c -= 4  -> {c}')
    c *= 2  # c = c * 2
    print(f'c *= 2  -> {c}')
    # c /= 3  # c = c / 3, az eredmény float lesz
    print(f'c /= 3  -> {c}')
    c **= 2  # c = c ** 2
    print(f'c **= 2 -> {c}')
    d: int = 17
    d %= 5  # d = d % 5
    print(f'd %= 5  -> {d}')

    # 3. Relációs (összehasonlító) operátorok
    # ========================================
    # Az eredményük mindig logikai (bool) érték
    print('\nRelációs operátorok')
    print(f'{a} == {b} -> {a == b}')  # type: ignore # egyenlő-e
    print(f'{a} != {b} -> {a != b}')  # type: ignore # nem egyenlő-e
    print(f'{a} > {b}  -> {a > b}')  # nagyobb
    print(f'{a} < {b}  -> {a < b}')  # kisebb
    print(f'{a} >= {b} -> {a >= b}')  # nagyobb vagy egyenlő
    print(f'{a} <= {b} -> {a <= b}')  # kisebb vagy egyenlő

    # 4. Logikai operátorok
    # ======================
    # and, or, not (a C-szerű nyelvek &&, ||, ! operátorainak felelnek meg)
    print('\nLogikai operátorok')
    x: bool = True
    y: bool = False
    print(f'x and y -> {x and y}')  # csak akkor True, ha mindkettő True
    print(f'x or y  -> {x or y}')  # akkor True, ha legalább az egyik True
    print(f'not x   -> {not x}')  # a logikai érték ellentettje

    # Gyakori felhasználás: összetett feltétel egy elágazásban
    év: int = 2024
    if év % 4 == 0 and (év % 100 != 0 or év % 400 == 0): # type: ignore
        print(f'{év} szökőév!')
    else:
        print(f'{év} nem szökőév!')

    # 5. Bitműveleti (bitwise) operátorok
    # ====================================
    # A számok bináris (kettes számrendszerbeli) alakján, bitenként végzett műveletek
    e: int = 0b1010  # 10 (kettes számrendszerben megadva)
    f: int = 0b0110  # 6
    print('\nBitműveleti operátorok')
    print(f'{e:04b} & {f:04b} = {e & f:04b}  ({e & f})')  # bitenkénti ÉS
    print(f'{e:04b} | {f:04b} = {e | f:04b}  ({e | f})')  # bitenkénti VAGY
    print(f'{e:04b} ^ {f:04b} = {e ^ f:04b}  ({e ^ f})')  # bitenkénti kizáró VAGY (XOR)
    print(f'~{e:04b}       = {~e}')  # bitenkénti negálás (a szám -(n+1) lesz)
    print(f'{e:04b} << 1   = {e << 1:05b}  ({e << 1})')  # balra léptetés: *2
    print(f'{e:04b} >> 1   = {e >> 1:03b}  ({e >> 1})')  # jobbra léptetés: //2

    # Gyakorlati példa: egy szám párosságának eldöntése bitművelettel
    # (a % 2 == 0 ellenőrzés helyett a legkisebb helyiértékű bitet vizsgáljuk)
    szám: int = 42
    if szám & 1 == 0:
        print(f'{szám} páros szám! (bitművelettel eldöntve)')
    else:
        print(f'{szám} páratlan szám! (bitművelettel eldöntve)')

    # 6. Tartalmazás- és azonosságvizsgáló operátorok (kitekintés)
    # ==============================================================
    # in / not in -> egy elem szerepel-e egy kollekcióban (lásd bővebben: 05_Kollekciok, 06_Karakterlancok)
    gyümölcsök: list[str] = ['alma', 'körte', 'szilva']
    print('\nTartalmazásvizsgálat')
    print(f"'alma' in gyümölcsök -> {'alma' in gyümölcsök}")
    print(f"'barack' not in gyümölcsök -> {'barack' not in gyümölcsök}")

    # 7. Műveleti sorrend (precedencia)
    # ===================================
    # Zárójel > hatványozás > szorzás/osztás/maradékképzés > összeadás/kivonás > relációs > logikai
    print('\nMűveleti sorrend')
    print(f'2 + 3 * 4 = {2 + 3 * 4}')  # 14, nem 20 (a szorzás előbb történik)
    print(f'(2 + 3) * 4 = {(2 + 3) * 4}')  # 20, a zárójel felülírja a sorrendet


if __name__ == "__main__":
    main()
