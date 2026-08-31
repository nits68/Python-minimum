# Modul fogalma: olyan (jellemzően .py kiterjesztésű) állomány, amely Python kódot
# (függvényeket, osztályokat, változókat) tartalmaz, és amit más programokból
# importálva újra fel tudunk használni. A modulok segítségével a kódunkat logikailag
# elkülönülő, jól kezelhető egységekre bonthatjuk.
# Csomag (package): modulok rendezett gyűjteménye egy könyvtárban.
#   A könyvtár csomagként való jelölését (régebbi Python verziókban) egy üres,
#   __init__.py nevű állomány jelezte; újabb Python verziókban ez már nem kötelező
#   (ún. "namespace package").

import math  # beépített (standard library) modul importálása
import random
import platform
import math as m  # a modulnak álnevet (aliast) is adhatunk az "as" kulcsszóval
from math import sqrt  # egyetlen névnek (itt: a sqrt függvénynek) az importálása
from math import *  # a modul ÖSSZES nyilvános nevének importálása (körültekintően használandó!)

import sajat_modul  # saját, a projektben elkészített modul importálása


def main() -> None:
    # A math modul: matematikai konstansokat és függvényeket tartalmaz
    print('A math modul használata')
    print(f'math.pi = {math.pi}')
    print(f'math.sqrt(16) = {math.sqrt(16)}')  # négyzetgyök
    print(f'math.pow(2, 10) = {math.pow(2, 10)}')  # hatványozás
    print(f'math.floor(3.7) = {math.floor(3.7)}')  # lefelé kerekítés
    print(f'math.ceil(3.2) = {math.ceil(3.2)}')  # felfelé kerekítés

    # Ugyanaz, az álnévvel (m) és a korábban importált sqrt függvénnyel:
    print(f'm.pi = {m.pi}')
    print(f'sqrt(16) = {sqrt(16)}')  # nem kell kiírni, hogy "math.", mert csak ezt a nevet importáltuk

    # A random modul: véletlenszám-generáláshoz
    print('\nA random modul használata')
    print(f'random.randint(1, 6) = {random.randint(1, 6)}')  # véletlen egész [1, 6] zárt intervallumból
    print(f'random.random() = {random.random()}')  # véletlen valós [0.0, 1.0) intervallumból
    gyümölcsök: list[str] = ['alma', 'körte', 'szilva']
    print(f'random.choice(gyümölcsök) = {random.choice(gyümölcsök)}')  # véletlen elem egy listából

    # A platform modul: a futtató környezetről ad információt
    print('\nA platform modul használata')
    print(f'platform.system() = {platform.system()}')  # pl.: Windows, Linux, Darwin (macOS)
    print(f'platform.python_version() = {platform.python_version()}')

    # A dir() beépített függvény: kilistázza egy modul (vagy objektum) elérhető neveit
    print('\nA dir() függvény használata (a random modul néhány tagja)')
    print([név for név in dir(random) if not név.startswith('_')][:10])

    # Python Module Index: a beépített (standard library) modulok hivatalos listája
    # és dokumentációja: https://docs.python.org/3/py-modindex.html

    # Saját modul használata (lásd: sajat_modul.py, ugyanebben a mappában):
    print('\nSaját modul használata')
    print(f'sajat_modul.négyzet_területe(5) = {sajat_modul.négyzet_területe(5)}')
    print(f'sajat_modul.kör_területe(3) = {sajat_modul.kör_területe(3)}')
    print(f'sajat_modul.PI_KÖZELÍTŐ_ÉRTÉK = {sajat_modul.PI_KÖZELÍTŐ_ÉRTÉK}')


if __name__ == "__main__":
    main()
