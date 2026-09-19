# Másodfokú egyenlet gyökei (MFEGY) — tanulói segédlet

Futtatás:

```bash
python main.py
```

Ez a feladat az **egymásba ágyazott elágazások** iskolapéldája: a megoldás a
`MFEGY_feladat.pdf` folyamatábráját követi.

## 1. A feladat

Az `a·x² + b·x + c = 0` egyenlet gyökeit keressük a bekért `a`, `b`, `c` együtthatókból.

## 2. A `math` modul

A gyökvonáshoz és a hatványozáshoz a `math` modult használjuk, amit importálni kell:

```python
import math

math.pow(b, 2)  # b a négyzeten  (ugyanaz, mint b ** 2)
math.sqrt(x)    # x négyzetgyöke
```

## 3. A döntési fa

A **diszkrimináns**: `D = b² − 4·a·c`. A program ennek alapján dönt:

```
a != 0 ?
├── igen: valódi másodfokú egyenlet
│   ├── D > 0  -> két valós gyök
│   ├── D == 0 -> egy (kétszeres) valós gyök
│   └── D < 0  -> nincs valós gyök
└── nem: nem másodfokú
    ├── b != 0 -> elsőfokú egyenlet, egy gyök
    └── b == 0
        ├── c != 0 -> ellentmondás (nincs megoldás)
        └── c == 0 -> azonosság (minden szám megoldás)
```

A kódban ez **egymásba ágyazott `if`-ekként** jelenik meg. Figyeld meg a behúzás
szintjeit: minden beljebb lépés egy újabb döntést jelent.

## 4. A gyökképlet

```python
x1 = (-b + math.sqrt(math.pow(b, 2) - 4 * a * c)) / (2 * a)
x2 = (-b - math.sqrt(math.pow(b, 2) - 4 * a * c)) / (2 * a)
```

Ha `D == 0`, a gyökvonás eredménye 0, így elég a rövidebb alak:

```python
x = -b / (2 * a)
```

A **zárójelezés** itt kritikus: a nevezőben álló `2 * a` köré kötelező a zárójel, különben
csak 2-vel osztanánk, majd megszoroznánk `a`-val.

## 5. Miért csak akkor vonunk gyököt, ha `D >= 0`?

Negatív számból a `math.sqrt()` **hibát dob** (`ValueError`). Ezért a program **előbb
megvizsgálja** a diszkriminánst, és csak utána számol. Ez általános szabály: a veszélyes
műveletet mindig előzze meg az ellenőrzés.

> A hibák másik kezelési módját lásd: *08_Kivetelek_kezelese*.

## 6. Az elsőfokú eset

Ha `a = 0`, az egyenlet valójában elsőfokú: `b·x + c = 0`. Ezt `b`-vel átrendezve:

```python
x: float = -c / b
```

Ellenőrizd az `a=0, b=2, c=-6` bemenettel — a helyes eredmény `3.0`.

Ha `b` is 0, akkor már `c = 0` alakú „egyenletünk" maradt:

- `c != 0` → **ellentmondás** (pl. `5 = 0`), nincs megoldás,
- `c == 0` → **azonosság** (`0 = 0`), minden szám megoldás.

## 7. Feladatok

1. Próbáld ki mind a hat ágat: adj meg olyan együtthatókat, amik eljuttatnak mindegyikhez.
2. Rövidítsd a kódot úgy, hogy a diszkriminánst **egyszer** számold ki egy `d` változóba.
3. Írd ki két gyök esetén a gyökök összegét és szorzatát is (Viète-formulák ellenőrzése).
