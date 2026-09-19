# Operátorok — tanulói segédlet

Futtatás:

```bash
python main.py
```

Áttekintés: <https://www.w3schools.com/python/python_operators.asp>

## 1. Aritmetikai operátorok

```python
a: int = 17
b: int = 5
```

| Operátor | Jelentés | `17` és `5` esetén |
| --- | --- | --- |
| `+` | összeadás | `22` |
| `-` | kivonás | `12` |
| `*` | szorzás | `85` |
| `/` | osztás — az eredmény **mindig `float`** | `3.4` |
| `//` | egészosztás (maradék nélkül, lefelé kerekít) | `3` |
| `%` | osztási maradék (modulo) | `2` |
| `**` | hatványozás | `1419857` |

Vigyázz: a `/` akkor is `float`-ot ad, ha maradék nélkül osztható (`10 / 5` → `2.0`).

**Negatív számoknál** az egészosztás és a modulo mindig **lefelé** kerekít:

```python
-17 // 5  # -4, nem -3!
-17 % 5   #  3, nem -2!
```

## 2. Rövidített (összetett) értékadás

A `változó = változó operátor érték` alak helyett rövidebben is írhatjuk:

```python
c: int = 10
c += 3   # c = c + 3
c -= 4   # c = c - 4
c *= 2   # c = c * 2
c /= 3   # c = c / 3  -> az eredmény float lesz!
c **= 2  # c = c ** 2
d %= 5   # d = d % 5
```

## 3. Relációs (összehasonlító) operátorok

Az eredményük **mindig logikai (`bool`) érték**.

| Operátor | Jelentés |
| --- | --- |
| `==` | egyenlő-e (két egyenlőségjel!) |
| `!=` | nem egyenlő-e |
| `>` | nagyobb |
| `<` | kisebb |
| `>=` | nagyobb vagy egyenlő |
| `<=` | kisebb vagy egyenlő |

A leggyakoribb kezdő hiba az `=` (értékadás) és a `==` (összehasonlítás) összekeverése.

## 4. Logikai operátorok

`and`, `or`, `not` — más nyelvekben (C, Java, JavaScript) ezek a `&&`, `||`, `!`.

| Művelet | Mikor `True`? |
| --- | --- |
| `x and y` | ha **mindkettő** `True` |
| `x or y` | ha **legalább az egyik** `True` |
| `not x` | a logikai érték ellentettje |

Tipikus felhasználás összetett feltételben:

```python
if év % 4 == 0 and (év % 100 != 0 or év % 400 == 0):
    print(f'{év} szökőév!')
else:
    print(f'{év} nem szökőév!')
```

## 5. Bitműveleti operátorok

Ezek a számok **kettes számrendszerbeli** alakján, **bitenként** dolgoznak.
A `0b` előtaggal bináris literált adhatunk meg:

```python
e: int = 0b1010  # 10
f: int = 0b0110  # 6
```

| Operátor | Jelentés | Példa |
| --- | --- | --- |
| `&` | bitenkénti ÉS | `1010 & 0110 = 0010` (2) |
| `\|` | bitenkénti VAGY | `1010 \| 0110 = 1110` (14) |
| `^` | bitenkénti kizáró VAGY (XOR) | `1010 ^ 0110 = 1100` (12) |
| `~` | bitenkénti negálás | `~n` értéke `-(n+1)` |
| `<<` | balra léptetés | egy lépés = szorzás 2-vel |
| `>>` | jobbra léptetés | egy lépés = egészosztás 2-vel |

A kiírásnál használt `{e:04b}` formátum azt jelenti: írd ki `e`-t **kettes
számrendszerben (`b`), 4 jegyen, vezető nullákkal (`04`)**.

Gyakorlati példa — párosság eldöntése a legkisebb helyiértékű bit vizsgálatával:

```python
if szám & 1 == 0:
    print(f'{szám} páros szám!')
```

(Ez ugyanaz, mint a megszokott `szám % 2 == 0` vizsgálat.)

## 6. Tartalmazásvizsgálat: `in` / `not in`

Megmondja, hogy egy elem szerepel-e egy kollekcióban. Az eredmény `bool`:

```python
gyümölcsök: list[str] = ['alma', 'körte', 'szilva']
'alma' in gyümölcsök        # True
'barack' not in gyümölcsök  # True
```

> Bővebben: *05_Kollekciok*, *06_Karakterlancok*.

## 7. Műveleti sorrend (precedencia)

> zárójel → hatványozás → szorzás / osztás / maradékképzés → összeadás / kivonás →
> relációs operátorok → logikai operátorok

```python
2 + 3 * 4    # 14, nem 20 — a szorzás előbb történik
(2 + 3) * 4  # 20 — a zárójel felülírja a sorrendet
```

Ha bizonytalan vagy, **tegyél zárójelet**: olvashatóbb is lesz tőle a kód.

## 8. Ellenőrző kérdések

1. Mi lesz a `7 / 2`, a `7 // 2` és a `7 % 2` eredménye — és milyen típusúak?
2. Miért `-4` a `-17 // 5`?
3. Mi a különbség az `=` és a `==` között?
4. Mikor igaz az `x or y` kifejezés?
5. Mennyi `2 + 3 ** 2 * 2`?
