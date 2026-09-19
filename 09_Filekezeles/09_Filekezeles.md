# Fájlkezelés — tanulói segédlet

Futtatás:

```bash
python main.py
```

A mappában lévő adatállományok: `forras.txt`, `szamok.txt` (bemenet), `cél.txt`,
`cél2.txt` (a program hozza létre).

## 1. Az állomány megnyitása: `open()` és `with-as`

```python
with open('forras.txt', 'r', encoding='utf-8') as file:
    sorok = file.read().splitlines()
```

Az `open()` három fontos paramétere:

1. az **állomány neve** (útvonala),
2. a **megnyitás módja**,
3. a **kódolás** — magyar ékezetekhez `encoding='utf-8'`, e nélkül hibás karaktereket
   kapnánk.

A **`with-as`** szerkezet előnye: a blokk végén **automatikusan lezárja** az állományt,
akkor is, ha közben hiba történt. (Enélkül `file.close()`-t kellene hívnunk.)

### A megnyitási módok

| Mód | Jelentése |
| --- | --- |
| `'r'` | **Read** — olvasás (alapértelmezett). **Hibát dob**, ha a fájl nem létezik. |
| `'w'` | **Write** — írás. A létező állományt **felülírja**, ha nincs, **létrehozza**. |
| `'a'` | **Append** — hozzáfűzés a végéhez; ha nincs, létrehozza. |
| `'x'` | **Create** — létrehozás íráshoz; **hibát dob**, ha a fájl már létezik. |

Vigyázz a `'w'` móddal: **szó nélkül törli** a fájl korábbi tartalmát!

## 2. Miért van try-except?

Az állománykezelés tipikus „előre nem látható" hibaforrás (nincs meg a fájl, nincs
jogosultság), ezért a gyakorlatban **erősen javasolt** a kivételkezelés:

```python
try:
    with open('forras.txt', 'r', encoding='utf-8') as file:
        sorok = file.read().splitlines()
except Exception as ex:
    print(f'Hiba: {ex}')
```

(Vizsgafeladatban elhagyható, ha nem kérik — de éles kódban ne hagyd el.)

> Bővebben: *08_Kivetelek_kezelese*.

## 3. Olvasás — három módszer

### 3.1 `read()` + `splitlines()` — a leggyakoribb

```python
sorok: list[str] = file.read().splitlines()
```

Az egész állományt beolvassa egy szövegbe, majd a sortörések mentén **listává** darabolja.
A sorvégi `\n` karakterek **nem** kerülnek bele. Az így kapott listát rendszerint
`for-in` ciklussal járjuk be.

### 3.2 `readlines()` + konverzió — ha számokat olvasunk

```python
számok: list[int] = []
with open('szamok.txt', 'r', encoding='utf-8') as file:
    for e in file.readlines():
        számok.append(int(e.strip()))
```

A fájlból **mindig szöveg** érkezik, ezért konvertálni kell. A `strip()` levágja a sorvégi
`\n` vezérlőkaraktert (és a felesleges szóközöket).

Rövidebben, listaértelmezéssel:

```python
számok = [int(e.strip()) for e in file.readlines()]
```

### 3.3 `readline()` — soronként

Nagyméretű állományokhoz (pl. rendszernaplók) javasolt, mert **nem tölti be** az egész
fájlt a memóriába:

```python
sor: str = 'x'
while sor:
    sor = file.readline()
    if sor != '':
        szamok2.append(int(sor))
```

A `readline()` a fájl végén **üres stringet** ad vissza — ez a ciklus leállási feltétele.

## 4. Írás — két módszer

### 4.1 `write()` — soronként

```python
with open('cél.txt', 'w', encoding='utf-8') as file:
    for e in sorok:
        file.write(f'{e}\n')
```

A `write()` **nem tesz** sortörést a végére — a `\n` vezérlőkaraktert nekünk kell
hozzáfűzni, különben minden egy sorba kerül.

### 4.2 `writelines()` — az egész lista egyben

```python
with open('cél2.txt', 'w', encoding='utf-8') as file:
    ki: list[str] = []
    for e in sorok:
        ki.append(f'{e}\n')
    file.writelines(ki)
```

A `writelines()` sem tesz sortörést: azt **minden sor végéhez** hozzá kell fűzni.

Rövidebben:

```python
file.writelines([f'{e}\n' for e in sorok])
```

## 5. A tipikus munkamenet

```
1. beolvasás  ->  lista
2. feldolgozás (programozási tételek a listán)
3. kiírás     ->  állomány
```

A *07_Programozasi_tetelek* fejezet feltöltési módjai közül a 4. pont pontosan ez.

## 6. Feladatok

1. Olvasd be a `szamok.txt` tartalmát, és írd ki egy új fájlba a **páros** számokat.
2. Fűzz hozzá egy sort a `cél.txt` végéhez az `'a'` (append) móddal.
3. Írd ki a `forras.txt` sorait **fordított sorrendben** egy új állományba.
4. Mi történik, ha a `forras.txt`-t átnevezed, és úgy futtatod a programot? Miért nem áll
   le a program?
