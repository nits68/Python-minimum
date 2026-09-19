# Rekurzió — tanulói segédlet

Futtatás:

```bash
python main.py
```

## 1. Mi a rekurzió?

**Rekurzió**: olyan függvény (vagy metódus), amely a saját törzsében — közvetlenül vagy
közvetve — **önmagát hívja meg**.

Minden rekurzív függvénynek **két fő része** van:

1. **Alapeset (bázisállapot):** a legegyszerűbb eset, amit további hívás nélkül,
   közvetlenül meg tudunk válaszolni. **Ez állítja meg a rekurziót** — nélküle a program
   végtelen hívásláncba kerülne (`RecursionError: maximum recursion depth exceeded`).
2. **Rekurzív eset:** a feladatot egy „kisebb", az alapesethez **közelebb álló**
   részfeladatra vezetjük vissza, és a függvény önmagát hívja meg ezzel.

## 2. Faktoriális

```python
def faktoriális(n: int) -> int:
    if n == 0:                      # 1. Alapeset: 0! = 1
        return 1
    return n * faktoriális(n - 1)   # 2. Rekurzív eset: n! = n * (n-1)!
```

A hívások „kibomlása" `n = 4` esetén:

```
faktoriális(4) = 4 * faktoriális(3)
               = 4 * 3 * faktoriális(2)
               = 4 * 3 * 2 * faktoriális(1)
               = 4 * 3 * 2 * 1 * faktoriális(0)
               = 4 * 3 * 2 * 1 * 1 = 24
```

Figyeld meg: a **szorzások csak a visszafelé úton** hajtódnak végre, amikor az alapeset már
visszaadta az 1-et.

Ugyanez ciklussal (rekurzió nélkül):

```python
def faktoriális_iteratívan(n: int) -> int:
    eredmény: int = 1
    for i in range(2, n + 1):
        eredmény *= i
    return eredmény
```

A program mindkettőt kiírja — **ellenőrzésképpen** ugyanazt kell adniuk.

## 3. Fibonacci-sorozat

`0, 1, 1, 2, 3, 5, 8, 13, 21, …` — minden elem (a 0. és 1. kivételével) az **előző kettő
összege**.

```python
def fibonacci(n: int) -> int:
    if n <= 1:                                   # Alapeset: fib(0)=0, fib(1)=1
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)   # Rekurzív eset
```

Itt a függvény **kétszer** hívja meg önmagát — a hívások „fát" alkotnak. Ez elegáns, de
nagyon pazarló: `fibonacci(30)` már több mint egymillió hívást jelent, mert ugyanazokat a
részeredményeket újra és újra kiszámolja.

## 4. Számjegyek összege

```python
def számjegyek_összege(n: int) -> int:
    if n < 10:                                       # Alapeset: egyjegyű szám
        return n
    return n % 10 + számjegyek_összege(n // 10)
```

A két alapművelet, amit érdemes megjegyezni:

- `n % 10` → az **utolsó számjegy**,
- `n // 10` → a szám az utolsó számjegy **nélkül**.

`987654` → `4 + (5 + (6 + (7 + (8 + 9))))` = **39**.

## 5. Mikor NE használj rekurziót?

A rekurzió kényelmes, de nem „ingyenes":

- minden hívás **új végrehajtási keretet (stack frame)** foglal le a memóriában,
- mély vagy hibásan megírt rekurzió (hiányzó, rossz alapeset) `RecursionError`-t okoz
  (a Python alapértelmezett korlátja kb. 1000 hívásmélység),
- jellemzően **lassabb**, mint az egyenértékű ciklusos megoldás.

Ezért egyszerűbb feladatoknál (faktoriális, összegzés) a gyakorlatban inkább **ciklust**
használunk. A rekurzió ott játszik igazán, ahol a feladat maga is „önmagára hivatkozó"
szerkezetű (fabejárás, könyvtárszerkezet, oszd-meg-és-uralkodj algoritmusok).

## 6. Feladatok

1. Vedd ki az alapesetet a `faktoriális()`-ból, és nézd meg a hibaüzenetet!
2. Írd meg a Fibonacci-sorozatot **ciklussal**, és mérd meg, mennyivel gyorsabb.
3. Írj rekurzív függvényt, ami megfordít egy szöveget.
4. Írj rekurzív függvényt 1-től `n`-ig az összeg kiszámítására.
