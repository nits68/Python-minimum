from FilmBemutató import FilmBemutató


def main() -> None:
    # 3.1 Olvassa be az UTF-8 kódolású  nyitohetvege.txt állományban lévő adatokat
    # és tárolja el egy saját osztály típusú listában!
    # Ügyeljen rá, hogy az állomány első sora az adatok fejlécét tartalmazza!
    fb: list[FilmBemutató] = []
    with open('nyitohetvege.txt', 'r', encoding='utf-8') as sr:
        for sor in sr.read().splitlines()[1:]:
            fb.append(FilmBemutató(sor))

    # 3.2 Határozza meg és írja ki a képernyőre a minta szerint,
    # hogy hány filmbemutató található az állományban!
    print(f'3.2 feladat: Filmbemutatók száma: {len(fb)} db')

    # 3.3  Összesítse és írja ki a képernyőre a UIP Duna Film forgalmazó
    # (forgalmazó="UIP") első hetes bevételeinek összegét!
    # Az összeg ezres szeparátorral jelenjen meg a minta szerint!
    összeg_UIP: int = 0
    for film in fb:
        if film.forgalmazó == 'UIP':
            összeg_UIP += film.bevétel
    ki_összeg_e_szep: str = f'{összeg_UIP:,} Ft'  # Egyszerűen csak vesszőt tud a Python szeparátorként
    ki_összeg_e_szep = ki_összeg_e_szep.replace(',', ' ')  # Lecseréljük a vesszőket szóközökre
    print(f'3.3 feladat: UIP összes bevétele az 1. héten: {ki_összeg_e_szep}')

    # 3.4  Határozzuk meg az átlagos nézőszámot az InterCom által forgalmazott
    # filmek esetében! Feltételezheti, hogy legalább 1 filmet forgalmazott a cég.
    # Az átlagot a minta szerint 1 tizedesjegyre kerekítve jelenítse meg!
    össz_néző_intercom: int = 0
    db_intercom: int = 0
    for film in fb:
        if film.forgalmazó == 'InterCom':
            össz_néző_intercom += film.látogató
            db_intercom += 1
    print(f'3.4 feladat: Átlagos nézőszám InterCom: {össz_néző_intercom / db_intercom:.1f} fő')

    # 3.5 Kérjen be egy évszámot majd döntse el, hogy az adatok között
    # található-e a megadott évben bemutatott film!
    # A keresését ne folytassa, ha a választ meg tudja adni!
    # A képernyőre írást a minta szerint végezze!
    input_évszám: int = int(input('3.5 feladat:\nKérek egy évszámot: '))
    volt_bemutató: bool = False
    for film in fb:
        if film.bemutató >= f'{input_évszám}.01.01' and film.bemutató <= f'{input_évszám}.12.31':
            volt_bemutató = True
            break
    print(f'3.5 feladat: Volt {input_évszám}-ban/ben bemutató? {"IGEN" if volt_bemutató else "NEM"}')

    # 5. feladat: Keresse meg azt a filmet, ami az első héten a legtöbb látogatót vonzotta
    # a mozikba! Az eredményeket a minta szerint jelenítse meg!

    # Minta: 5. feladat: Legtöbb látogató az első héten:
    #         Eredeti cím: Avengers: Endgame
    #         Magyar cím: Bosszúállók: Végjáték
    #         Forgalmazó: Forum
    #         Bevétel az első héten: 540 481 595 Ft
    #         Látogatók száma: 343240 fő

    legtöbb_néző_film: FilmBemutató = fb[0]
    for film in fb[1:]:
        if film.látogató > legtöbb_néző_film.látogató:
            legtöbb_néző_film = film
    bevétel_e_szep: str = f'{legtöbb_néző_film.bevétel:,} Ft'.replace(',', ' ')
    print('3.6 feladat: Legtöbb látogató az első héten:')
    print(f'\tEredeti cím: {legtöbb_néző_film.eredeti_cím}')
    print(f'\tMagyar cím: {legtöbb_néző_film.magyar_cím}')
    print(f'\tForgalmazó: {legtöbb_néző_film.forgalmazó}')
    print(f'\tBevétel az első héten: {bevétel_e_szep}')
    print(f'\tLátogatók száma: {legtöbb_néző_film.látogató} fő')

    # 6. feladat: Döntse el, hogy található-e az állományban olyan film, melynek mind
    # az eredeti és mind a magyar címében az összes szó "W", vagy "w" karakterrel kezdődik!
    # Feltételezheti, hogy a filmcímekben a szavakat pontosan egy szóköz karakter választja el!

    # Minta: 6. feladat: Ilyen film volt!

    def minden_szó_w_vel_kezdődik(cím: str) -> bool:
        for szó in cím.split(' '):
            if not szó.startswith(('W', 'w')):
                return False
        return True

    volt_w_film: bool = False
    for film in fb:
        if minden_szó_w_vel_kezdődik(film.eredeti_cím) and minden_szó_w_vel_kezdődik(film.magyar_cím):
            volt_w_film = True
            break
    print(f'3.7 feladat: {"Ilyen film volt!" if volt_w_film else "Nem volt ilyen film!"}')

    # 7. feladat: Készítsen pontosvesszővel tagolt szöveges állományt stat.csv néven a minta
    # szerint, melybe forgalmazónként csoportosítva a filmek darabszámát írja! Az állományban
    # csak azok a forgalmazók szerepeljenek, ahol a filmek száma egynél nagyobb! Az állomány
    # első sora a mezőneveket tartalmazza a minta szerint!

    # Minta stat.csv:
    # forgalmazo;filmekSzama
    # UIP;57
    # Forum;61
    # InterCom;92
    # Big Bang Media;52
    # MoziNet;35

    print('3.8 feladat: stat.csv állomány létrehozása')
    forgalmazói_statisztika: dict[str, int] = {}
    for film in fb:
        if film.forgalmazó in forgalmazói_statisztika:
            forgalmazói_statisztika[film.forgalmazó] += 1
        else:
            forgalmazói_statisztika[film.forgalmazó] = 1
    with open('stat.csv', 'w', encoding='utf-8') as file:
        file.write('forgalmazo;filmekSzama\n')
        for forgalmazó, db in forgalmazói_statisztika.items():
            if db > 1:
                file.write(f'{forgalmazó};{db}\n')

    # 8. feladat: Határozza meg az InterCom forgalmazó esetében, hogy hány nap volt
    # a leghosszabb időszak két filmjük bemutatása között! Feltételezheti, hogy az
    # InterCom legalább két filmje megtalálható az állományban! Megoldása úgy is
    # teljes értékű, ha a szökőnapokkal nem számol!

    # Minta: 3.9 feladat: A leghosszabb időszak két InterCom-os bemutató között: 36 nap

    from datetime import date

    intercom_dátumok: list[date] = []
    for film in fb:
        if film.forgalmazó == 'InterCom':
            év, hó, nap = film.bemutató.split('.')
            intercom_dátumok.append(date(int(év), int(hó), int(nap)))
    intercom_dátumok.sort()

    leghosszabb_időszak: int = 0
    for i in range(1, len(intercom_dátumok)):
        eltelt_napok: int = (intercom_dátumok[i] - intercom_dátumok[i - 1]).days
        if eltelt_napok > leghosszabb_időszak:
            leghosszabb_időszak = eltelt_napok
    print(f'3.9 feladat: A leghosszabb időszak két InterCom-os bemutató között: {leghosszabb_időszak} nap')


if __name__ == "__main__":
    main()
