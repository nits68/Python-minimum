from Épület import Épület


def main() -> None:
    # 2. Olvassa be az UTF-8 kódolású legmagasabb.txt állományban lévő adatokat
    # és tárolja el egy saját osztály típusú listában!
    # Ügyeljen rá, hogy az állomány első sora az adatok fejlécét tartalmazza!
    épületek: list[Épület] = []
    with open('legmagasabb.txt', 'r', encoding='utf-8') as file:
        for sor in file.read().splitlines()[1:]:
            épületek.append(Épület(sor))

    # 3. Határozza meg és írja ki a képernyőre a minta szerint,
    # hogy hány épület található az állományban!
    # Minta: 3. feladat: Épületek száma: 136 db
    print(f'3. feladat: Épületek száma: {len(épületek)} db')

    # 4. Határozza meg és írja ki a képernyőre a minta szerint az állományba
    # található épületek emeleteinek az összegét!
    # Minta: 4. feladat: Emeletek összege: 5964
    emeletek_összege: int = 0
    for e in épületek:
        emeletek_összege += e.emelet
    print(f'4. feladat: Emeletek összege: {emeletek_összege}')

    # 5. Határozza meg és írja ki a képernyőre a minta szerint, a legmagasabb épület
    # adatait! Feltételezheti, hogy nem alakult ki holtverseny!
    print('5. feladat: A legmagasabb épület adatai')
    legmagasabb_épület: Épület = épületek[0]
    for e in épületek[1:]:
        if e.magasság > legmagasabb_épület.magasság:
            legmagasabb_épület = e
    print(f'\tNév: {legmagasabb_épület.név}')
    print(f'\tVáros: {legmagasabb_épület.város}')
    print(f'\tOrszág: {legmagasabb_épület.ország}')
    print(f'\tMagasság: {legmagasabb_épület.magasság} m')
    print(f'\tEmeletek száma: {legmagasabb_épület.emelet}')
    print(f'\tÉpítés éve: {legmagasabb_épület.épült}')

    # 6. Döntse el, hogy az adatok között található-e olasz épület!
    # A keresését ne folytassa, ha a választ meg tudja adni!
    # A képernyőre írást a minta szerint végezze!
    van_olasz_épület: bool = False
    for e in épületek:
        if e.ország == 'Olaszország':
            van_olasz_épület = True
            break
    print(f'6. feladat: {"Van" if van_olasz_épület else "Nincs"} olasz épület az adatok között!')

    # 7. Határozza meg és írja ki a képernyőre a minta szerint azoknak az épületeknek a számát,
    # melyek 666 lábnál magasabbak! Az átváltáshoz az 1 m = 3.280839895 láb értékkel dolgozzon!
    # Minta: 7. feladat: 666 lábnál magasabb épületek száma: 32
    LÁB_VÁLTÓSZÁM: float = 3.280839895
    magas_épületek_száma: int = 0
    for e in épületek:
        if e.magasság * LÁB_VÁLTÓSZÁM > 666:
            magas_épületek_száma += 1
    print(f'7. feladat: 666 lábnál magasabb épületek száma: {magas_épületek_száma}')

    # 8. Készítsen statisztikát országok szerint az épületek számáról!
    # A képernyőre írást a minta szerint végezze!
    print('8. feladat: Ország statisztika')
    stat: dict[str, int] = dict()
    for e in épületek:
        if e.ország in stat:  # az ország, mint kulcs a szótárban található-e?
            # stat[e.ország] = stat[e.ország] + 1
            # vagy:
            stat[e.ország] += 1
        else:
            stat[e.ország] = 1
    for key, value in stat.items():  # szótár bejárása for-in ciklussal
        print(f'\t{key} - {value} db')

    # HF: Előző (szótáras) feladat megoldása szótár nélkül, csak listákkal!
    # országok: list[str] = []
    # darabszámok: list[int] = []
    # for e in épületek:
    #     if e.ország in országok:
    #         darabszámok[országok.index(e.ország)] += 1
    #     else:
    #         országok.append(e.ország)
    #         darabszámok.append(1)

    # 9. A nemet.txt állományba írja ki azoknak a német városoknak a nevét, melyekben
    # épület található a forrásadatok szerint! Az állományba a városok nevei egymás alá
    # kerüljenek a minta szerint! Oldja meg, hogy a városnevek ne ismétlődjenek az állományban!

    # Minta nemet.txt:
    # Frankfurt
    # Lipcse
    # Köln
    # München
    # Jéna
    # Bonn

    print('9. feladat: nemet.txt állomány létrehozása')
    német_városok: list[str] = []
    for e in épületek:
        if e.ország == 'Németország' and e.város not in német_városok:
            német_városok.append(e.város)
    with open('nemet.txt', 'w', encoding='utf-8') as file:
        for város in német_városok:
            file.write(f'{város}\n')


if __name__ == "__main__":
    main()
