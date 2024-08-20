import csv
import sys

def load_csv(file_path):
    heroes = []
    with open(file_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            heroes.append({
                "Hero": row["Hero"],
                "Location": row["Location"],
                "First Villain": row["First Villain"]
            })
    return heroes

def encode_heroes(heroes):
    encoded_heroes = []
    for hero in heroes:
        encoded_hero = {
            "Hero": hero["Hero"],
            "Location": hero["Location"],
            "First_Villain": hero["First Villain"]
        }
        encoded_heroes.append(encoded_hero)
    return encoded_heroes


if __name__ == "__main__":
    file_path = 'marvel_char.csv'
    heroes = load_csv(file_path)
    encoded_heroes = encode_heroes(heroes)

    for hero in encoded_heroes:
        print(hero)