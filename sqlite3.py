import sqlite3

conn = sqlite3.connect("pets.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS pets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        species TEXT
    )
""")

cursor.execute("""
               INSERT INTO pets (name, species)
               VALUES (?, ?)
               """,
               ("Mephisto", "Crow"))

cursor.execute("""
               INSERT INTO pets (name, species)
               VALUES (?, ?)
               """,
               ("Kitty", "Cat"))

cursor.execute("""
               INSERT INTO pets (name, species)
               VALUES (?, ?)
               """,
               ("Zell", "Iguana"))

cursor.execute("""
               INSERT INTO pets (name, species)
               VALUES (?, ?)
               """,
               ("Tofu", "Snake"))

cursor.execute("SELECT * FROM pets")

pets1 = cursor.fetchall()

print("Before: ")
for p in pets1:
    print(p)
cursor.execute("""
            UPDATE pets
            SET species = ?
            WHERE name = ?
               """,
               ("Red Iguana", "Zell"))

cursor.execute("""
            DELETE FROM pets
            WHERE name = ?
               """,
               ("Tofu",))

cursor.execute("SELECT * FROM pets")

pets = cursor.fetchall()

print("After :")
for pet in pets:
    print(pet)


conn.commit()
conn.close()