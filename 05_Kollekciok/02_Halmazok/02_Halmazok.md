# Halmazok (set) — tanulói segédlet

Futtatás:

```bash
python main.py
```

## 1. Mi a halmaz?

A **halmaz (set)** olyan kollekció, amelyben:

- **nem lehet két azonos elem** (az ismétlődés automatikusan eltűnik),
- az elemeknek **nincs sorrendje** — ezért **nem indexelhető** (`halmaz[0]` hibát ad!),
- az elemek nem módosíthatók, csak **hozzáadni** és **törölni** lehet őket.

A kiírás sorrendje futásonként változhat — ne építs rá!

## 2. Halmaz létrehozása

```python
halmaz1 = {'barack', 'körte', 'szilva', 'alma', 'szőlő'}   # elemekkel, kapcsos zárójelben
halmaz3 = set({})                                          # ÜRES halmaz
halmaz2 = set(range(10, 15))                               # számsorozatból
halmaz3 = set((1, 2, "a"))                                 # tuple-ból
halmaz4 = set(['a', 'e', 'i', 'o', 'u'])                   # listából
halmaz5: set[str] = {'barack', 'körte'}                    # típusos halmaz
```

**Figyelem:** az üres halmaz **nem** `{}` — az üres **szótár**! Üres halmazhoz `set()` kell.

A `set(lista)` konverzió egyben a **duplikátumok kiszűrésének** bevált módja.

## 3. Tartalmazásvizsgálat

```python
if 'alma' in halmaz1:
    print('Az alma érték megtalálható a halmazban!')
```

Ez a halmaz erőssége: a keresés **nagyon gyors**, sokkal gyorsabb, mint listában.

## 4. Elemek hozzáadása és törlése

| Metódus | Mit csinál? |
| --- | --- |
| `add(e)` | **egy** elem hozzáadása |
| `update({...})` | **több** elem hozzáadása (paramétere lehet lista, halmaz stb.) |
| `discard(e)` | elem törlése — ha nincs ilyen, **nem dob hibát** |
| `remove(e)` | elem törlése — ha nincs ilyen, **hibát dob** |
| `pop()` | egy „véletlen" elem törlése — **ne használd**, nem tudod, melyiket törli |
| `clear()` | a halmaz kiürítése |
| `len(halmaz)` | az elemszám |

```python
halmaz1.add('szilva')   # már létezik -> nem nő az elemszám, és NINCS hibaüzenet
halmaz1.add('répa')
halmaz1.update({'zeller', 'karalábé', 'karfiol'})
```

A `remove()` hibáját `try-except` szerkezettel foghatjuk el:

```python
try:
    halmaz1.remove('karfiol')
    halmaz1.remove('karfiol')   # másodszor már nincs ilyen elem -> KeyError
except Exception as ex:
    print(ex.__doc__)
```

> Bővebben: *08_Kivetelek_kezelese*.

A `del halmaz1` magát a változót szünteti meg.

## 5. Bejárás

```python
for e in halmaz1:
    print(f'{e} ', end='')
```

Index szerinti bejárás nincs — a halmaz nem indexelhető.

## 6. Halmazműveletek

```python
h1 = {"a", "b", "c"}
h2 = {"b", "c", "d"}
```

| Művelet | Metódus | Eredmény |
| --- | --- | --- |
| **unió** (egyesítés) | `h1.union(h2)` | `{'a', 'b', 'c', 'd'}` |
| **metszet** (közös rész) | `h1.intersection(h2)` | `{'b', 'c'}` |
| **különbség** | `h1.difference(h2)` | `{'a'}` |

Érdemes még ismerni: `isdisjoint()` (van-e közös elem), `issubset()` (részhalmaz-e),
`copy()` (másolat).

## 7. Mikor melyiket?

| | lista | halmaz |
| --- | --- | --- |
| sorrend | megmarad | nincs |
| ismétlődés | lehet | nem lehet |
| indexelés | igen | **nem** |
| keresés (`in`) | lassabb | **nagyon gyors** |

## 8. Feladatok

1. Szűrd ki egy lista duplikátumait `set()` segítségével.
2. Két osztály névsorából állítsd elő: kik járnak mindkettőbe (metszet), kik csak az
   elsőbe (különbség).
3. Próbáld ki: mi történik, ha `halmaz1[0]`-ra hivatkozol?
