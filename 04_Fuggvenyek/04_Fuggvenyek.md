# Függvények (alprogramok) — tanulói segédlet

Futtatás:

```bash
python main.py
```

## 1. Mi a függvény?

A **függvény** azonosítóval ellátott, meghatározott feladatot ellátó **utasítások csoportja**.
Használat előtt **definiálni kell**.

Miért használjuk?

- **ismétlődő kód** kiváltása (egyszer írjuk meg, sokszor hívjuk),
- a program **áttekinthető** részekre bontása,
- a részfeladatok **külön tesztelhetők**.

## 2. A függvénydefiníció szerkezete

```python
def összead(a: int, b: int) -> int:   # 1. a függvény FEJE
    return a + b                       # 2. a függvény TÖRZSE
```

A fej elemei:

| Elem | Jelentése |
| --- | --- |
| `def` | a definíciót bevezető foglalt szó |
| `összead` | a függvény **azonosítója** (neve) |
| `( )` | a paraméterek megadására szolgáló zárójelpár |
| `a: int, b: int` | a **formális paraméterek** azonosítóval és típussal (a típus opcionális) |
| `->` | ezután adható meg a visszatérési érték típusa (opcionális) |
| `int` | a **visszatérési érték típusa** |
| `:` | a fejet lezáró kettőspont |

A **törzs** tetszőleges számú utasítás (behúzva!), benne általában egy **`return`**
utasítással — utána áll a visszaadott érték. A `return` végre is hajtja a kilépést a
függvényből.

## 3. A függvény hívása

Szintaxis: `függvény_azonosítója(aktuális paraméterlista)`

```python
összead(3, 4)                 # a visszatérési érték ELVÉSZ
print(összead(3, 4))          # kiírjuk
összeg: int = összead(3, 4)   # eltároljuk egy változóban
```

A **formális** paraméter a definícióban álló név (`a`, `b`); az **aktuális** paraméter a
híváskor átadott érték (`3`, `4`).

## 4. Algoritmus függvénybe zárva

Az LNKO kivonásos algoritmusa (lásd *03_Ciklusok/01_Lnko*) függvényként:

```python
def lnko(a: int, b: int) -> int:
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a
```

Így a `main()`-ben már csak ennyi a dolgunk:

```python
print(f'LNKO({a}, {b}) = {lnko(a, b)}')
```

## 5. Láthatósági kör (scope)

**Egy változó ott és addig érhető el, ahol és ameddig létrejött.**

### 5.1 Helyi (lokális) változó

A függvényen belül létrehozott változó **csak azon a függvényen belül létezik**, és a
függvény befejeződésekor megszűnik:

```python
def keres_nélküle_hibázna() -> None:
    helyi_változó: int = 100
    print(f'helyi_változó a függvényen belül: {helyi_változó}')

# print(helyi_változó)  # Hiba! NameError — kívülről nem érhető el
```

### 5.2 Globális (modulszintű) változó

A függvényeken **kívül** létrehozott változó a teljes állományban elérhető. **Olvasni**
bárhonnan lehet, de ha egy függvényből **módosítani** akarjuk, jelezni kell a `global`
kulcsszóval — különben a Python új, helyi változót hozna létre:

```python
számláló: int = 0          # globális változó

def számol() -> None:
    global számláló        # nem új helyi, hanem a GLOBÁLIS változót módosítjuk
    számláló += 1
```

> Jó szokás: globális változót csak indokolt esetben használj. A függvény inkább
> **paraméterben kapja** az adatot, és `return`-nel adja vissza az eredményt.

## 6. Paraméterátadás módjai

```python
def üdvözlés(név: str, kor: int = 18) -> None:
    print(f'{név} {kor} éves.')
```

| Hívás | Mód |
| --- | --- |
| `üdvözlés('Kovács Anna', 16)` | **pozíció szerint** — a sorrend számít |
| `üdvözlés(név='Nagy Béla', kor=17)` | **kulcsszó szerint** — a név számít |
| `üdvözlés(kor=15, név='Tóth Dóra')` | kulcsszóval a sorrend felcserélhető |
| `üdvözlés('Szabó Elek')` | a `kor` elhagyható: van **alapértelmezett értéke** (18) |

Az alapértelmezett értékkel rendelkező paraméterek a paraméterlista **végén** állnak.

## 7. A `None`

A `None` a „nincs érték" jelentésű speciális érték. Ha egy függvényben **nincs `return`**
(vagy a `return` után nincs érték), a visszatérési értéke automatikusan `None` lesz — ezt
jelzi a fejben a `-> None`.

```python
eredmény = üdvözlés('Teszt Elemér')   # az üdvözlés() nem ad vissza semmit
print(eredmény)                        # None
print(eredmény is None)                # True
```

`None`-nal mindig az **`is`** operátorral hasonlítunk, nem `==`-szel.

## 8. Fontosabb beépített függvények

Ezeket ismerni kell (ágazati alapvizsga-szint):

| Függvény | Mit csinál? |
| --- | --- |
| `abs(x)` | abszolút érték — `abs(-5)` → `5` |
| `len(x)` | az objektum hossza (pl. lista elemszáma) |
| `max(x)` / `min(x)` | legnagyobb / legkisebb elem |
| `sum(x)` | elemek összege |
| `range(...)` | számsorozat előállítása |
| `input(...)` | felhasználói adatbekérés |
| `print(...)` | képernyőre írás |
| `type(x)` | az objektum típusa (osztálya) |
| `id(x)` | az objektum azonosítója |
| `open(...)` | fájl megnyitása / létrehozása |
| `enumerate(x)` | kollekció bejárása index–elem párokkal |
| `chr(n)` | a Unicode-kódhoz tartozó karakter — `chr(65)` → `'A'` |
| `ord(c)` | a karakter Unicode-kódja — `ord('A')` → `65` |

Néhány hasznos kódpont: `ord('A') = 65`, `ord('a') = 97`, `ord('0') = 48`.

**Konstruktor (típuskonvertáló) függvények:** `bool()`, `int()`, `float()`, `str()`,
`list()`, `tuple()`, `set()`, `dict()`.

További, később hasznos beépített függvények: `sorted()`, `reversed()`, `round()`, `pow()`,
`bin()`, `hex()`, `zip()`, `all()`, `any()`, `filter()`, `map()`.

## 9. Feladatok

1. Írj `terület(a, b)` és `kerület(a, b)` függvényt a téglalaphoz, és hívd meg őket.
2. Írj `legnagyobb(a, b, c)` függvényt három szám közül a legnagyobb visszaadására.
3. Egészítsd ki az `üdvözlés()` függvényt egy alapértelmezett `köszönés='Szia'` paraméterrel.
4. Miért kapsz `NameError`-t, ha a `helyi_változó`-t a `main()`-ből írod ki?
