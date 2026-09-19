# LNKO — legnagyobb közös osztó — tanulói segédlet

Futtatás:

```bash
python main.py
```

A program **két algoritmussal** is meghatározza két szám legnagyobb közös osztóját.

## 1. Kivonásos algoritmus

Ötlet: amíg a két szám nem egyenlő, a **nagyobbikból kivonjuk a kisebbet**. Amikor
egyenlők lesznek, ez a közös érték az LNKO.

```python
while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a
print(f'LNKO = {a}')
```

Kövessük végig `a = 12`, `b = 18` esetén:

| lépés | a | b |
| --- | --- | --- |
| kezdet | 12 | 18 |
| 1. | 12 | 6 |
| 2. | 6 | 6 |

Eredmény: **6**.

Figyeld meg, hogy ez **ciklus + elágazás** egymásba ágyazva: a `while` magjában egy
`if-else` áll.

## 2. Euklideszi algoritmus (maradékos)

Ötlet: mindig az **osztási maradékkal** dolgozunk tovább. Euklidész tétele szerint
**az utolsó nem nulla maradék az LNKO**.

```python
m: int = -1   # biztosan lesz egy ciklusmag-végrehajtás
while m != 0:
    m = a % b   # osztás maradéka
    a = b       # a 2. ismétléstől az előző maradék kerül "a"-ba
    b = m
print(f'LNKO = {a}')
```

`a = 12`, `b = 18` esetén:

| lépés | a | b | m = a % b |
| --- | --- | --- | --- |
| 1. | 12 | 18 | 12 |
| 2. | 18 | 12 | 6 |
| 3. | 12 | 6 | 0 |

A ciklus után `a` értéke **6** — ez a keresett LNKO.

## 3. Hátultesztelő ciklus pótlása

Pythonban **nincs** hátultesztelő (`do-while`) ciklus, pedig itt arra lenne szükség: a
maradékot legalább egyszer ki kell számolni. A trükk a kódban:

```python
m: int = -1        # olyan kezdőérték, ami biztosan teljesíti a feltételt
while m != 0:
    ...
```

Ezzel garantáljuk, hogy a ciklusmag **legalább egyszer** lefusson.

A másik bevett megoldás ugyanerre a `while True` + `break` (lásd: *03_Ciklusok*).

## 4. Melyik a jobb?

Az euklideszi algoritmus **sokkal gyorsabb**: a kivonásos változat pl. `a = 1000000`,
`b = 2` esetén félmillió kört futna, míg az euklideszi egyetlen osztással végez.

## 5. Feladatok

1. Próbáld ki mindkét algoritmust `a = 48`, `b = 18` értékekkel, és írd le a táblázatot.
2. Mi történik, ha `b = 0`? Egészítsd ki a programot ennek kivédésével.
3. Az LNKO ismeretében számold ki a **legkisebb közös többszöröst**: `LKKT = a * b // LNKO`.
   (Lásd: *04_Fuggvenyek/01_Lkkt*.)
