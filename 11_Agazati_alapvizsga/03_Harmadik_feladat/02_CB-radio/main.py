from CBadas import CBadas
# from typing import List # Python 3.8.X, vagy alatta kell


def main() -> None:
    print('CB-Rádió')
    # 2. feladat: Olvassa be és tárolja el a cb.txt UTF-8 kódolású szöveges
    # állományban található adatokat!
    # Az összetartozó adatokat saját osztály definiálásával kezelje!
    # A fájl soraiban található adatokat saját osztály típusú listában tárolja!
    # Ügyeljen rá, hogy az állomány első sora a mezőneveket tartalmazza!

    # adasok: List[CBadas] = [] # Python 3.8.X, vagy alatta
    adasok: list[CBadas] = []
    with open('cb.txt', 'r', encoding='utf-8') as file:
        for sor in file.read().splitlines()[1:]:
            # aktAdas: CBadas = CBadas(sor)
            # adasok.append(aktAdas)
            # vagy:
            adasok.append(CBadas(sor))

    # 3. feladat: Határozza meg és írja ki a képernyőre a minta szerint,
    # hogy hány bejegyzés található a forrásállományban!

    # Minta: 3. feladat: Bejegyzések száma: 381 db

    print(f'3. feladat: Bejegyzések száma: {len(adasok)} db')

    # 4. feladat: Döntse el és írja ki a képernyőre a minta szerint, hogy található-e
    # a naplóban olyan bejegyzés, amely szerint a sofőr egy percen belül pontosan
    # 4 adást indított! A keresést ne folytassa, ha az eredményt meg tudja határozni!

    # Minta: 4. feladat: Volt négy adást indító sofőr.

    volt_négy_adásos: bool = False
    for adas in adasok:
        if adas.adas_db == 4:
            volt_négy_adásos = True
            break
    print(f'4. feladat: {"Volt" if volt_négy_adásos else "Nem volt"} négy adást indító sofőr.')

    # 5. feladat: Kérje be a felhasználótól egy sofőr nevét, majd határozza meg a sofőr
    # által indított hívások számát a napló bejegyzéseiből! Az eredményt a minta szerint
    # írja ki a képernyőre! Ha olyan sofőr nevét adja meg a felhasználó, aki nem szerepel
    # a naplóban, akkor a "Nincs ilyen nevű sofőr!" mondat jelenjen meg!

    # Minta, ha szerepel a megadott nevű sofőr:
    # 5. feladat: Kérek egy nevet: Laci
    #         Laci 34x használta a CB-rádiót.
    # Minta, ha nem szerepel a megadott nevű sofőr:
    # 5. feladat: Kérek egy nevet: Vera
    #         Nincs ilyen nevű sofőr!

    kért_név: str = input('5. feladat: Kérek egy nevet: ')
    hívások_száma: int = 0
    szerepel: bool = False
    for adas in adasok:
        if adas.nev == kért_név:
            szerepel = True
            hívások_száma += adas.adas_db
    if szerepel:
        print(f'\t{kért_név} {hívások_száma}x használta a CB-rádiót.')
    else:
        print('\tNincs ilyen nevű sofőr!')

    # 6. feladat: Készítsen atszamol_percre azonosítóval egész típusú értékkel visszatérő metódust
    # a saját osztályban, ami a az óra- és percértéket percekre számolja át!
    # Egy óra 60 percből áll. Például: 8 óra 5 perc esetén a visszatérési érték: 485 (perc).
    # Lásd: CBadas.atszamol_percre()

    # 7. feladat: Készítsen szöveges állományt cb2.txt néven, melybe a forrásállományban található
    # bejegyzéseket írja ki új formátumban! Az órákat és a perceket percekre számolja át az
    # elkészített metódus hívásával! Az új állomány első sorát és az adatsorokat a minta szerint alakítsa ki!

    # Minta cb2.txt:
    # Kezdes;Nev;AdasDb
    # 360;Laci;2
    # 361;Bandi;3
    # ...

    print('7. feladat: cb2.txt állomány létrehozása')
    with open('cb2.txt', 'w', encoding='utf-8') as file:
        file.write('Kezdes;Nev;AdasDb\n')  # fejlécsor kiírása
        for adas in adasok:
            file.write(f'{adas.atszamol_percre()};{adas.nev};{adas.adas_db}\n')

    # 8. feladat: Határozza meg és írja ki a minta szerint a sofőrök számát a forrásállományban
    # található becenevek alapján! Feltételezheti, hogy nincs két azonos becenév.

    # Minta: 8. feladat: Sofőrök száma: 19 fő

    sofőrök: set[str] = set()
    for adas in adasok:
        sofőrök.add(adas.nev)
    print(f'8. feladat: Sofőrök száma: {len(sofőrök)} fő')

    # 9. feladat: Határozza meg a legtöbb adást indító sofőr nevét! A sofőr neve és az
    # általa (a napló összes bejegyzésében összesen) indított hívások száma
    # a minta szerint jelenjen meg a képernyőn!

    # Minta: 9. feladat: Legtöbb adást indító sofőr
    #         Név: Sanyi
    #         Adások száma: 68 alkalom

    sofőrönkénti_összesítés: dict[str, int] = {}
    for adas in adasok:
        if adas.nev in sofőrönkénti_összesítés:
            sofőrönkénti_összesítés[adas.nev] += adas.adas_db
        else:
            sofőrönkénti_összesítés[adas.nev] = adas.adas_db
    legtöbb_adást_indító_sofőr: str = ''
    legtöbb_adás_száma: int = 0
    for név, összes_adás in sofőrönkénti_összesítés.items():
        if összes_adás > legtöbb_adás_száma:
            legtöbb_adást_indító_sofőr = név
            legtöbb_adás_száma = összes_adás
    print('9. feladat: Legtöbb adást indító sofőr')
    print(f'\tNév: {legtöbb_adást_indító_sofőr}')
    print(f'\tAdások száma: {legtöbb_adás_száma} alkalom')

    # Kiegészítő feladat (nem az official feladatsor része): melyik bejegyzésben (egy adott
    # percen belül) volt a legtöbb adás? Holtverseny esetén az összes ilyen bejegyzés jelenjen meg!

    # Minta:
    # Kiegészítő feladat: Egy percen belüli legtöbb adás:
    #         Idő: 6:42 Darab: 5 Név: Józsi
    #         Idő: 7:25 Darab: 5 Név: Zoli
    #         Idő: 7:43 Darab: 5 Név: Gabi

    max_adas_darab: int = adasok[0].adas_db
    for adas in adasok[1:]:
        if adas.adas_db > max_adas_darab:
            max_adas_darab = adas.adas_db
    print('Kiegészítő feladat: Egy percen belüli legtöbb adás:')
    for adas in adasok:
        if (adas.adas_db == max_adas_darab):
            print(f'\tIdő: {adas.ora}:{adas.perc} Darab: {adas.adas_db} Név: {adas.nev}')


if __name__ == "__main__":
    main()
