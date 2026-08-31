# Ez egy saját modul: egyszerűen egy .py kiterjesztésű Python forrásállomány,
# amit egy másik állományból importálva tudunk használni.
# A modul neve megegyezik az állomány nevével (kiterjesztés nélkül): sajat_modul

PI_KÖZELÍTŐ_ÉRTÉK: float = 3.14  # a modulban definiált adat (konstans)


def négyzet_területe(oldal: float) -> float:  # a modulban definiált függvény
    return oldal * oldal


def kör_területe(sugár: float) -> float:
    return PI_KÖZELÍTŐ_ÉRTÉK * sugár * sugár


# Ez a blokk csak akkor fut le, ha a modult ÖNÁLLÓAN (nem importálva) futtatjuk.
# Importáláskor a __name__ nem "__main__", hanem a modul neve lesz, ezért ilyenkor ez a rész kimarad.
if __name__ == "__main__":
    print('A sajat_modul.py-t importálás nélkül, önállóan futtattad!')
    print(f'négyzet_területe(4) = {négyzet_területe(4)}')
