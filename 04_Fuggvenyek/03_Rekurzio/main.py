# Rekurzió: olyan függvény (vagy metódus), amely a saját törzsében (közvetlenül
# vagy közvetve) önmagát hívja meg.
# Minden rekurzív függvénynek két fő része van:
#   1. Alapeset (bázisállapot): a legegyszerűbb eset, amit közvetlenül, hívás nélkül
#      meg tudunk válaszolni. Ez állítja meg a rekurziót, e nélkül a program végtelen
#      hívásláncba kerülne (RecursionError: maximum recursion depth exceeded).
#   2. Rekurzív eset: a feladatot egy "kisebb" (az alapesethez közelebb álló)
#      részfeladatra vezetjük vissza, és a függvény önmagát hívja meg ezzel a
#      részfeladattal.


def faktoriális(n: int) -> int:
    if n == 0:  # 1. Alapeset: 0! = 1
        return 1
    return n * faktoriális(n - 1)  # 2. Rekurzív eset: n! = n * (n-1)!


def faktoriális_iteratívan(n: int) -> int:
    # Ugyanaz az eredmény ciklussal (rekurzió nélkül) is előállítható:
    eredmény: int = 1
    for i in range(2, n + 1):
        eredmény *= i
    return eredmény


def fibonacci(n: int) -> int:
    # A Fibonacci-sorozat: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
    # Minden elem (a 0. és 1. kivételével) az előző kettő összege.
    if n <= 1:  # Alapeset: fib(0) = 0, fib(1) = 1
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)  # Rekurzív eset


def számjegyek_összege(n: int) -> int:
    # Egy szám számjegyeinek összege rekurzívan
    if n < 10:  # Alapeset: egyjegyű szám, önmaga az összeg
        return n
    return n % 10 + számjegyek_összege(n // 10)  # utolsó számjegy + a maradék rekurzív összege


def main() -> None:
    print('Rekurzió - Faktoriális')
    n: int = int(input('n = '))
    print(f'{n}! = {faktoriális(n)} (rekurzívan)')
    print(f'{n}! = {faktoriális_iteratívan(n)} (iteratívan, ellenőrzésképpen)')

    print('\nRekurzió - Fibonacci-sorozat első 10 eleme')
    for i in range(10):
        print(fibonacci(i), end=' ')
    print()

    print('\nRekurzió - Számjegyek összege')
    szám: int = 987654
    print(f'A {szám} számjegyeinek összege: {számjegyek_összege(szám)}')

    # Figyelem: a rekurzió kényelmes, de nem "ingyenes" - minden hívás új
    # végrehajtási keretet (stack frame) foglal le, ezért mély/nem megfelelően
    # megírt rekurzió (hiányzó vagy hibás alapeset) könnyen RecursionError-t okozhat,
    # és jellemzően lassabb is, mint az egyenértékű iteratív (ciklusos) megoldás.
    # Éppen ezért sok, egyszerűbb feladat (pl. faktoriális, összegzés) esetén
    # a gyakorlatban inkább a ciklust (while, for) részesítjük előnyben.


if __name__ == "__main__":
    main()
