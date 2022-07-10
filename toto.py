import numpy as np

def get_name():
    print("Rentre ton blaze :")
    prenom=input()
    prenom_without_case=prenom.casefold()
    if prenom.isalpha()==False :
        print("ERREUR : Le nom fourni ne peut contenir que des lettres de l'alphabet sans espace")
        quit() 
    print("Le prénom à classer est : " + prenom + ". Sa longueur est de " + str(len(prenom)) + " caracteres")
    return prenom_without_case

def give_name_rank(prenom):
    longueur = int(len(prenom))
    classement = 0

    #Algo
    for i in range(longueur) :
        classement = classement + ((ord(prenom[i])-96) * pow(26,longueur-i-1))

    return classement

prenom=get_name()
classement = give_name_rank(prenom)

#Résultat
print("Vous êtes classé numéro : ", classement)


