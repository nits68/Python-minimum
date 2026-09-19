# Kivételek kezelése — tanulói segédlet

Futtatás:

```bash
python main.py
```

## 1. Miért kell kivételkezelés?

A program futásakor bizonyos utasítások esetén **hibák** léphetnek fel, amiket a megfelelő
szerkezettel kézben tarthatunk. Tipikus esetek:

- állománykezelés közbeni problémák (nincs meg a fájl, nincs jogosultság),
- **nullával osztás**,
- **hibás konverzió** (a felhasználó számsor helyett betűt gépel),
- lista **helytelen indexelése**.

Kivételkezelés nélkül a program ilyenkor **hibaüzenettel leáll**.

## 2. A `try-except` szerkezet

- A **`try`** blokkba kerülnek a „kritikus" utasítások.
- Ha ott hiba lép fel, a végrehajtás azonnal az **`except`** blokkra ugrik — ott
  kezelhetjük, jelezhetjük a hibát.

```python
try:
    szamlalo: int = int(input('Kérem a számlálót: '))
    nevezo: int = int(input('Kérem a nevezőt: '))
    tort: float = szamlalo / nevezo
    print(f'{szamlalo}/{nevezo} = {tort}')
except Exception as ex:
    print(f'A hibaobjektum típusa: {type(ex)}')
    print(f'Hiba szövege: {ex}')
```

Az `Exception` az osztályhierarchia tetején áll, ezért **minden** hibaobjektumot „elkap".
Az `as ex` révén hozzáférünk magához a **hibaobjektumhoz**: kiírhatjuk a típusát
(`type(ex)`) és az üzenetét (`ex`).

Fontos: ha a hiba a `try` blokk közepén lép fel, a **blokk hátralévő utasításai nem
futnak le**.

## 3. Több `except` blokk

Ha a hiba típusától függően **más-más** kezelést szeretnénk:

```python
try:
    ...
except ValueError as ex:            # konverziós hiba (pl. int('alma'))
    print('Konverziós hiba!')
except ZeroDivisionError as ex:     # nullával osztás
    print('Nullával osztani csak Chuck Norris tud!')
except Exception as ex:             # minden MÁS hiba
    print(f'Hiba szövege: {ex}')
```

**Szabály:** a felsorolás sorrendje kötött, ha ős–leszármazott viszony áll fenn.
**A hierarchia alján lévő leszármazottakkal kell kezdeni**, és az ősök jönnek utána — az
első illeszkedő `except` fut le, így ha az `Exception` állna elöl, a többi soha nem
jutna szóhoz.

## 4. Saját kivétel dobása: `raise`

Nem csak a Python dobhat hibát — mi is jelezhetjük, hogy egy érték érvénytelen:

```python
def Tort(szamlalo: float, nevezo: float) -> float:
    if nevezo == 0:
        raise ValueError('A nevező nem lehet nulla!')
    return szamlalo / nevezo
```

A `raise` utasítás **létrehoz és „eldob"** egy hibaobjektumot; a függvény végrehajtása
azonnal befejeződik. A hívó oldalon ezt ugyanúgy `try-except`-tel kapjuk el:

```python
try:
    print(f'{szamlalo}/{nevezo} = {Tort(szamlalo, nevezo)}')
except Exception as ex:
    print(f'Hiba szövege: {ex}')
```

Ez azért hasznos, mert a **függvény** felismeri a hibát, de a **hívó** dönti el, mit
kezdjen vele (kiír, újra bekér, naplóz).

## 5. A Python beépített hibaosztályai

A hibák (kivételek) **osztályhierarchiát** alkotnak. A legfontosabb ág:

```
BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- Exception              <- gyakorlatilag minden "kezelendő" hiba őse
      +-- ArithmeticError
      |    +-- ZeroDivisionError       nullával osztás
      +-- LookupError
      |    +-- IndexError              nem létező listaindex
      |    +-- KeyError                nem létező szótárkulcs
      +-- NameError                    nem létező azonosító
      |    +-- UnboundLocalError
      +-- OSError
      |    +-- FileNotFoundError       nincs meg az állomány
      |    +-- PermissionError         nincs jogosultság
      +-- ImportError
      |    +-- ModuleNotFoundError     nincs ilyen modul
      +-- RuntimeError
      |    +-- RecursionError          túl mély rekurzió
      +-- SyntaxError
      |    +-- IndentationError        rossz behúzás
      +-- TypeError                    rossz típusú művelet
      +-- ValueError                   jó típus, rossz érték (pl. int('alma'))
           +-- UnicodeError
```

A hierarchia ismerete azért fontos, mert az `except ArithmeticError` **elkapja** a
`ZeroDivisionError`-t is — minden leszármazottat elkap.

## 6. Mikor használjunk kivételkezelést, és mikor `if`-et?

| Helyzet | Megoldás |
| --- | --- |
| előre ellenőrizhető feltétel (pl. `nevezo != 0`) | **`if`** — egyszerűbb, olvashatóbb |
| előre nem ellenőrizhető (fájl, felhasználói bemenet, hálózat) | **`try-except`** |

Ne használd a `try-except`-et az `if` helyettesítésére — és főleg ne „nyeld el" a hibát
üres `except` blokkal, mert akkor a program hibásan fut tovább.

## 7. Feladatok

1. Írj programot, ami addig kéri be a számot, amíg érvényes egészet nem kap
   (`try-except` + `while`).
2. Próbáld ki: mi történik, ha egy 5 elemű lista 10. elemére hivatkozol? Kapd el a hibát!
3. Egészítsd ki a `Tort()` függvényt úgy, hogy negatív nevezőnél is saját hibát dobjon.
4. Melyik hibaosztály keletkezik `int('alma')`, `10/0`, `lista[99]`, `szotar['nincs']`
   esetén?
