#Header 
'''
Fichier contenant le programme principale du TP1 
Réalisé par Ballandras Quentin le 25/09/23
'''

from Fct import date_valide

# Programme principale de l'exo question 2 
date=input("Entrez une date en séparant par des '/' et en écrivant l'année en entier")
date=date.split('/')
print(Fct.date_valide(date[0],date[1],date[2]))




