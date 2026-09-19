# Tuple-ök — tanulói segédlet

Futtatás:

```bash
python main.py
```

## 1. Mi a tuple?

A **tuple** olyan kollekció, ami a listához hasonlít — sorrendtartó és indexelhető —, de
**nem módosítható** (angolul: *immutable*, megváltoztathatatlan). Gyakorlatilag
**konstans lista**.

Mire jó? Olyan adatokra, amiknek **nem szabad** megváltozniuk: a hét napjai, egy pont
koordinátái, egy konfigurációs érték.

## 2. Tuple létrehozása

```python
tuple1: tuple[str, str, str, str, str] = ('barack', 'körte', 'szilva', 'alma', 'szőlő')
tuple2 = ()                                  # üres tuple
tuple3 = tuple((1, 2, 3))                    # tuple-ból
tuple4 = tuple({'a', 'e', 'i', 'o', 'u'})    # halmazból (a sorrend véletlenszerű lesz!)
tuple5 = tuple(['a', 'e', 'i', 'o', 'u'])    # listából
```

Zárójel: **kerek** (`( )`) — szemben a lista szögletes és a halmaz/szótár kapcsos
zárójelével.

## 3. Indexelés — ugyanúgy, mint a listánál

```python
tuple1[0]       # 'barack'
tuple1[1:3]     # ('körte', 'szilva')
tuple1[1:]      # az 1. indextől a végéig
tuple1[:2]      # az elejétől a 2. index előttig
tuple1[-1]      # 'szőlő' — az utolsó elem
tuple1[-3:-1]   # ('szilva', 'alma')
```

## 4. Értékadás NEM lehetséges

```python
# tuple1[0] = 'alma'   # HIBA: a tuple elemei nem módosíthatók
```

Ez a tuple lényege — épp ez védi meg az adatot a véletlen felülírástól.

## 5. Bejárás, tartalmazásvizsgálat, hossz

```python
for e in tuple1:                              # index nélkül
    print(f'{e} ', end='')

for index, item in enumerate(tuple1):         # indexszel
    print(f'tuple1[{index}]={item} ', end='')

if 'barack' in tuple1:                        # tartalmazásvizsgálat
    print('A barack érték megtalálható!')

len(tuple1)                                   # 5 — az elemszám
```

## 6. Metódusok

A tuple-nek — épp a módosíthatatlansága miatt — csak **két** metódusa van:

| Metódus | Mit csinál? |
| --- | --- |
| `count(e)` | hányszor szerepel a megadott érték |
| `index(e)` | az első előfordulás indexe |

```python
tuple6 = (4, 5, 6, 5, 5, 3, 4, 5, 6)
tuple6.count(5)   # 4
tuple6.index(6)   # 2
```

## 7. „Módosítás" trükkel: konverzió listává és vissza

```python
lista6: list[int] = list(tuple6)
lista6[1] = 7
tuple6 = tuple(lista6)
print(tuple6)   # (4, 7, 6, 5, 5, 3, 4, 5, 6)
```

Valójában nem az eredeti tuple változott meg — **új** tuple jött létre.

## 8. Tuple-ök összefűzése

```python
tuple7 = tuple3 + tuple4   # (1, 2, 3, 'o', 'i', 'a', 'e', 'u')
```

A `+` itt is új tuple-t hoz létre.

## 9. Az egyelemű tuple csapdája

```python
tuple1elemmel = ("apple",)   # a vessző kell! -> <class 'tuple'>
tuple1elemmel = ("apple")    # vessző nélkül EGYSZERŰ SZÖVEG -> <class 'str'>
```

Az egyelemű tuple után **ki kell tenni a vesszőt**, különben a zárójel csak csoportosító
zárójelnek számít.

## 10. A négy kollekció összehasonlítása

| | lista | tuple | halmaz | szótár |
| --- | --- | --- | --- | --- |
| zárójel | `[ ]` | `( )` | `{ }` | `{k: é}` |
| sorrendtartó | igen | igen | nem | igen (beszúrási) |
| indexelhető | igen | igen | nem | kulccsal |
| módosítható | igen | **nem** | csak add/remove | igen |
| ismétlődhet | igen | igen | **nem** | kulcs nem |

## 11. Feladatok

1. Tárold a hét napjait tuple-ben, és írasd ki a 3. napot.
2. Mi történik, ha megpróbálsz értéket adni egy tuple elemének? Olvasd el a hibaüzenetet!
3. Írj függvényt, ami egy tuple-ből visszaadja a legnagyobb és a legkisebb elemet.
