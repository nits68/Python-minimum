# Osztályok és objektumok — tanulói segédlet

Futtatás:

```bash
python main.py
```

## 1. Mi az osztály?

Az **osztály** a programozási nyelvek legfontosabb összetett adattípusa. Biztosítja az
**adatok** és a rajtuk műveletet végző **függvények** egységét.

Szóhasználat:

| Általános név | Az osztályon belül |
| --- | --- |
| az osztály változói | **adattagok**, **mezők** |
| az osztály függvényei | **kódtagok**, **metódusok** |
| egy létrehozott osztálypéldány | **objektum** |

Az osztályt leggyakrabban csak **példányosítás** után tudjuk használni.

## 2. Osztály definiálása

```python
class Hőmérséklet:                    # a class foglalt szó után az osztály neve
    érték_fok: float                  # adattag (mező)
    feldolgozás_alatt: bool           # adattag (mező)

    def __init__(self, értek_fok: float) -> None:   # KONSTRUKTOR
        self.érték_fok = értek_fok
        self.feldolgozás_alatt = False

    def valtoztat(self, delta_fok: float) -> None:  # metódus (kódtag)
        self.érték_fok += delta_fok

    def értek_fahrenheit(self) -> float:            # metódus (kódtag)
        return (self.érték_fok * 1.8) + 32
```

### A konstruktor

A **konstruktor** speciális metódus: jellemzően az adattagok **inicializálását** végzi,
felkészíti a példányt a használatra. A példány létrehozásakor **automatikusan** meghívódik.
Pythonban kötelezően az **`__init__`** nevet kapja.

A konstruktorban is létre lehet hozni adattagokat, de ezt **javasolt elkerülni** — az
adattagokat soroljuk fel az osztály elején.

### A `self`

A **`self`** foglalt szóval érjük el az **aktuális osztálypéldány** adat- és kódtagjait az
osztályon belül. **Kötelezően minden kódtag első paramétere**, típusmegadás nélkül.

A `self.érték_fok` az adott objektum mezője; a `self` nélküli `érték_fok` csak egy helyi
változó lenne.

## 3. Példányosítás és használat

```python
testhő: Hőmérséklet = Hőmérséklet(37)
```

- `testhő` → az objektum (osztálypéldány) **azonosítója**,
- `Hőmérséklet` → az **osztály** neve,
- `Hőmérséklet(37)` → a **konstruktor hívása** a 37 aktuális paraméterrel.

Az adattagok elérése az objektum felől, ponttal:

```python
testhő.feldolgozás_alatt = True      # írás
print(testhő.érték_fok)              # olvasás
testhő.érték_fok = 36.4
```

A metódusok hívása ugyanígy — a `self`-et **nem** adjuk át, azt a Python teszi hozzá:

```python
print(testhő.értek_fahrenheit())     # 97.52
testhő.valtoztat(10.5)
```

## 4. Az osztály és az állomány neve

A Python forrásállomány neve gyakran megegyezik az osztály nevével (ebben a példában
`Hőmérséklet.py` lenne az illendő). Ha egy osztály másik állományban van, importálni kell:

```python
from Hőmérséklet import Hőmérséklet
```

> Lásd: *07b_Modulok_es_csomagok*.

## 5. Láthatósági szintek

A klasszikus láthatósági szinteket (`public`, `private`, `protected`) a Python **nem
különbözteti meg** úgy, mint más nyelvek — csak **elnevezési konvenciót** használ:

```python
class LáthatóságiSzintekTeszt:
    mező1_pub: int        # publikus (alapértelmezett, legmegengedőbb)
    _mező2_prot: int      # "protected" — egy aláhúzás: osztályon belül és leszármazottakban
    __mező3_priv: int     # "private"   — két aláhúzás: csak osztályon belül
```

A gyakorlatban:

- a **publikus** mezők felügyelet nélkül írhatók-olvashatók — ez **veszélyes lehet**,
  ezért kerülendő,
- a `_` előtagú mezőket Pythonban *el lehet* érni kívülről, de a Pylance figyelmeztet rá,
- a `__` előtagú mezők kívülről **már nem érhetők el** (a Python átnevezi őket).

## 6. Jellemzők (property) — felügyelt hozzáférés

A jellemzőkkel **felügyelhetjük** a mezők olvasását és írását: ellenőrzést építhetünk az
értékadásba.

```python
@property
def jellemző2(self) -> int:              # GETTER — olvasás
    return self._mező2_prot

@jellemző2.setter
def jellemző2(self, new_value: int) -> None:   # SETTER — írás, ellenőrzéssel
    if new_value % 2 == 0:
        self._mező2_prot = new_value
    else:
        raise ValueError("Csak páros szám kerülhet a védett mezőbe!")
```

Kívülről ez **ugyanúgy néz ki, mint egy sima mező** — zárójel nélkül használjuk:

```python
print(t.jellemző2)      # a getter hívódik
t.jellemző2 = 222       # a setter hívódik: rendben (páros)
t.jellemző2 = 223       # a setter ValueError-t dob (páratlan)
```

Ezért a használatát `try-except`-be tesszük:

```python
try:
    t.jellemző2 = 223
except ValueError as ex:
    print(ex)
```

Ez a lényeg: **az adat csak érvényes értéket vehet fel**, mert az osztály maga őrködik
felette.

## 7. Miért jó az osztály?

- **egységbe zárás**: az adat és a rajta végzett művelet egy helyen van,
- **védelem**: a jellemzőkkel ellenőrzött hozzáférést adhatunk,
- **újrafelhasználhatóság**: egy osztályból tetszőleges számú objektum készíthető.

## 8. Feladatok

1. Készíts `Tanuló` osztályt `név` és `jegy` adattagokkal, konstruktorral és egy
   `megfelelt()` metódussal (igaz, ha a jegy nagyobb 1-nél).
2. Hozz létre több `Hőmérséklet` objektumot, és tedd őket listába — járd be a listát.
3. Egészítsd ki a `Hőmérséklet` osztályt `értek_kelvin()` metódussal (`°C + 273.15`).
4. Védd le a `Hőmérséklet.érték_fok` mezőt jellemzővel úgy, hogy −273.15 alá ne lehessen
   állítani.
