# Lottószámok — tanulói segédlet

Futtatás:

```bash
python main.py
```

## 1. A feladat

Sorsoljunk ki 5 **különböző** számot 1 és 90 között (ötöslottó), majd írjuk ki őket
**növekvő sorrendben**.

## 2. Miért halmazt használunk?

A lottószámok között **nem lehet ismétlődés** — épp ezt garantálja a halmaz. Ha véletlenül
már meglévő számot adnánk hozzá, az elemszám egyszerűen nem nő, és nem kapunk hibát sem.

```python
lotto90: set[int] = set()        # ÜRES halmaz (nem {}, az szótár lenne!)
while len(lotto90) < 5:
    lotto90.add(random.randint(1, 90))
print(lotto90)
```

Ez egy **elöltesztelő (`while`) ciklus** iskolapéldája: előre **nem tudjuk**, hányszor kell
majd ismételni — addig sorsolunk, amíg össze nem gyűlik az 5 szám.

A `random.randint(1, 90)` **mindkét határt beleértve** ad véletlen egészet, ezt importálni
kell: `import random`.

## 3. A rendezés — tartalmazásvizsgálattal

A halmaznak **nincs sorrendje**, ezért a kiíráshoz rendezni kell. A trükk: végigmegyünk az
összes lehetséges számon 1-től 90-ig, és amelyik benne van a halmazban, azt hozzáfűzzük
egy listához:

```python
lotto90rendezve: list[int] = []
for szam in range(1, 91):        # 1..90
    if szam in lotto90:
        lotto90rendezve.append(szam)
print(lotto90rendezve)
```

Mivel a `range` növekvő sorrendben halad, a lista **eleve rendezett** lesz.

Ez a **kiválogatás** programozási tétele (lásd: *07_Programozasi_tetelek*).

## 4. Rövidebb megoldás

Ugyanez egyetlen sorban, a beépített `sorted()` függvénnyel:

```python
print(sorted(lotto90))
```

A `sorted()` bármilyen kollekcióból **rendezett listát** készít. A kódban szereplő
hosszabb megoldás viszont jól mutatja a tartalmazásvizsgálat és a kiválogatás működését.

## 5. Feladatok

1. Írd át a programot **hatoslottóra** (6 szám 1–45 között).
2. Sorsolj egy második „szelvényt" is, és írd ki, hány találat van (metszet!).
3. Mi történne, ha halmaz helyett listát használnál? Hogyan kellene kivédeni az
   ismétlődést?
