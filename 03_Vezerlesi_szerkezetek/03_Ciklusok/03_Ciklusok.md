# Ciklusok (iterációk) — tanulói segédlet

Futtatás:

```bash
python main.py
```

Áttekintés: <https://www.w3schools.com/python/python_for_loops.asp> és
<https://www.w3schools.com/python/python_while_loops.asp>

## 1. Mi a ciklus?

Az **iteráció (ciklus)** olyan vezérlési szerkezet, amit utasítás(ok) **ismétlésére**
használunk.

| Ciklusfajta | Pythonban |
| --- | --- |
| klasszikus növekményes `for` | **nincs** (a `range`-dzsel helyettesítjük) |
| `for-in` ciklus | **van** — a C# `foreach`-éhez hasonlít |
| elöltesztelő ciklus (`while`) | **van** |
| hátultesztelő ciklus (`do-while`) | **nincs** |

## 2. A `for-in` ciklus `range`-dzsel

A klasszikus növekményes ciklust a `range` számsorozattal valósítjuk meg:

```python
for i in range(8):        # 0 1 2 3 4 5 6 7
for i in range(-5, 5):    # -5 -4 -3 -2 -1 0 1 2 3 4
for i in range(1, 11, 2): # 1 3 5 7 9
```

A `range` három alakja: `range(vég)`, `range(kezdő, vég)`, `range(kezdő, vég, lépésköz)` —
a **végérték soha nem része** a sorozatnak.

## 3. Lista bejárása

Egy lista elemeit **index** alapján érjük el (`t[0]`, `t[1]`, …). Az indexelés **0-tól**
indul, a hosszt a `len()` adja meg:

```python
t: list[str] = ['alma', 'körte', 'szilva']
for i in range(len(t)):
    print(f't[{i}]={t[i]}', end=' ')
```

Ha az **indexre nincs szükség**, csak az elemekre, akkor egyszerűbb közvetlenül bejárni:

```python
for e in t:
    print(e)
```

**Elnevezési szabály:** az `i`, `j`, `k` neveket **csak tömbindexre** használjuk — ha a
ciklusváltozó magát az elemet tárolja, a neve legyen `e` (vagy egy beszédes név, pl.
`gyümölcs`).

## 4. A `while` (elöltesztelő) ciklus

A feltételt a ciklusmag **előtt** vizsgálja: ha a feltétel már az elején hamis, a mag
egyszer sem fut le.

```python
i: int = 1
while i < 6:
    print(i, end=' ')
    i += 1
```

Három dologra kell figyelni:

1. a ciklusváltozó **kezdőértéket** kap a ciklus előtt,
2. a **feltétel**,
3. a ciklusmagban a ciklusváltozó **változik** — e nélkül végtelen ciklust kapnánk.

## 5. A `break` utasítás

A `break`-kel **kilépünk a ciklusból**: befejezzük az ismétlést a ciklusfeltétel újbóli
vizsgálata nélkül.

```python
i: int = 1
while i < 6:
    print(i, end=' ')  # 1 2 3
    if i == 3:
        break
    i += 1
```

## 6. A `continue` utasítás

A `continue` a ciklusmag **aktuális** végrehajtását fejezi be, és a **feltétel vizsgálatával**
folytatja — vagyis „kihagy" egy kört.

```python
i: int = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i, end=' ')  # 1 2 4 5 6
```

Páros számok kiírása ugyanezzel a technikával:

```python
i: int = 1
while i < 10:
    i += 1
    if i % 2 == 1:
        continue
    print(i, end=' ')  # 2 4 6 8 10
```

**Vigyázz:** ha a `continue` *előtt* nem növeled a ciklusváltozót, a program megáll (végtelen
ciklusba kerül).

## 7. Végtelen ciklus: `while True` + `break`

A végtelen ciklus feltétele sosem lesz hamis, ezért **belülről**, egy vezérlő utasítással
(jellemzően `break`-kel, feltételhez kötve) kell kiléptetni — különben a program „lefagy".

```python
i = 0
while True:
    i += 1
    print(i, end=' ')  # 1 2 3 4 5
    if i == 5:         # e nélkül a ciklus sosem érne véget
        break
```

Tipikus felhasználása: addig ismétlünk, amíg a felhasználó be nem gépel egy megállító
értéket (**végjelet**).

## 8. Nyomkövetés (debug) — így nézz bele a ciklusba

1. Helyezz el **töréspontot (breakpoint)** a sor száma melletti kattintással.
2. Indítsd a nyomkövetést: **F5**.
3. Az első töréspontnál a program megáll.
4. Itt megvizsgálhatod a **változók értékét**, és lépésenként követheted az algoritmust:
   **F10** (step over — átlép a függvényhívás fölött), **F11** (step into — belép a
   függvénybe).
5. Végül: folytatás **F5**, leállítás **Shift+F5**.

Ciklusoknál ez a leghasznosabb eszköz: látod, hogyan változik a ciklusváltozó körönként.

## 9. Feladatok

1. Írasd ki 1-től 100-ig a 7-tel osztható számokat (előbb `range` lépésközzel, aztán
   `continue`-val).
2. Számold ki 1-től `n`-ig a számok összegét `while` ciklussal.
3. Kérj be számokat addig, amíg a felhasználó 0-t nem ír (végjel), és írd ki a darabszámukat.
