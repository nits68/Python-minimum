# Programozási tételek — tanulói segédlet

Futtatás:

```bash
python main.py
```

A **programozási tételek** tipikus, újra és újra előforduló részfeladatok bevált
megoldásai. Ha felismered, melyik tételről van szó, a kódot már „fejből" tudod írni.

## 1. Adatszerkezet feltöltésének módjai

### 1.1 Felhasználói bemenetről (végjeles beolvasás)

```python
nevek: list[str] = []
inputNév: str = ''
while inputNév != '0':
    inputNév = input('Név: ')
    if inputNév != '0' and len(inputNév) != 0:
        nevek.append(inputNév)
```

Pontos, de **időigényes** tesztelni. A `0` itt a **végjel**.

### 1.2 Véletlen értékekkel

```python
számok: list[int] = []
for i in range(5):
    számok.append(random.randint(10, 99))
```

Teszteléshez ez a leggyorsabb — minden futtatás más adatokat ad.

### 1.3 Literálokkal

```python
állítások: list[bool] = [True, True, False, True, False]
```

### 1.4 Szöveges állományból (soronként egy adat)

```python
with open('bukk-videk.txt', 'r', encoding='UTF-8') as sr:
    sorok: list[str] = sr.read().splitlines()

magasságok: list[float] = []
for sor in sorok:
    magasságok.append(float(sor))
```

A beolvasott sorok **szövegek**, ezért konvertálni kell (`float()`). A `splitlines()` a
sortöréseknél darabol listává.

> Bővebben: *09_Filekezeles*.

## 2. Az adatszerkezet bejárása

```python
for e in számok:                      # ha az index NEM kell
    print(e, end=' ')

for i in range(len(számok)):          # ha az index kell
    print(f'számok[{i}] = {számok[i]}')

for i, e in enumerate(számok):        # index ÉS érték egyszerre
    print(f'számok[{i}] = {e}')
```

## 3. Egy sorozathoz egy értéket rendelő tételek

### 3.1 Eldöntés

*Van-e a listában megadott tulajdonságú elem?* Az eredmény **logikai** érték.

```python
vanPáratlan: bool = False      # feltételezzük, hogy NINCS ilyen elem
for szám in számok:
    if szám % 2 == 1:
        vanPáratlan = True
        break                  # megvan a válasz — ne keressünk tovább!
```

A `break` fontos: ha megvan a válasz, felesleges folytatni.

A kiírás háromféleképpen (mindhárom ugyanazt adja):

```python
if vanPáratlan:
    print('A listában van páratlan szám!')
else:
    print('A listában nincs páratlan szám!')

print(('A listában van' if vanPáratlan else 'A listában nincs') + ' páratlan szám!')

print(f'A listában {"van" if vanPáratlan else "nincs"} páratlan szám!')
```

Figyelem: a feltételes kifejezés **lazábban köt**, mint a `+`, ezért a második változatban
**zárójelezni kell**.

### 3.2 Megszámlálás

*Hány megadott tulajdonságú elem van?*

```python
db_páros_50: int = 0            # a számláló MINDIG 0-ról indul
for e in számok:
    if e % 2 == 0 and e > 50:
        db_páros_50 += 1
```

### 3.3 Összegzés (és átlag)

```python
db_oszt5: int = 0
összeg_oszt5 = 0                # összegzésnél a kezdőérték 0 (szorzásnál 1 lenne!)
for e in számok:
    if e % 5 == 0:
        db_oszt5 += 1
        összeg_oszt5 += e

if db_oszt5 == 0:               # NULLÁVAL NEM OSZTHATUNK!
    print('Nincs a listában 5-el osztható szám!')
else:
    print(f'Az átlaguk: {összeg_oszt5 / db_oszt5}')
```

Az átlagszámítás előtti **nullavizsgálat kötelező** — e nélkül a program hibával leáll,
ha egyetlen megfelelő elem sincs.

### 3.4 Szélsőérték-keresés (minimum, maximum)

**a) Csak az érték kell**

```python
max: int = számok[0]            # kinevezzük az első elemet a legnagyobbnak
for szám in számok[1:]:         # az elsőt elhagyjuk: önmagához nem hasonlítjuk
    if szám > max:
        max = szám
```

**b) Az érték és az index is kell** — ilyenkor az **indexet** tároljuk:

```python
mini: int = 0                   # az első elem indexe
for i in range(1, len(számok)):
    if számok[i] < számok[mini]:
        mini = i
print(f'érték: {számok[mini]}, index: {mini}')
```

