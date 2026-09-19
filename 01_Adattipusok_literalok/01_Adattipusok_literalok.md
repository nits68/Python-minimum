# Adattípusok és literálok — tanulói segédlet

Futtatás:

```bash
python main.py
```

## 1. Alapfogalmak

| Fogalom | Jelentése |
| --- | --- |
| **program** | algoritmus + adatszerkezet |
| **algoritmus** | az utasítások végrehajtásának sorrendje (ezt a vezérlési szerkezetek határozzák meg) |
| **változó** | adat tárolására szolgáló egység |
| **adatszerkezet** | a programban használt változók halmaza |
| **literál** | olyan adat, amihez nem rendelünk azonosítót; a leírás módja dönti el a típusát |

A változó négy jellemzője:

1. **azonosító** (a változó neve),
2. **adattípus** (`str`, `int`, `float`, `bool` stb. — Pythonban a kiírása *opcionális*),
3. **kezdőérték**,
4. **aktuális érték**.

Az **adattípus** azt határozza meg, hogy a változóban hány és milyen típusú érték tárolható,
és mekkora az értéktartománya.

## 2. Egyszerű adattípusok — egy érték tárolására

### 2.1 Szöveg: `str`

```python
szoveg: str = 'Python'
szoveg2: str = "Jedlik"
print(szoveg + ' ' + szoveg2)
print(type(szoveg))
```

A szöveges literált **aposztróf** (`'...'`) vagy **idézőjel** (`"..."`) közé tesszük — a kettő
egyenértékű, csak legyünk következetesek. A `+` szövegek között **összefűzést** jelent.

A `type()` beépített függvény megmondja egy változó típusát.

### 2.2 Számok: `int` és `float`

```python
egesz: int = 68     # egész érték
valos: float = 3.14 # valós (tizedes) érték
```

A valós literálban a tizedesjel **pont**, nem vessző!

### 2.3 Logikai érték: `bool`

```python
logikai: bool = True   # értéke csak True vagy False lehet
```

Figyelj a **nagy kezdőbetűre**: `True` és `False` (nem `true`/`false`).

## 3. Összetett adattípusok (kollekciók) — több érték tárolására

| Típus | Literál | Jellemzője |
| --- | --- | --- |
| `list` | `['apple', 'banana', 'cherry']` | szögletes zárójel; sorrendtartó, **módosítható** (más nyelveken: tömb, vektor) |
| `tuple` | `('apple', 'banana', 'cherry')` | kerek zárójel; **konstans listának** tekinthető, nem módosítható |
| `set` | `{'apple', 'banana', 'cherry'}` | kapcsos zárójel; **nem lehet benne két azonos érték** |
| `dict` | `{"alma": 20, "körte": 23}` | kapcsos zárójel, **kulcs: érték** párok, a kulcs egyedi |

```python
lista: list[str] = ['apple', 'banana', 'cherry']
konstans_lista: tuple[str, str, str] = ('apple', 'banana', 'cherry')
halmaz: set[str] = {'apple', 'banana', 'cherry'}
szotar: dict[str, int] = {"alma": 20, "körte": 23, "barack": 33}
```

A szögletes zárójelben álló `list[str]`, `dict[str, int]` azt is elárulja, **milyen típusú
elemeket** tárol a kollekció.

> Ezekkel részletesen a *05_Kollekciok* fejezetben foglalkozunk.

## 4. Számsorozat: `range`

A `range` számok sorozatát állítja elő — leggyakrabban `for` ciklushoz használjuk.
Három alakja van:

```python
range(6)        # 0 1 2 3 4 5        -> 0-tól a megadott szám ELŐTTIG
range(2, 8)     # 2 3 4 5 6 7        -> kezdőérték, végérték (ez már nem tartozik bele)
range(2, 15, 3) # 2 5 8 11 14        -> kezdőérték, végérték, lépésköz
```

Fontos: a **végérték soha nem része** a sorozatnak.

A `print(sor1)` nem a számokat írja ki, hanem magát a `range(0, 6)` objektumot — a számokat
végig kell járni egy ciklussal:

```python
for i in sor1:
    print(i, end=' ')
```

A `print` `end=' '` paramétere azt mondja meg, mit írjon a kiírás *végére* soremelés helyett —
így egy sorba kerülnek a számok. Az üres `print()` zárja le a sort.

## 5. A programváz

```python
def main() -> None:
    ...


if __name__ == "__main__":
    main()
```

A kódot egy `main` nevű **függvénybe** tesszük, az utolsó két sor pedig elindítja.
Ez a szerkezet minden példaprogramunkban vissza fog térni.

## 6. Ellenőrző kérdések

1. Mi a különbség a változó és a literál között?
2. Melyik kollekcióban nem lehet két azonos érték?
3. Mit ír ki a `range(1, 10, 4)` bejárása?
4. Milyen típusú lesz a `3.0` literál?
