# Prímszámvizsgálat — tanulói segédlet

Futtatás:

```bash
python main.py
```

**Prímszám**: olyan 1-nél nagyobb egész, aminek pontosan **két** osztója van (1 és önmaga).

A program két megoldást mutat ugyanarra a feladatra — érdemes összevetni őket.

## 1. „Favágó" módszer — az osztók megszámlálása

```python
def prime_favágó(szám: int) -> bool:
    osztók_száma: int = 0
    for osztó in range(1, szám + 1):
        if szám % osztó == 0:
            osztók_száma += 1
    return osztók_száma == 2
```

Végigmegyünk **minden** lehetséges osztón 1-től a számig, és megszámoljuk a valódi
osztásokat (**megszámlálás tétele**). A szám akkor prím, ha pontosan 2 osztója van — ezért
ad `False`-t az 1-re is (annak csak egy osztója van).

A `return osztók_száma == 2` sor egy **logikai kifejezés** értékét adja vissza — nem kell
hozzá `if`!

Előnye: egyszerű, rövid, biztosan jó. Hátránya: **lassú**, `n` darab osztást végez.

## 2. Optimalizált megoldás

```python
def prime(szam: int) -> bool:
    if szam > 2 and szam % 2 == 0 or szam == 1:
        return False
    szam_gyoke: int = int(math.sqrt(szam))
    for oszto in range(3, szam_gyoke + 1, 2):
        if szam % oszto == 0:
            return False
    return True
```

Három gyorsító ötlet:

1. **Az 1 és a 2-nél nagyobb páros számok** biztosan nem prímek → azonnal `False`.
2. Elég **a szám négyzetgyökéig** vizsgálni: ha `n = a · b`, akkor a két tényező közül az
   egyik biztosan kisebb-egyenlő a gyöknél. Ezért kell a `math` modul.
3. A ciklus **3-tól, kettesével** lép (`range(3, gyök + 1, 2)`), mert a páros osztókat már
   kizártuk.

A `return False` a cikluson belül **azonnal kilép**: felesleges tovább keresni, ha már
találtunk osztót. Ez az **eldöntés tétele** (lásd *07_Programozasi_tetelek*).

## 3. A két megoldás összevetése

| | „favágó" | optimalizált |
| --- | --- | --- |
| vizsgált osztók száma | kb. `n` | kb. `√n / 2` |
| `n = 1 000 003` esetén | ~1 000 000 osztás | ~500 osztás |
| olvashatóság | egyszerűbb | trükkösebb |

## 4. Használat

```python
if prime(n):
    print("A szám prím!")
else:
    print("A szám nem prím!")
```

A `bool`-t visszaadó függvényt közvetlenül tesszük az `if` feltételébe — nem kell
`if prime(n) == True:` alakban írni.

## 5. Feladatok

1. Írasd ki az 1–100 közötti prímeket az **optimalizált** függvénnyel is, és hasonlítsd
   össze az eredményt.
2. Mit ad a `prime(2)`? Kövesd végig a kódot — jó az eredmény?
3. Számold meg, hány prím van 1 és 1000 között.
4. Írj függvényt, ami egy szám **összes osztóját** listába gyűjti.
