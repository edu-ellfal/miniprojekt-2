"""
Projekt 2: Högt/lågt-spel med highscore
Ett spel där användaren gissar ett slumpmässigt tal.
Highscore sparas i JSON-format.
"""

import random
import json

# === FILHANTERING ===

def ladda_highscore(filnamn="highscore.json"):
    try:
        with open(filnamn, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def spara_highscore(highscore_lista, filnamn="highscore.json"):
    with open(filnamn, "w") as f:
        json.dump(highscore_lista, f, indent=4, ensure_ascii=False)


# === SPELMECKANIK ===

def spela_omgang():
    hemligt_tal = random.randint(1, 100)
    antal = 0

    print("\nJag tänker på ett tal mellan 1 och 100...")

    while True:
        try:
            gissa = int(input("Gissa: "))
            antal += 1

            if gissa < hemligt_tal:
                print("För lågt!")
            elif gissa > hemligt_tal:
                print("För högt!")
            else:
                print(f"Rätt! Du klarade det på {antal} gissningar.")
                return antal
        except ValueError:
            print("Skriv ett giltigt heltal!")


# === HIGHSCORE-VISNING ===

def visa_highscore(highscore_lista):
    print("\n--- HIGHSCORE ---")

    if not highscore_lista:
        print("Inga resultat ännu")
        return

    sorterad = sorted(highscore_lista, key=lambda x: x["gissningar"])

    for i, spelare in enumerate(sorterad, start=1):
        print(f"{i}. {spelare['namn']} - {spelare['gissningar']} gissningar")


# === HUVUDPROGRAM ===

def huvudprogram():
    highscore_lista = ladda_highscore()

    while True:
        print("\n--- HÖGT / LÅGT ---")
        print("1. Spela ny omgång")
        print("2. Visa highscore")
        print("3. Avsluta")

        val = input("Välj: ")

        if val == "1":
            antal = spela_omgang()
            namn = input("Skriv ditt namn: ")

            spelare = {
                "namn": namn,
                "gissningar": antal
            }

            highscore_lista.append(spelare)
            spara_highscore(highscore_lista)

        elif val == "2":
            visa_highscore(highscore_lista)

        elif val == "3":
            print("Hejdå!")
            break

        else:
            print("Ogiltigt val, försök igen.")


# Starta programmet
if __name__ == "__main__":
    huvudprogram()