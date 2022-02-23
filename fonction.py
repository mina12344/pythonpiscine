import math as m


def lenom(): 
    Nom = input("Entez votre nom: ")
    Prenom =input("Entez votre prenom: ")

    print("Bonjour", Nom, Prenom + "!")


def age():
    Age = input("entrez votre age ")
    age_hundred=2022+100-int(Age)
    print("vous aurez 100 ans en: ", age_hundred)

def volume():
    r=input("le rayon:")
    h=input("la hauteur: ")
    volume= 1/3*m.pi() * float(r^2)  * float(h)