# Szótárak (dict) — tanulói segédlet

Futtatás:

```bash
python main.py
```

## 1. Mi a szótár?

A **szótár (dict)** **kulcs–érték párokat** tároló kollekció. Az elemeket nem sorszámmal,
hanem **kulccsal** érjük el. A kulcs **egyedi** — egy kulcs csak egyszer szerepelhet.

Tipikus használat: névhez telefonszám, országhoz adat, terméknévhez ár.

## 2. Szótár létrehozása

```python
szotar1 = {                        # elemekkel inicializált szótár
    "brand": "Ford",
    "veteran": True,
    "year": 1964,
}

szotar2: dict[str, int] = {"Magyarország": 12, "Ausztria": 34, "Anglia": 23}  # típusos
szotar3 = dict([("x", 5), ("y", -5)])   # a dict() konstruktorral
szotar4: dict[int, int] = {}            # üres típusos szótár
szotar5 = dict({})                      # üres szótár konstruktorral
```

A `dict[str, int]` jelölés azt mondja meg: a kulcs `str`, az érték `int` típusú.

**Figyelem:** a `dict[int, int]` önmagában (zárójel nélkül) csak **típusjelölés**, nem hoz
létre szótárat! Az üres szótár: `{}` vagy `dict({})`.

## 3. Hivatkozás az elemekre

A kulcs olyan, mint egy index:

```python
print(szotar1["brand"])      # 'Ford'
szotar1["year"] = 1968       # meglévő érték módosítása
print(szotar1.get("year"))   # 1968 — a get() metódussal is lekérdezhető
```

Különbség: ha a kulcs **nem létezik**, a `szotar1["nincs"]` **hibát dob** (`KeyError`), a
`szotar1.get("nincs")` viszont `None`-t ad vissza.

## 4. Bejárás

```python
for key, value in szotar2.items():        # kulcs–érték párok együtt
    print(f"Kulcs: {key} Érték: {value}")

for e in szotar2.values():                # csak az értékek
    print(f"Érték: {e}")
```

Létezik a `.keys()` is, ami csak a kulcsokat adja. (A `for e in szotar2:` szintén a
kulcsokon megy végig.)

## 5. További műveletek

| Művelet | Mit csinál? |
| --- | --- |
| `"Anglia" in szotar2` | szerepel-e a megadott **kulcs** a szótárban |
| `len(szotar2)` | a kulcs–érték párok száma |
| `szotar2["Szlovénia"] = 34` | **új** elem hozzáadása (ha a kulcs nincs még benne) |
| `szotar2.pop("Ausztria")` | a megadott kulcsú elem törlése |
| `szotar2.clear()` | a szótár kiürítése (`{}`) |
| `del szotar2` | magának a változónak a megszüntetése |

Jegyezd meg: **ugyanaz az értékadás** ad hozzá új elemet, illetve módosít meglévőt — a
kulcs megléte dönti el, melyik történik.

## 6. Másolás — itt is vigyázz!

```python
szotar6 = szotar1          # NEM másolat: ugyanarra a memóriacímre mutatnak!
szotar6 = szotar1.copy()   # valódi másolat
szotar7 = dict(szotar1)    # másolat a konstruktorral
```

## 7. Szótár azonos alapértelmezett értékekkel

```python
myTuple = ("kulcs1", "kulcs2", "kulcs3")
thisdict = dict.fromkeys(myTuple, 0)
print(thisdict)   # {'kulcs1': 0, 'kulcs2': 0, 'kulcs3': 0}
```

Hasznos például **számlálásnál**: minden kulcs 0-ról indul.

## 8. Mikor használj szótárat?

| Kérdés | Adatszerkezet |
| --- | --- |
| „hányadik elem?" | lista |
| „szerepel-e benne?" | halmaz |
| „mi tartozik ehhez a névhez / kulcshoz?" | **szótár** |

## 9. Feladatok

1. Készíts szótárat 5 tanuló nevével és osztályzatával, majd írd ki az átlagot.
2. Írd ki annak a tanulónak a nevét, akinek a legjobb a jegye.
3. Számold meg egy szövegben az egyes betűk előfordulását szótárral.
4. Mi a különbség a `szotar["x"]` és a `szotar.get("x")` között nem létező kulcs esetén?
