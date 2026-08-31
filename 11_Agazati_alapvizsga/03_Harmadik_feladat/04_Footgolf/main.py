from Versenyző import Versenyző


def main() -> None:
    # 2. Olvassa be a fob2016.txt állományban lévő adatokat és tárolja el egy
    # saját osztály típusú listában!
    fg2016: list[Versenyző] = []
    with open('fob2016.txt', 'r', encoding='utf-8') as file:
        for sor in file.read().splitlines():
            fg2016.append(Versenyző(sor))

    # 3. Határozza meg és írja ki a képernyőre a minta szerint, hogy
    # hány versenyző indult összesen a két kategóriában a bajnokságon!
    # Minta: 3. feladat: Versenyzők száma: 77
    print(f'3. feladat: Versenyzők száma: {len(fg2016)}')

    # 4. Határozza meg és írja ki a képernyőre a minta szerint
    #  a női versenyzők arányát az összes versenyzőszámhoz képest!
    # A százalékos értéket két tizedesjegy pontossággal jelenítse meg!
    # Feltételezheti, hogy legalább egy női versenző indult a bajnokságban.
    # Minta: 4. feladat: A női versenyzők aránya: 11,69%
    női_versenyzők_száma: int = 0
    for v in fg2016:
        if v.kategória == 'Noi':
            női_versenyzők_száma += 1
    arány_nők: float = női_versenyzők_száma / len(fg2016) * 100
    print(f'4. feladat: A női versenyzők aránya: {arány_nők:.2f} %')

    # 5. feladat tesztjéhez: print(fg2016[1].összpont())
    # (Az összpont() metódus a Versenyző osztályban van definiálva.)

    # 6. Határozza meg és írja ki a minta szerint a 2016-os footgolf bajnokság legtöbb pontot
    # szerzett női bajnokát! Feltételezheti, hogy legalább egy női induló volt a bajnokságon, és
    # nem alakult ki holtverseny.
    # Minta: 6. feladat: A bajnok női versenyző
    #         Név: Major Ilona
    #         Egyesület: FTC FOOTGOLF
    #         Összpont: 680

    # Megoldás a None objektummal:
    női_bajnok = None
    for v in fg2016:
        if v.kategória == 'Noi':
            if női_bajnok is None:
                női_bajnok = v
            else:
                if v.összpont() > női_bajnok.összpont():
                    női_bajnok = v

    print('6. feladat: A bajnok női versenyző')
    print(f'\tNév: {női_bajnok.név}')
    print(f'\tEgyesület: {női_bajnok.egyesület}')
    print(f'\tÖsszpont: {női_bajnok.összpont()}')

    # Ugyanez az eredmény más módszerekkel is előállítható:

    # Megoldás segédindexszel:
    # női_maxi = -1
    # for i, v in enumerate(fg2016):
    #     if v.kategória == 'Noi':
    #         if női_maxi == -1 or v.összpont() > fg2016[női_maxi].összpont():
    #             női_maxi = i
    # női_bajnok = fg2016[női_maxi]

    # Megoldás segédlistával:
    # női_versenyzők: list[Versenyző] = [v for v in fg2016 if v.kategória == 'Noi']
    # női_bajnok = női_versenyzők[0]
    # for v in női_versenyzők[1:]:
    #     if v.összpont() > női_bajnok.összpont():
    #         női_bajnok = v

    # 7. Készítsen szöveges állományt osszpontFF.txt néven, amelybe kiírja a felnőtt férfi
    # kategóriában indult versenyzők nevét és a bajnokságban elért összpontszámát!
    # A sorokban az adatokat pontosvesszővel válassza el egymástól a minta szerint!

    # Minta: osszpontFF.txt (részlet)
    # Albert Laszlo;30
    # Bacskai Bence;541
    # Bado Szilard;288

    print('7. feladat: osszpontFF.txt állomány létrehozása')
    with open('osszpontFF.txt', 'w', encoding='utf-8') as file:
        for v in fg2016:
            if v.kategória == 'Felnott ferfi':
                file.write(f'{v.név};{v.összpont()}\n')

    # 8. Készítsen statisztikát a minta szerint, hogy az egyes egyesületekből hány versenyző
    # indult a bajnokságon! Az egyesületen kívül indult versenyzőknél az egyesületnél
    # az "n.a." adat szerepel. Ezek a versenyzők és az egy vagy két versenyzőt indító
    # egyesületek ne szerepeljenek a statisztikában!

    # Minta: 8. feladat: Egyesület statisztika
    #         HOLE HUNTERS - 7 fő
    #         EMFGSE - 10 fő
    #         ...

    egyesületi_statisztika: dict[str, int] = {}
    for v in fg2016:
        if v.egyesület == 'n.a.':
            continue
        if v.egyesület in egyesületi_statisztika:
            egyesületi_statisztika[v.egyesület] += 1
        else:
            egyesületi_statisztika[v.egyesület] = 1

    print('8. feladat: Egyesület statisztika')
    for egyesület, létszám in egyesületi_statisztika.items():
        if létszám > 2:
            print(f'\t{egyesület} - {létszám} fő')


if __name__ == "__main__":
    main()
