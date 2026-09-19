# Listák — tanulói segédlet

Futtatás:

```bash
python main.py
```

## 1. Mi a lista?

A **lista** összetett adatszerkezet (kollekció), amely több, akár különböző típusú adat
tárolására alkalmas. Mi **típusos listákat** használunk: a lista elemei azonos típusúak.

> Más programozási nyelvekben ezt **egydimenziós tömbnek** vagy **vektornak** hívják.

## 2. Lista létrehozása

```python
lista1: list[str] = []                        # üres lista
lista1: list[str] = list()                    # a list() konstruktorral
lista1: list[str] = ["barack", "körte", "szilva", "alma", "szőlő"]   # elemekkel

lista3 = list((1, 2, "a"))                    # tuple-ból
lista4 = list({"a", "e", "i", "o", "u"})      # halmazból
lista5 = list(range(5, 18, 3))                # számsorozatból -> [5, 8, 11, 14, 17]

lista8: list[int] = [0] * 20                  # 20 elemű, csupa 0 lista
```

Az utolsó forma felel meg a C#-beli „20 elemű tömb, alapértelmezett értékekkel"
konstrukciónak.

## 3. Hivatkozás az elemekre (indexelés)

A lista elemeit **0-tól** induló egész számokkal indexeljük:

```python
lista1[0]       # 'barack'      — az első elem
lista1[-1]      # 'szőlő'       — az UTOLSÓ elem (negatív index hátulról számol)
```

**Index­tartomány (szeletelés, slicing)** — `[kezdő:vég]`, a végindex **nem** tartozik bele:

```python
lista1[1:3]     # ['körte', 'szilva']
lista1[1:]      # a 1. indextől a végéig
lista1[:2]      # az elejétől a 2. index ELŐTTIG
lista1[-3:-1]   # ['szilva', 'alma']
```

## 4. Elem módosítása, hossz, bejárás

```python
lista1[0] = "alma"                 # értékadás indexeléssel
len(lista1)                        # az elemek száma (a lista "hossza")
```

A lista elemei elvileg bármikor válthatnak típust (`lista1[0] = True`), de ez kerülendő —
a Pylance figyelmeztetést is ad rá.

Bejárás **index nélkül** (ha csak az elemek kellenek):

```python
for e in lista1:
    print(f"{e} ", end="")
```

Bejárás **indexekkel**:

```python
for i, e in enumerate(lista1):     # egyszerre adja az indexet és az elemet
    print(f"lista1[{i}]={e} ", end="")

for i in range(len(lista1)):       # a hagyományos megoldás
    print(f"lista1[{i}]={lista1[i]} ", end="")
```

**Elnevezés:** az `i`, `j`, `k` neveket **csak indexre** használjuk; ha a ciklusváltozó
magát az elemet tárolja, a neve legyen `e` (vagy beszédes név, pl. `sor`, `elem`).

## 5. Tartalmazásvizsgálat: `in`

```python
if "alma" in lista1:
    print("Az alma érték megtalálható a listában!")
```

## 6. Listaműveletek — a fontosabb metódusok

| Metódus | Mit csinál? |
| --- | --- |
| `append(e)` | elemet fűz a lista **végéhez** |
| `insert(i, e)` | beszúr a megadott indexű elem **elé** |
| `remove(e)` | a megadott **értékű** elem **első** előfordulását törli |
| `pop()` | az **utolsó** elemet törli |
| `pop(i)` | a megadott **indexű** elemet törli |
| `clear()` | kiüríti a listát (`[]`) |
| `count(e)` | hányszor szerepel az adott érték |
| `index(e)` | az első előfordulás **indexe** (ha nincs ilyen: hibát dob) |
| `extend(másik)` | a listát egy másik lista elemeivel bővíti |
| `reverse()` | megfordítja a lista sorrendjét |
| `sort()` | növekvő sorrendbe rendez |
| `sort(reverse=True)` | csökkenő sorrendbe rendez |
| `copy()` | **másolatot** készít |

A `del lista2` utasítás magát a **változót** szünteti meg — utána a névre hivatkozás hibát
ad.

## 7. Figyelem: másolat vagy referencia?

Ez a listák legfontosabb buktatója:

```python
lista2 = lista1        # NEM másolat! A két név UGYANARRA a listára mutat
lista2.pop()
print(lista1)          # lista1 is megváltozott!
```

Valódi másolat kétféleképpen készíthető:

```python
lista2 = lista1.copy()   # 1. módszer
lista5 = list(lista1)    # 2. módszer: list() konstruktorral
```

## 8. Rendezés magyar ékezetekkel

Az alapértelmezett `sort()` a Unicode-kódok szerint rendez, ezért az ékezetes betűk a
sor végére kerülnek. Magyar ábécé szerinti rendezéshez:

```python
import locale

locale.setlocale(locale.LC_ALL, "hu")
lista7.sort(key=locale.strxfrm)
```

## 9. Beágyazott listák — a „kétdimenziós" lista (mátrix)

Egy lista elemei maguk is lehetnek listák:

```python
mátrix: list[list[int]] = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

mátrix[1]        # a 2. sor (indexe 1): [4, 5, 6]
mátrix[1][2]     # a 2. sor 3. eleme: 6
```

Az indexelés sorrendje: **`[sor][oszlop]`**.

Bejárás **egymásba ágyazott ciklussal**:

```python
for sor in mátrix:
    for elem in sor:
        print(elem, end=' ')
    print()          # soremelés minden sor után
```

Adott méretű, feltöltött mátrix előállítása (3 sor × 4 oszlop, csupa 0):

```python
üres_mátrix: list[list[int]] = []
for _ in range(3):
    üres_mátrix.append([0] * 4)
```

Az aláhúzás (`_`) ciklusváltozó-név azt jelzi: **nem használjuk** a ciklusváltozó értékét,
csak a megadott számú ismétlésre van szükségünk.

## 10. Feladatok

1. Kérj be 5 számot listába, és írd ki az összegüket, átlagukat, legnagyobb elemüket.
2. Írd ki a lista elemeit fordított sorrendben — `reverse()` **nélkül**, indexeléssel.
3. Készíts 3×3-as mátrixot, és írd ki a főátló elemeit (`mátrix[i][i]`).
4. Mi lesz a `lista1` tartalma, ha `lista2 = lista1` után `lista2.append('x')`-et hívsz?
