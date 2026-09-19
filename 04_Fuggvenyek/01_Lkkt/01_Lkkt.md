# LKKT — legkisebb közös többszörös — tanulói segédlet

Futtatás:

```bash
python main.py
```

## 1. A feladat

Két szám **legkisebb közös többszöröse**: a legkisebb olyan szám, ami mindkettővel
maradék nélkül osztható.

## 2. Az algoritmus

Ötlet: vegyük a **nagyobbik szám** többszöröseit egymás után, és álljunk meg az elsőnél,
ami a **kisebbikkel is** osztható.

```python
def lkkt(a: int, b: int) -> int:
    if a > b:
        nsz: int = a
        ksz: int = b
    else:
        nsz: int = b
        ksz: int = a
    osztandó: int = nsz              # a nagyobb szám első többszöröse
    while osztandó % ksz != 0:
        osztandó += nsz              # a nagyobb szám következő többszöröse
    return osztandó
```

Az első `if-else` a **maximum- és minimumkiválasztás** tétele. Ugyanez rövidebben a
beépített függvényekkel (a kódban kikommentezve szerepel):

```python
ksz: int = min(a, b)
nsz: int = max(a, b)
```

Miért a **nagyobbik** szám többszöröseit nézzük? Mert így kevesebb lépésből érünk célba.

Kövessük végig `a = 4`, `b = 6` esetén (`nsz = 6`, `ksz = 4`):

| osztandó | `osztandó % 4` | folytatjuk? |
| --- | --- | --- |
| 6 | 2 | igen |
| 12 | 0 | **nem → LKKT = 12** |

## 3. Véletlen számok

```python
import random

a: int = random.randint(1, 999)
```

A `random.randint(alsó, felső)` **mindkét határt beleértve** ad véletlen egészet. Így a
program minden futtatáskor más adatokkal dolgozik — jó tesztelési szokás.

## 4. Miért írjuk ki a szorzatot is?

A program kiírja `a * b` értékét is. Érdemes megfigyelni az összefüggést:

```
a * b = LNKO(a, b) * LKKT(a, b)
```

Ebből az LKKT gyorsabban is számolható, ha már van LNKO-nk
(lásd *03_Ciklusok/01_Lnko*):

```python
def lkkt_gyors(a: int, b: int) -> int:
    return a * b // lnko(a, b)
```

## 5. Feladatok

1. Írd át a függvényt úgy, hogy a `min()` és `max()` beépített függvényeket használja.
2. Ellenőrizd több véletlen számpáron, hogy `a * b == lnko(a, b) * lkkt(a, b)`.
3. Mi történik, ha az egyik szám 0? Hogyan védenéd ki?
