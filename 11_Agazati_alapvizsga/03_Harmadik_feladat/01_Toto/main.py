from fogadasi_fordulo import Fogadasi_fordulo
# from typing import List # Python 3.8.X, vagy alatta kell


def main() -> None:
    # 1. feladat: Olvassa be és tárolja el a toto.txt UTF-8 kódolású szöveges
    # állományban található adatokat!
    # Az összetartozó adatokat saját osztály definiálásával kezelje!
    # A fogadási fordulók adatait saját osztály típusú listában tárolja!
    # Ügyeljen rá, hogy az állomány első sora a mezőneveket tartalmazza.

    print('Toto feladat')
    print('1. feladat: Adatok beolvasása és tárolása')
    # ff: List[Fogadasi_fordulo] = []  #  Python 3.8.X, vagy alatta
    ff: list[Fogadasi_fordulo] = []
    with open('toto.txt', 'r', encoding='UTF-8') as file:
        for sor in file.read().splitlines()[1:]:
            ff.append(Fogadasi_fordulo(sor))

    # 2. feladat: Határozza meg és írja ki a fogadási fordulók számát

    # Minta: 2. feladat: Fogadási fordulók száma: 1630

    print(f'2. feladat: Fogadási fordulók száma: {len(ff)}')

    # 3. feladat: Számolja meg és írja ki a képernyőre a telitalálatos szelvények számát!

    # Minta: 3. feladat: Telitalálatos szelvények száma: 13718 darab

    szelveny13p1_darab: int = 0
    for e in ff:
        szelveny13p1_darab += e.t13p1
    print(f'3. feladat: Telitalálatos szelvények száma: {szelveny13p1_darab} darab')

    # 4. feladat: Döntse el, hogy volt-e olyan forduló, ahol nem volt döntetlen mérkőzés

    # Minta: 4. feladat: Volt döntetlen mentes forduló!

    volt_ilyen_fordulo: bool = False
    for e in ff:
        if e.nem_volt_dontetlen():
            volt_ilyen_fordulo = True
            break
        # vagy:
        # if e.eredmenyek.count('X') == 0:
        #     volt_ilyen_fordulo = True
        #     break

    print(f'4. feladat: {"Volt" if volt_ilyen_fordulo else "Nem volt"} döntetlen mentes forduló!')

    # 5. feladat: Számítsa ki, mekkora volt a "telitalálatos" (T13p1>0 vagy Ny13p1>0)
    # fordulók során a telitalálatos szelvényekre kifizetett nyereményösszegek átlaga!
    # Egy fordulóban a nyereményösszeget a T13p1 * Ny13p1 kifejezéssel számolja!
    # Az átlagot egész számra kerekítve jelenítse meg!

    # Minta: 5. feladat: Átlag: 4227932 Ft

    összeg_nyeremény: int = 0
    for e in ff:
        if e.t13p1 > 0 or e.ny13p1 > 0:
            összeg_nyeremény += e.t13p1 * e.ny13p1
    # Az átlagot az ÖSSZES forduló számára vetítve kell megadni (nem csak a telitalálatosakéra)!
    átlag: int = round(összeg_nyeremény / len(ff))
    print(f'5. feladat: Átlag: {átlag} Ft')

    # 6. feladat: Írja ki annak a két fordulónak az adatait, ahol a legnagyobb, illetve
    # a legkisebb volt az egy telitalálatos szelvény után fizetett nyeremény (Ny13p1)!
    # Feltételezhető, hogy nem alakult ki holtverseny és minden telitalálatos fordulóban
    # fizettek nyereményt.

    # Minta:
    # 6. feladat:
    #         Legnagyobb:
    #         Év: 2013
    #         Hét: 8.
    #         Forduló: 1.
    #         Telitalálat: 1 db
    #         Nyeremény: 57145865 Ft
    #         Eredmények: 1X2222X11X1X11

    telitalálatos_fordulók: list[Fogadasi_fordulo] = [e for e in ff if e.t13p1 > 0]
    legnagyobb: Fogadasi_fordulo = telitalálatos_fordulók[0]
    legkisebb: Fogadasi_fordulo = telitalálatos_fordulók[0]
    for e in telitalálatos_fordulók[1:]:
        if e.ny13p1 > legnagyobb.ny13p1:
            legnagyobb = e
        if e.ny13p1 < legkisebb.ny13p1:
            legkisebb = e

    def ki_forduló(cím: str, e: Fogadasi_fordulo) -> None:
        print(f'\t{cím}:')
        print(f'\tÉv: {e.ev}')
        print(f'\tHét: {e.het}.')
        print(f'\tForduló: {e.fordulo}.')
        print(f'\tTelitalálat: {e.t13p1} db')
        print(f'\tNyeremény: {e.ny13p1} Ft')
        print(f'\tEredmények: {e.eredmenyek}')

    print('6. feladat:')
    ki_forduló('Legnagyobb', legnagyobb)
    print()
    ki_forduló('Legkisebb', legkisebb)


if __name__ == "__main__":
    main()
