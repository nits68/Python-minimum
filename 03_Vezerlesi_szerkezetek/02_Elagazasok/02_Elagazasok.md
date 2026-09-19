# Elágazások (szelekciók) — tanulói segédlet

Futtatás:

```bash
python main.py
```

## 1. Mi az elágazás?

A **szelekció (elágazás)** olyan vezérlési szerkezet, amelyben **feltételhez kötjük** az
utasítások végrehajtását.

Fajtái:

| Fajta | Szerkezet |
| --- | --- |
| egyágú | `if` |
| kétágú | `if` – `else` |
| többágú | `if` – `elif` – … – `elif` – `else` |
| mintaillesztés | `match` – `case` (a **Python 3.10** verziótól) |

> A más nyelvekből ismert `switch-case` szerkezetnek a **`match-case`** felel meg. Ez
> hosszú ideig valóban hiányzott a nyelvből: a **Python 3.10** (2021) vezette be
> *strukturált mintaillesztés* néven. Régebbi Python verzióval `SyntaxError`-t kapsz,
> ezért a vizsgakövetelményekben többnyire ma is az `if-elif-else` lánc szerepel.

**Fontos:** a feltétel után **kettőspont** áll, a hozzá tartozó blokkot pedig **behúzás
(indentálás)** jelöli ki — Pythonban a behúzás nem szépészeti kérdés, hanem a nyelv része!

## 2. Egyágú elágazás (`if`)

Csak akkor csinálunk valamit, ha a feltétel igaz. Példa: abszolút érték.

```python
absX: int = inputX
if inputX < 0:
    absX = inputX * -1   # előjelváltás
print(f"Abs({inputX}) = {absX}")
```

Figyeld meg a trükköt: előbb **feltételezzük**, hogy az eredmény maga a szám, és csak negatív
esetben javítunk rajta.

## 3. Kétágú elágazás (`if-else`)

Két egymást kizáró eset. Példa: páros-páratlan eldöntése a maradékos osztással.

```python
if inputSzám % 2 == 0:
    print("A szám páros!")
else:
    print("A szám páratlan!")
```

## 4. Többágú elágazás (`if-elif-else`)

Kettőnél több eset. A feltételek **sorban** értékelődnek ki, és az **első igaz** ág fut le —
a többit a program már meg sem nézi.

```python
if érdemjegy == 1:
    print("Elégtelen")
elif érdemjegy == 2:
    print("Elégséges")
elif érdemjegy == 3:
    print("Közepes")
elif érdemjegy == 4:
    print("Jó")
elif érdemjegy == 5:
    print("Jeles")
else:                      # az else ág opcionális, elhagyható
    print("Ez nem osztályzat!")
```

Az `else` ág a „minden más eset" — érdemes megtartani a hibás bemenet kezelésére.

## 5. Mintaillesztés: `match-case` (Python 3.10-től)

Ugyanaz a feladat, `if-elif-else` helyett mintaillesztéssel:

```python
match érdemjegy2:
    case 1:
        print("Elégtelen")
    case 2:
        print("Elégséges")
    case 3:
        print("Közepes")
    case 4:
        print("Jó")
    case 5:
        print("Jeles")
    case _:                      # a "minden más eset" mintája
        print("Ez nem osztályzat!")
```

Működése: a `match` után álló kifejezés értékét hasonlítjuk össze a `case` ágak
**mintáival**, és az **első illeszkedő** ág utasításai hajtódnak végre.

Amit érdemes megjegyezni:

- Az aláhúzás (`_`) a **„minden más eset"** mintája — az `if-elif-else` `else` ágának
  felel meg. Elhagyható, ekkor illeszkedés hiányában nem történik semmi.
- **Nincs szükség `break` utasításra** — a C-szerű nyelvekkel ellentétben a végrehajtás
  nem „csúszik át" a következő ágra.
- Egy ágban **több minta** is felsorolható a `|` (vagy) jellel:

```python
match érdemjegy2:
    case 1 | 2:
        print("Gyenge eredmény")
    case 3 | 4:
        print("Közepes eredmény")
    case 5:
        print("Kiváló eredmény")
    case _:
        print("Ez nem osztályzat!")
```

Mikor melyiket? A `match-case` akkor olvashatóbb, ha **egyetlen változó konkrét
értékeit** soroljuk fel. Ha a feltételek összetettebbek (tartományok, több változó,
logikai kifejezések), maradj az `if-elif-else` láncnál.

> A `match-case` ennél sokkal többet tud (listák, szótárak, objektumok szerkezetének
> illesztése) — ezt a részét most nem érintjük.

## 6. Rövidített (shorthand) elágazás

Ha az elágazás **egyetlen értékadás** két lehetséges értékkel, egy sorban is írható. Ez a
feltételes operátor szerepét tölti be:

```python
ki = 'A' if a > b else 'B'
c: int = 12 if a != b else 24
```

Olvasd így: *„legyen `'A'`, ha `a > b`, egyébként `'B'`"*.

> C#-ban vagy JavaScriptben ugyanez: `c = a != b ? 12 : 24;`

## 7. Véletlen számok: a `random` modul

A példában véletlen értékekkel dolgozunk. A modult használat **előtt importálni kell**, a
fájl legelején:

```python
import random

a: int = random.randint(10, 20)   # véletlen egész 10 és 20 KÖZÖTT, mindkettőt beleértve
```

## 8. A `pass` utasítás

Pythonban egy blokk **nem maradhat üres**. Ha egy ág törzsét csak később írnád meg, tedd bele
a `pass` utasítást — így elkerülöd a szintaktikai hibát:

```python
if b > a:
    pass
else:
    pass
```

## 9. Gyakori kezdő hibák

- `=` (értékadás) írása `==` (összehasonlítás) helyett a feltételben.
- Lemaradt **kettőspont** az `if` sor végéről.
- Rossz **behúzás** — az utasítás kicsúszik az ágból.
- `elif` helyett több önálló `if` — ilyenkor minden feltétel kiértékelődik.

## 10. Feladatok

1. Írj programot, ami két bekért számról megmondja, melyik a nagyobb (vagy hogy egyenlők).
2. Kérj be egy pontszámot (0–100), és írd ki az osztályzatot `if-elif-else` szerkezettel.
3. Írd át a 2. pont páros-páratlan példáját rövidített elágazással.
4. Írj programot, ami egy bekért hónapszámhoz (1–12) kiírja a hónap nevét — előbb
   `if-elif-else`, majd `match-case` szerkezettel.
5. Írd ki `match-case`-szel, hogy a bekért hónap melyik évszakhoz tartozik (`|` jellel
   több mintát is felsorolva egy ágban).
