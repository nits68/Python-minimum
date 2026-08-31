from Eredmény import Eredmény
# from typing import List # Python 3.8.X, vagy alatta kell


def main() -> None:
    # 2. Olvassa be az ub2017egyeni.txt állományban lévő adatokat és tárolja el
    # egy saját osztály típusú listában!
    # Ügyeljen arra, hogy az állomány első sora a mezőneveket tartalmazza.

    # ub2017: List[Eredmény] = []  # Python 3.8.X, vagy alatta
    ub2017: list[Eredmény] = []
    with open('ub2017egyeni.txt', 'r', encoding='utf-8') as file:
        for sor in file.read().splitlines()[1:]:
            ub2017.append(Eredmény(sor))

    # 3. Határozza meg és írja ki a minta szerint a képernyőre
    # a versenyen elindult futók számát!
    # Minta: 3. feladat: Egyéni indulók: 186 fő

    print(f'3. feladat: Egyéni indulók: {len(ub2017)} fő')

    # 4. Számolja meg és írja ki a képernyőre a minta szerint,
    # hogy hány női sportoló teljesítette a teljes távot!
    # Minta: 4. feladat: Célba érkező női sportolók: 11 fő
    nők100: int = 0
    for e in ub2017:
        if e.kategória == 'Noi' and e.táv_százalék == 100:
            nők100 += 1
    print(f'4. feladat: Célba érkező női sportolók: {nők100} fő')

    # Kiegészítő feladat (nem az official feladatsor része):
    # Határozzuk meg a leghosszabb nevű futót/futókat és írjuk ki az adatait a minta szerint!
    # Holtverseny esetén csak a futók neveit írjuk egymás mellé a minta szerint!
    print('Kiegészítő feladat: A leghosszabb nevű futó(k)')
    # Meghatározzuk a leghosszabb név hosszát:
    név_hossz_max: int = 0
    for e in ub2017:
        # if e.név_hossz() > név_hossz_max:
        #     név_hossz_max = e.név_hossz()
        # vagy:
        if len(e.név) > név_hossz_max:
            név_hossz_max = len(e.név)

    # Kiválogatjuk egy új listába a leghosszabb nevű futókat:
    # ub2017_max: List[Eredmény] = [] # Python 3.8.X, vagy alatta
    ub2017_max: list[Eredmény] = []
    for e in ub2017:
        if e.név_hossz() == név_hossz_max:
            ub2017_max.append(e)

    # Az új lista (ub2017_max) hossza szerint elvégezzük az eredmény kiírását
    if len(ub2017_max) == 1:
        print(f'\tNév: {ub2017_max[0].név}')
        print(f'\tRajtszám: {ub2017_max[0].rajtszám}')
        print(f'\tEredmény: {ub2017_max[0].idő}')
    else:
        print('\tNevek: ', end='')
        for e in ub2017_max:
            print(f'{e.név}', end='; ')
        print()  # soremelés az utolsó futó neve után

    # 5. Kérje be a felhasználótól egy sportoló nevét, majd határozza meg és írja ki
    # a minta szerint, hogy a sportoló indult-e a versenyen! A keresést ne folytassa,
    # ha az eredményt meg tudja határozni! Ha a sportoló indult a versenyen, akkor azt is
    # írja ki a képernyőre, hogy a teljes távot teljesítette-e!
    # Feltételezheti, hogy nem indultak azonos nevű sportolók ezen a versenyen.

    # Minta: 5. feladat: Kérem a sportoló nevét: Utasi Akos
    #         Indult egyéniben a sportoló? Igen
    #         Teljesítette a teljes távot? Nem

    kért_név: str = input('5. feladat: Kérem a sportoló nevét: ')
    talált_sportoló: Eredmény | None = None
    for e in ub2017:
        if e.név == kért_név:
            talált_sportoló = e
            break
    print(f'\tIndult egyéniben a sportoló? {"Igen" if talált_sportoló is not None else "Nem"}')
    if talált_sportoló is not None:
        teljesítette: bool = talált_sportoló.táv_százalék == 100
        print(f'\tTeljesítette a teljes távot? {"Igen" if teljesítette else "Nem"}')

    # 6. Készítsen idő_óra azonosítóval valós típusú értékkel visszatérő függvényt vagy
    # jellemzőt, ami a versenyző időeredményét órában határozza meg! Egy óra 60 percből,
    # illetve 3600 másodpercből áll.
    # Lásd: Eredmény.idő_óra()

    # 7. Határozza meg és írja ki a minta szerint a teljes távot teljesítő
    # férfi sportolók átlagos idejét órában!
    # Feltételezheti, hogy legalább egy ilyen sportoló volt.
    # Minta: 7. feladat: Átlagos idő: 28,347301051051 óra
    férfi100_összeg_idő: float = 0
    férfi100_fő: int = 0
    for e in ub2017:
        if e.kategória == 'Ferfi' and e.táv_százalék == 100:
            férfi100_fő += 1
            férfi100_összeg_idő += e.idő_óra()
    print(f'7. feladat: Átlagos idő: {férfi100_összeg_idő / férfi100_fő} óra')

    # 8. Keresse meg a női és a férfi kategóriák győzteseit és írja ki nevüket, rajtszámukat
    # és időeredményeiket a minta szerint! Feltételezheti, hogy egyik kategóriában sem
    # alakult ki holtverseny és mindkét kategóriában volt célba érkező futó.

    # Minta: 8. feladat: Verseny győztesei
    #         Nők: Maraz Zsuzsanna (114.) - 22:31:31
    #         Férfiak: Dan Lawson (31.) - 18:30:20

    nő_győztes: Eredmény | None = None
    férfi_győztes: Eredmény | None = None
    for e in ub2017:
        if e.táv_százalék != 100:
            continue
        if e.kategória == 'Noi':
            if nő_győztes is None or e.idő_óra() < nő_győztes.idő_óra():
                nő_győztes = e
        elif e.kategória == 'Ferfi':
            if férfi_győztes is None or e.idő_óra() < férfi_győztes.idő_óra():
                férfi_győztes = e

    print('8. feladat: Verseny győztesei')
    print(f'\tNők: {nő_győztes.név} ({nő_győztes.rajtszám}.) - {nő_győztes.idő}')
    print(f'\tFérfiak: {férfi_győztes.név} ({férfi_győztes.rajtszám}.) - {férfi_győztes.idő}')


if __name__ == "__main__":
    main()
