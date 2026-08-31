# pylint: disable=line-too-long


def main() -> None:

    #  Szótár létrehozása:
    szotar1 = {  # Elemekkel inicializált szótár # type: ignore
        "brand": "Ford",
        "veteran": True,
        "year": 1964,
    }

    # Jellemzően a szótár kulcsa és értéke azonos típusú, amit meg is adhatunk a typing modult használva:
    szotar2: dict[str, int] = {"Magyarország": 12, "Ausztria": 34, "Anglia": 23}

    szotar3 = dict([("x", 5), ("y", -5)])  # Szótár létrehozása a dict() konstruktorral
    szotar4: dict[int, int] = {}  # Üres 'típusos' szótár
    # FIGYELEM: a "dict[int, int]" (zárójel nélkül) csak egy típusjelölés, nem hoz létre szótárpéldányt!
    szotar5 = dict({})  # type: ignore # Üres 'típus nélküli' szótár létrehozása

    # Teljes szótár kiírása
    print(szotar1)  # type: ignore
    print(szotar2)
    print(szotar3)
    print(szotar4)
    print(szotar5)  # type: ignore

    # Hivatkozás szótár elemeire (indexelés)
    # Szótárak elemire a kulcsok segítségével, mint indexekkel tudunk hivatkozni
    print(szotar1["brand"])  # type: ignore # Ford
    szotar1["year"] = 1968
    # Indexelés helyett használhatjuk a get() függvényt is
    print(szotar1.get("year"))  # type: ignore # 1968

    # Szótár bejárása:
    for key, value in szotar2.items():
        print(f"Kulcs: {key} Érték: {value}")

    for i in szotar2.values():
        print(f"Érték: {i}")

    # A megadott kulcs szerepel-e a szótárban?
    if "Anglia" in szotar2:
        print("Anglia szerepel a szótár kulcsai között!")

    # Szótárban lévő kulcs-értékpárok száma:
    print(f"A szotar2 kulcs-értékpárjainak a száma: {len(szotar2)}")

    # Új elem (kulcs-érték pár) hozzáadása a szótárhoz:
    szotar2["Szlovénia"] = 34
    print(szotar2)

    # Elem (kulcs-érték pár) törlése:
    szotar2.pop("Ausztria")
    print(szotar2)

    # Szótár ürítése (minden elem törlése)
    szotar2.clear()
    print(szotar2)  # {}

    # Teljes szótár törlése
    # del szotar2
    # print(szotar2)  # Hiba: UnboundLocalError local variable 'szotar2' referenced before assignment

    # Szótár másolása
    # szotar6 = szotar1  # Így csak a szotar6 referenciája is szotar1 lesz! (azonos memóriacímre mutatnak)
    szotar6 = ( # type: ignore
        szotar1.copy()
    )  # Csak így lesz fizikailag egy új referenciára másolva szotar1 adatai
    print(szotar6) # type: ignore
    # Másoláshoz használhatjuk a dict() konstruktort is:
    szotar7 = dict(szotar1) # type: ignore
    print(szotar7) # type: ignore
    # Szótár létrehozása kulcsokkal és azonos 'alapértelmetett' értékel:
    myTuple = ("kulcs1", "kulcs2", "kulcs3")
    thisdict = dict.fromkeys(myTuple, 0)
    print(thisdict)


if __name__ == "__main__":
    main()
