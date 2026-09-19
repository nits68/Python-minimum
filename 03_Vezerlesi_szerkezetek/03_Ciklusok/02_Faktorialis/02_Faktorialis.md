# Faktoriális — tanulói segédlet

Futtatás:

```bash
python main.py
```

## 1. A feladat

Egy `n` szám faktoriálisa: `n! = 1 · 2 · 3 · … · n`. Definíció szerint `0! = 1` és `1! = 1`.

## 2. Az algoritmus — sorozatszámítás

```python
n: int = int(input('n = '))
faktor: int = 1
for sz in range(2, n + 1):
    faktor = faktor * sz
print(f'{n}! = {faktor}')
```

Három fontos részlet:

1. A `faktor` **kezdőértéke 1**, nem 0 — szorzásnál az 1 a semleges elem (ha 0-ról indulnánk,
   a végeredmény is 0 lenne).
2. A ciklus **2-től** indul, mert 1-gyel szorozni fölösleges.
3. A felső határ `n + 1`, mert a `range` **végértéke nem tartozik bele** a sorozatba — `n`-ig
   kell szoroznunk.

Kövessük végig `n = 5` esetén:

| sz | művelet | faktor |
| --- | --- | --- |
| — | kezdőérték | 1 |
| 2 | 1 · 2 | 2 |
| 3 | 2 · 3 | 6 |
| 4 | 6 · 4 | 24 |
| 5 | 24 · 5 | 120 |

Ez a **sorozatszámítás** programozási tétel (lásd: *07_Programozasi_tetelek*).

## 3. Egymásba ágyazott ciklus

A program második fele 5-től 30-ig **minden** szám faktoriálisát kiírja:

```python
for n in range(5, 31):
    faktor: int = 1          # a belső ciklus előtt MINDIG újrainduló kezdőérték!
    for sz in range(2, n + 1):
        faktor = faktor * sz
    print(f'{n}! = {faktor}')
```

A **külső** ciklus adja az `n`-t, a **belső** kiszámolja hozzá a faktoriálist.
A leggyakoribb hiba itt a `faktor = 1` kihagyása a külső ciklus magjából — ilyenkor az
előző szám eredményéből indulnánk, és értelmetlen számokat kapnánk.

## 4. Kitekintés: a nagy számok

Nézd meg a `30!` értékét — 33 jegyű szám! A Python `int` típusa **tetszőlegesen nagy**
egészeket kezel, nincs túlcsordulás (a legtöbb más nyelvvel ellentétben).

## 5. Feladatok

1. Mennyi `0!` és `1!` a program szerint? Miért működik jól a ciklus ezekre is?
2. Írd át a számolást `while` ciklussal.
3. Írd meg a faktoriálist **függvénnyel** (lásd: *04_Fuggvenyek*), majd **rekurzívan** is
   (lásd: *04_Fuggvenyek/03_Rekurzio*).
