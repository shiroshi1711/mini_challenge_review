# review
# bikin pet shop system
# animal class atribut nama umur ama suara, umur di encapsulate n kasih get methodnya
# method speak () n {name} says {sound}, intro() n hi im {name} im a {species} and im {age} y.o
# 2 child class, pet atribut + owner, wild animal atribut + habitat
# method pet show owner n {name} belongs to {owner}
# method wild animal show habitat n {name} lives in {habitat}
# custom error invalid age kalo ketuaan atau 0 kebawah
# save ke petshop.json, read it back n print everything
# regex text = our pets are 2, 5, and 8 years old!
# bikin generator animal_sound() that yield each animal's sound one by one

import json
import re

filename = "petshop.json"

class AgeTooOldError(Exception):
    pass

class AgeTooYoungError(Exception):
    pass

class Animal:
    def __init__(self, name, species, age, sound):
        self.name = name
        self.species = species
        if age < 0:
            raise AgeTooYoungError("age cant be minus!")
        elif age > 100:
            raise AgeTooOldError("age too old!")
        self.__age = age
        self.sound = sound

    def get_age(self):
        return self.__age
    
    def speak(self):
        print(f'{self.name} says {self.sound}!')

    def show_info(self):
        pass
    
    def introduce(self):
        print(f"Hi! I am {self.name}, I am a {self.species} and I am {self.__age} years old!")

    def to_dict(self):
        return {
            "name" : self.name,
            "species" : self.species,
            "age" : self.__age,
            "sound" : self.sound
        } 

class Pet(Animal):
    def __init__(self, name, species, age, sound, owner):
        super().__init__(name, species, age, sound)
        self.owner = owner

    def show_owner(self):
        print(f'{self.name} belongs to {self.owner}!')

    def show_info(self):
        return self.show_owner()

    def to_dict(self):
        data = super().to_dict()
        data["owner"] = self.owner
        return data

class WildAnimal(Animal):
    def __init__(self, name, species, age, sound, habitat):
        super().__init__(name, species, age, sound)
        self.habitat = habitat

    def show_habitat(self):
        print(f'{self.name} lives in {self.habitat}!')

    def show_info(self):
        return self.show_habitat()

    def to_dict(self):
        data = super().to_dict()
        data["habitat"] = self.habitat
        return data

try:
    animal1 = Pet("Milo","poodle", 2, "woof", "Friend")
    animal2 = Pet("Buddy", "golden retriever", 5, "woof", "Papi")
    animal3 = Pet("Kitty", "maine coon", 3, "meow", "Shiro" )
    animal4 = WildAnimal("Crow", "bird", 1, "caw ", "woodlands")
except AgeTooOldError as e:
    print(e)
except AgeTooYoungError as e:
    print(e)

animals = [animal1,animal2,animal3,animal4]

for animal in animals:
    animal.speak()
    print()
    animal.introduce()
    print()
    animal.show_info()
    print()

print()

dictdata = [animal1.to_dict(), animal2.to_dict(), animal3.to_dict(), animal4.to_dict()]

with open (filename, "w") as file:
    json.dump(dictdata, file, indent=4)
    print(f"{filename} saved to JSON ✅")

print()

try:
    with open(filename,"r") as p:
        data = json.load(p)
        print(data)
        print()
        print(type(data))
except FileNotFoundError:
    print('file not found error')

print()

def animal_sound(animal_sound):
    for s in animal_sound:
        yield f'{s} {s}!'

sound = [animal["sound"] for animal in data]

a = animal_sound(sound)

for b in a:
    print(b)
    print()

text = "our animals are 2,5,8 years old"

ages = re.findall(r'\d+', text)
print(ages)