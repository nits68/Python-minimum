# Modulok és csomagok — tanulói segédlet

Futtatás:

```bash
python main.py
```

## 1. Fogalmak

**Modul**: olyan (jellemzően `.py` kiterjesztésű) állomány, amely Python kódot —
függvényeket, osztályokat, változókat — tartalmaz, és amit más programokból **importálva**
újra fel tudunk használni. A modulokkal a kódot logikailag elkülönülő, jól kezelhető
egységekre bontjuk.

**Csomag (package)**: modulok rendezett gyűjteménye egy könyvtárban. Régebbi Python
verziókban egy üres `__init__.py` állomány jelezte, hogy a könyvtár csomag; újabb
verziókban ez már nem kötelező (ún. *namespace package*).

## 2. Az importálás módjai

```python
import math                # a teljes modul importálása
import math as m           # ÁLNÉV (alias) adása az "as" kulcsszóval
from math import sqrt      # EGYETLEN név importálása
from math import *         # a modul ÖSSZES nyilvános neve — körültekintően használandó!
import sajat_modul         # saját, a projektben elkészített modul
```

Használat a különböző formák szerint:

```python
math.sqrt(16)   # import math esetén: ki kell írni a modul nevét
m.pi            # import math as m esetén
sqrt(16)        # from math import sqrt esetén: NEM kell a "math." előtag
```

A `from modul import *` azért veszélyes, mert **névütközést** okozhat: felülírhat egy
azonos nevű saját függvényt, és nem látszik, honnan származik egy név.

Az `import` utasítások a **fájl elejére** kerülnek.

## 3. A `math` modul

Matematikai konstansokat és függvényeket tartalmaz:

| Hívás | Eredmény |
| --- | --- |
| `math.pi` | 3.141592653589793 |
| `math.sqrt(16)` | `4.0` — négyzetgyök |
| `math.pow(2, 10)` | `1024.0` — hatványozás |
| `math.floor(3.7)` | `3` — lefelé kerekítés |
| `math.ceil(3.2)` | `4` — felfelé kerekítés |

## 4. A `random` modul

| Hívás | Mit ad? |
| --- | --- |
| `random.randint(1, 6)` | véletlen **egész** az **[1, 6] zárt** intervallumból |
| `random.random()` | véletlen **valós** a `[0.0, 1.0)` intervallumból |
| `random.choice(lista)` | véletlenül kiválasztott **elem** egy listából |

## 5. A `platform` modul

A futtató környezetről ad információt:

```python
platform.system()           # 'Windows', 'Linux' vagy 'Darwin' (macOS)
platform.python_version()   # pl. '3.12.4'
```

## 6. Mi van egy modulban? — a `dir()`

A `dir()` beépített függvény kilistázza egy modul (vagy objektum) elérhető neveit:

```python
print([név for név in dir(random) if not név.startswith('_')][:10])
```

Az aláhúzással kezdődő nevek **belső használatúak**, ezeket szűrjük ki.

A beépített (standard library) modulok hivatalos listája és dokumentációja:
<https://docs.python.org/3/py-modindex.html>

## 7. Saját modul készítése

A `sajat_modul.py` egyszerűen egy `.py` forrásállomány ugyanabban a mappában. A modul
neve megegyezik az állomány nevével, **kiterjesztés nélkül**.

```python
# sajat_modul.py
PI_KÖZELÍTŐ_ÉRTÉK: float = 3.14        # konstans (csupa nagybetűs név!)


def négyzet_területe(oldal: float) -> float:
    return oldal * oldal


def kör_területe(sugár: float) -> float:
    return PI_KÖZELÍTŐ_ÉRTÉK * sugár * sugár
```

Használat a `main.py`-ból:

```python
import sajat_modul

sajat_modul.négyzet_területe(5)
sajat_modul.kör_területe(3)
sajat_modul.PI_KÖZELÍTŐ_ÉRTÉK
```

## 8. Végre érthető: mire jó az `if __name__ == "__main__":`

Minden modulban van egy `__name__` nevű beépített változó:

- ha az állományt **önállóan futtatod**, az értéke `"__main__"`,
- ha **importálod**, az értéke a **modul neve** (itt: `"sajat_modul"`).

Ezért az ebbe a blokkba írt kód **csak önálló futtatáskor** fut le, importáláskor **nem**:

```python
if __name__ == "__main__":
    print('A sajat_modul.py-t importálás nélkül, önállóan futtattad!')
```

Ez a magyarázata annak, amit az első fejezet óta minden programunk végén látsz — így
lehet egy állomány egyszerre futtatható program **és** importálható modul.

## 9. Feladatok

1. Bővítsd a `sajat_modul.py`-t egy `téglalap_területe(a, b)` függvénnyel, és hívd meg.
2. Írd át a `kör_területe()` függvényt úgy, hogy a `math.pi` pontos értékét használja.
3. Futtasd önállóan a `sajat_modul.py`-t, majd importáld — figyeld meg a különbséget!
4. Nézd meg a `dir(math)` kimenetét: hány használható neve van a modulnak?
