# Karakterláncok (string) — tanulói segédlet

Futtatás:

```bash
python main.py
```

## 1. A string mint karakterlista

Pythonban **nincs külön karakter típus**: egy karakter is `str` típusú, egy hosszúságú
szöveg. A string **indexelhető**, ugyanúgy, mint a lista:

```python
a: str = 'Hello, World!'
a[1]        # 'e'
type(a[1])  # <class 'str'>
a[1:5]      # 'ello'
a[-6:-3]    # 'Wor'
a[7:]       # 'World!'
len(a)      # 13 — szóközökkel és írásjelekkel együtt
```

A szeletelés (slicing) szabályai megegyeznek a listáéval: a **végindex nem tartozik bele**,
a negatív index hátulról számol.

**Fontos:** a string **nem módosítható** (immutable) — `a[0] = 'h'` hibát ad. Minden
„módosító" metódus valójában **új** stringet ad vissza.

## 2. Darabolás: `split()`

Szintaxis: `string.split(elválasztó, maxsplit)` — a visszatérési érték **lista**.

```python
a.split()        # ['Hello,', 'World!'] — alapértelmezetten a szóköznél darabol
a.split('o')     # ['Hell', ', W', 'rld!']
a.split(', ')    # ['Hello', 'World!'] — több karakter is lehet elválasztó
```

Az elválasztó **nem kerül bele** az eredménylistába.

## 3. Összeállítás f-stringgel

```python
b: str = f'{a[:5]} Python! {math.pi:.2f}'
```

A `{math.pi:.2f}` **formátummegadás**: írd ki 2 tizedesjegyre kerekítve (`3.14`).

## 4. Tartalmazásvizsgálat, összefűzés, ismétlés

```python
'World' in a          # True
'world' not in a      # True — a vizsgálat KIS- ÉS NAGYBETŰ-ÉRZÉKENY!

'ab' + 'cd'           # 'abcd'   — összefűzés
'ab' * 3              # 'ababab' — ismétlés (replikáció)
'-' * 20              # elválasztó vonal készítésének gyakori módja
```

## 5. Konverzió és bejárás

```python
list('alma')          # ['a', 'l', 'm', 'a']

for e in a:           # karakterenkénti bejárás
    print(e, end=' ')
```

## 6. Karakterkódok: `ord()` és `chr()`

Egymás **inverzei**:

| Hívás | Eredmény | Hívás | Eredmény |
| --- | --- | --- | --- |
| `ord('A')` | 65 | `chr(65)` | `'A'` |
| `ord('a')` | 97 | `chr(97)` | `'a'` |
| `ord('0')` | 48 | `chr(48)` | `'0'` |
| `ord('ő')` | 337 | `chr(337)` | `'ő'` |

Figyeld meg: a nagy- és kisbetűk kódja között pontosan **32** a különbség.

## 7. Fontosabb string metódusok

### Kis- és nagybetűk

| Metódus | Példa | Eredmény |
| --- | --- | --- |
| `title()` | `'python object'.title()` | `'Python Object'` — minden szó nagy kezdőbetűvel |
| `capitalize()` | `'python object'.capitalize()` | `'Python object'` — csak az első betű |
| `swapcase()` | `'Python'.swapcase()` | `'pYTHON'` — felcseréli a kis- és nagybetűket |
| `lower()` | `'ÁRVÍZTŰRŐ'.lower()` | `'árvíztűrő'` |
| `upper()` | `'árvíztűrő'.upper()` | `'ÁRVÍZTŰRŐ'` |

### Levágás (trim)

| Metódus | Mit vág le? |
| --- | --- |
| `strip()` | a whitespace karaktereket a string **elejéről és végéről** |
| `lstrip()` | csak az **elejéről** |
| `rstrip()` | csak a **végéről** |

Whitespace karakter: szóköz, tabulátor (`\t`), soremelés (`\n`), kocsivissza (`\r`).

### Keresés és csere

| Metódus | Példa | Eredmény |
| --- | --- | --- |
| `replace(mit, mire)` | `a.replace("o", "@")` | `'Hell@, W@rld!'` — **minden** előfordulást cserél |
| `count(mit)` | `a.count('l')` | `3` |
| `find(mit)` | `'korcsoportotokhoz'.find('to')` | `9` — az **első** előfordulás indexe |
| `rfind(mit)` | `'korcsoportotokhoz'.rfind('to')` | `11` — az **utolsó** előfordulás indexe |
| `find('x')` | nem található | **`-1`** |

Létezik `index()` és `rindex()` is — ezek ugyanezt csinálják, de ha nincs találat,
**hibát dobnak** `-1` helyett.

### Vizsgáló metódusok (`bool` értéket adnak)

| Metódus | Mit vizsgál? |
| --- | --- |
| `isalnum()` | csupa betű vagy számjegy? |
| `isalpha()` | csupa betű? |
| `isdigit()` / `isdecimal()` / `isnumeric()` | csupa számjegy? |
| `islower()` / `isupper()` | csupa kisbetű / nagybetű? |
| `isspace()` | csupa whitespace? |
| `istitle()` | minden szó nagy kezdőbetűvel kezdődik? |
| `startswith(x)` / `endswith(x)` | ezzel kezdődik / végződik? |

### Egyéb

```python
'*, '.join(['4', '8', '78'])    # '4*, 8*, 78' — lista összefűzése elválasztóval
'körte'.center(12, '*')         # '***körte****' — középre igazítás kitöltő karakterrel
'szöveg'.splitlines()           # sortörések mentén darabol listába
```

A `join()` szintaxisa fordított, mint várnánk: **az elválasztó string** metódusa, és a
kollekció a paramétere.

## 8. Feladatok

1. Kérj be egy nevet, és írd ki nagybetűsen, illetve megfordítva (`[::-1]`).
2. Számold meg egy bekért mondatban a szavakat (`split()`) és a magánhangzókat.
3. Döntsd el egy szóról, hogy palindrom-e (visszafelé olvasva ugyanaz).
4. Írj programot, ami egy mondat minden szavát nagy kezdőbetűssé alakítja — `title()`
   nélkül!