Az indexből az érték mindig előállítható (`számok[mini]`), fordítva nem — ezért érdemes az
indexet tárolni.

**c) Holtverseny kezelése** — a minimum ismeretében újra végigmegyünk a listán:

```python
for i, e in enumerate(számok):
    if e == számok[mini]:
        print(i, end=' ')
```

**d) Ha nem nevezhető ki az első elem** (mert feltételnek is meg kell felelnie):

```python
maxi_páratlan: int = -1         # -1: "még nem találtunk ilyen elemet"
for i, e in enumerate(számok):
    if e % 2 == 1:
        if maxi_páratlan == -1:     # az ELSŐ páratlan szám: ezt nevezzük ki
            maxi_páratlan = i
        elif e > számok[maxi_páratlan]:
            maxi_páratlan = i

if maxi_páratlan == -1:
    print('Nincs a listában páratlan szám!')
```

A `-1` kezdőérték egyszerre jelenti azt, hogy „még nincs jelöltünk", és azt, hogy „nincs
ilyen elem" — a ciklus után ezt vizsgálni **kell**.

## 4. Egy sorozathoz egy sorozatot rendelő tételek

### 4.1 Kiválogatás

*Gyűjtsük külön a megadott tulajdonságú elemeket.*

```python
osztható3al: list[int] = []
for e in számok:
    if e % 3 == 0:
        osztható3al.append(e)
```

A séma mindig ugyanaz: **üres lista → bejárás → feltétel → `append()`**.

### 4.2 Rendezés — buborékos rendezés

```python
for ig in range(len(számok) - 1, 0, -1):
    csere_volt: bool = False
    for i in range(ig):
        if számok[i] > számok[i + 1]:
            seged: int = számok[i]         # segédváltozó a két érték cseréjéhez
            számok[i] = számok[i + 1]
            számok[i + 1] = seged
            csere_volt = True
    if csere_volt is False:                # nem volt csere -> már rendezett
        break
```

Hogyan működik? Az egymás mellett álló elemeket hasonlítjuk össze, és ha rossz a
sorrendjük, **felcseréljük** őket. Így a legnagyobb elem minden körben „felbuborékol" a
lista végére — ezért csökken a belső ciklus felső határa (`ig`).

Két kulcsrészlet:

- **A csere segédváltozóval**: közvetlenül nem tudunk két értéket felcserélni, kell egy
  átmeneti tároló. (Pythonban van rövidebb út is: `a, b = b, a`.)
- **A `csere_volt` jelzőváltozó**: ha egy teljes körben nem volt csere, a lista már
  rendezett, kiléphetünk.

## 5. Egy sorozathoz két sorozatot rendelő tételek

### 5.1 Szétválogatás

```python
páros_számok: list[int] = []
páratlan_számok: list[int] = []
for e in számok:
    if e % 2 == 0:
        páros_számok.append(e)
    else:
        páratlan_számok.append(e)
```

A kiválogatás „kétkimenetű" változata: **minden** elem kerül valahová.

## 6. Két sorozathoz egy sorozatot rendelő tételek (kitekintés)

- **Összefuttatás** — két **rendezett** sorozat összefésülése egy rendezetté,
- **Egyesítés (unió)** — a két sorozatban előforduló összes elem, ismétlés nélkül,
- **Metszet** — a mindkét sorozatban szereplő elemek.

Ezekre halmazokkal is van kész megoldás (lásd: *05_Kollekciok/02_Halmazok*).

## 7. Összefoglaló táblázat

| Tétel | Kezdőérték | A cikluson belül |
| --- | --- | --- |
| eldöntés | `False` | feltétel → `True` + `break` |
| megszámlálás | `0` | feltétel → `+= 1` |
| összegzés | `0` | feltétel → `+= e` |
| maximum/minimum | első elem (vagy `-1`) | jobb elem → megjegyezzük |
| kiválogatás | üres lista | feltétel → `append()` |
| szétválogatás | két üres lista | `if-else` → `append()` |

## 8. Feladatok

A `bukk-videk.txt` állomány magasságadataival:

1. Hány hegycsúcs magasabb 900 méternél?
2. Mennyi a magasságok átlaga?
3. Melyik a legmagasabb csúcs, és hányadik a sorban?
4. Válogasd ki külön a 800 méternél magasabb és alacsonyabb csúcsokat.
