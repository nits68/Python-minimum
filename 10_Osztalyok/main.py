# Az osztály a programozási nyelvek legfontosabb összetett adattípusai
# Biztosítják az adatok és a rajtuk műveletet végző függvények (kódtagok) egységét
# A függvényeket gyakran metódusoknak hívjuk
# Az osztály változóit (adattagjait) gyakran mezőknek is hívjuk
# Az adat- és kódtagok klasszikus láthatósági szintjét (public, private, protected, stb.)
#   a Python nem különbözteti meg, a protected tagok jelölésére van csak módunk (de ezt nem tesszük meg az alapozó vizsgáig)
# Egy osztályt leggyakrabban csak példányosítás után használhatunk
# Az osztály konstruktora egy speciális metódus, jellemzően az adattagok inicializálását végzi,
#   felkészíti az osztálypéldányt a használatra
# A konstruktor automatikusan hívódik az osztálypéldány létrehozásakor
# A konstruktor Pythonban kötelezően az __init__ nevet kapja
# Az osztálypéldányt gyakran objektumnak is hívjuk
# A self foglalt szóval az aktuális osztálypéldány adat- és kódtagjait érjük el osztályon belül,
#   kötelezően minden kódtag első paramétere, adattípus nélkül
# A Python forrásállomány neve gyakran az osztály nevével egyezik meg (itt Hőmérséklet.py kéne hogy legyen)
# Ha az osztályra másik forrásállományba van szükségünk, akkor azt importálni kell, pl.:
#   from Hőmérséklet import Hőmérséklet

# A Homerseklet osztály definiálása:

class Hőmérséklet:  # a class foglalt szó után adjuk meg az osztály azonosítóját (nevét)
    érték_fok: float  # adattag (mező)
    feldolgozás_alatt: bool  # adattag (mező)

    def __init__(self, értek_fok: float) -> None:  # az osztály konstruktora, speciális metódusa
        self.érték_fok = értek_fok
        self.feldolgozás_alatt = False
        # A konstruktorban is létrehozhatunk adattagokat, de ezt javasolt elkerülni!

    def valtoztat(self, delta_fok: float) -> None:  # az osztály kódtagja, metódusa
        self.érték_fok += delta_fok

    def értek_fahrenheit(self) -> float:  # az osztály kódtagja, metódusa
        return (self.érték_fok * 1.8) + 32


class LáthatóságiSzintekTeszt:
    mező1_pub: int  # Publikus mező (alapértelmezés, a leg "megengedőbb" láthatósági szint)
    _mező2_prot: int  # Protected mező (csak osztályon belül és a leszármazott osztályokban használható)
    __mező3_priv: int  # Private mező (csak osztályon belül használható, a legszigorúbb láthatósági szint)

    # A jellemzők használatával a private és protected mezők olvasását és írását felügyelhetjük
    @property
    def jellemző2(self) -> int:
        return self._mező2_prot

    @jellemző2.setter
    def jellemző2(self, new_value: int) -> None:
        if new_value % 2 == 0:
            self._mező2_prot = new_value
        else:
            raise ValueError("Csak páros szám kerülhet a védett mezőbe!")

    @property
    def jellemző3(self) -> int:
        return self.__mező3_priv

    @jellemző3.setter
    def jellemző3(self, new_value: int) -> None:
        if new_value % 2 == 1:
            self.__mező3_priv = new_value
        else:
            raise ValueError("Csak páratlan szám kerülhet a védett mezőbe!")

    def __init__(self):
        self.mező1_pub = 11
        self._mező2_prot = 22
        self.__mező3_priv = 33


def main() -> None:
    print('Osztályok - objektumok')
    testhő: Hőmérséklet = Hőmérséklet(37)  # osztálypéldány (objektum) létrehozása
    # testho => objektum (osztálypéldány) azonosítója (neve)
    # Homerseklet => Osztály azonosítója (neve)
    # Homerseklet(37) => Osztály konstruktora az aktuális (37) paraméterrel
    # A példány (objektum) létrehozásakor a konstruktor (__init__) automatikusan meghívásra kerül

    # az adattagok elérése osztálypéldány felől
    testhő.feldolgozás_alatt = True
    print(testhő.feldolgozás_alatt)  # a tagok osztálypéldány felől is elérhetők (írhatók, olvashatók)
    print(testhő.érték_fok)
    testhő.érték_fok = 36.4
    print(testhő.érték_fok)

    # kódtagok hívása:
    print(testhő.értek_fahrenheit())
    testhő.valtoztat(10.5)

    print(testhő.érték_fok)

    print('Osztályok - Láthatósági szintek')
    t = LáthatóságiSzintekTeszt()
    t.mező1_pub = 123  # A publikus adattagok felügyelet nélkül írhatók és olvashatók, ami veszélyes lehet1, ezért kerülendő használatuk
    print(t.mező1_pub)

    # print(teszt._mező2)  # Pythonban elérjük a protected mezőket, de figyelmeztet a Pylance a hibára
    # print(teszt.__mező3)  # A private mezők már nem érhetők el

    try:
        print(t.jellemző2)
        t.jellemző2 = 222
        print(t.jellemző2)
        t.jellemző2 = 223  # Ez az értékadás hibát fog "dobni", mert az új érték nem páros
    except ValueError as ex:
        print(ex)


if __name__ == "__main__":
    main()
