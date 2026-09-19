# Szekvencia — tanulói segédlet

Futtatás:

```bash
python main.py
```

## 1. Mi a szekvencia?

A **szekvencia** a legegyszerűbb vezérlési szerkezet: az utasítások **fentről lefelé**
(top-down), a **leírás sorrendjében** hajtódnak végre. Nincs se feltétel, se ismétlés.

A példaprogram egy téglalap kerületét és területét számolja ki.

## 2. Kiírás: `print()`

A `print()` függvénnyel változók, literálok és kifejezések értékét jelenítjük meg a
konzolablakban.

```python
print('Téglalap kerülete és területe')
```

## 3. Adatbekérés: `input()`

Az `input()` függvény **mindig szöveget (`str`) ad vissza**, akkor is, ha a felhasználó számot
gépelt be. Ezért a beolvasott értéket **át kell alakítani** (konvertálni) a kívánt típusra:

```python
a: float = float(input('a= '))
```

| Konvertáló függvény | Mire alakít | Példa |
| --- | --- | --- |
| `float()` | valós szám | `float('3.14')` → `3.14` |
| `int()` | egész szám | `int('68')` → `68` |
| `str()` | szöveg | `str(3.14)` → `'3.14'` |

Az `input()` paramétere az a szöveg, ami **kiíródik a bekérés előtt** (itt: `a= `).

## 4. A használt operátorok

| Jel | Jelentés |
| --- | --- |
| `+` | összeadás |
| `*` | szorzás |
| `=` | értékadás |
| `( )` | zárójel — függvények paraméterei, illetve a műveleti sorrend felülbírálása |

```python
terület: float = a * b
kerület: float = 2 * (a + b)
```

A kerület képletében a zárójel **kötelező**: nélküle előbb a szorzás hajtódna végre.

## 5. f-string — így írj ki értékeket

Az f-string olyan speciális szövegliterál, amibe **kapcsos zárójelek között** változók és
kifejezések értéke illeszthető. Az `f` betű a nyitó aposztróf elé kerül:

```python
print('T = ' + str(terület))  # nem ajánlott módszer
print(f'K = {kerület}')       # HASZNÁLJ f-STRINGET!
```

A kapcsos zárójelbe kifejezés is kerülhet: `f'T = {a * b}'`.

## 6. Ékezetes változónevek

A Python megengedi az ékezetes azonosítót (`terület`, `kerület`) — a példaprogramok élnek is
ezzel a magyar nyelvű olvashatóság kedvéért. Nagyobb, vagy nemzetközi projektben ez nem szokás, ott angol nyelvű azonosítókat használunk.

## 7. Feladatok

1. Egészítsd ki a programot a téglalap **átlójának** kiszámításával.
2. Írj hasonló programot, ami egy **kör** kerületét és területét számolja (`r` bekérésével).
3. Mi történik, ha az `a= ` kérdésre betűt gépelsz? Miért?
