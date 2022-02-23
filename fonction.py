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
    r=float(input("le rayon:"))
    h=float(input("la hauteur: "))
    volume= 1/3*(m.pi)*(r**2)*(h)
    print("le volume est ", volume)

def paire():
    n=int(input("un chiffre :"))
    if(n%2==0):
        print("Nombre paire")
    else: print("Nombre impaire")

def fibonacci():
    n = int(input("Entrez un nombre:"))
    def fib(n): 
        if(n <= 1):
            return n
        else:
            return (fib(n-1) + fib(n-2))
    print(fib(n))        
