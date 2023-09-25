#Header 
'''
Fichier contenant les fonctions du TP1 
Réalisé par Ballandras Quentin le 25/09/23
'''


def bissextille (année : int)-> bool : # Fonction qui renvoie 'True' si une 'année' est bissextile et 'False' sinon
    assert isinstance(année,int), 'Saisie invalide'
    if année % 400 == 0 : # On vérifie si l'année est un multiple de 400
        return True
    elif année % 100 != 0 and année % 4 == 0 : # On vérifie si l'année est un multiple de 4 et n'est pas un multiple de 100
        return True
    else : 
        return False 

def nombre_mois (mois, an) : # Fonction qui donne le nombre de jour d'un mois en fonction de celui-ci mais également de l'année 
    # Définition des listes contenant les mois en fonction du nombre de jour 
    liste_mois_30 = [4,6,9,11] # liste de mois à 30 jours 
    février = 2 # numéro du mois de février 
    assert isinstance(mois,int) and 1 <= mois <= 12 , 'Saisie invalide'
    if mois == février : # Traitement du cas particulier du mois de février
        if bissextille(an) == True : # Vérification de si l'année est bissextile 
            return 29
        return 28
    elif mois in liste_mois_30 : 
        return 30
    return 31
    

def date_valide (jour, mois, année) : # Fonction qui vérifie le nombre 
    assert isinstance(jour,int) and 1 <= mois <= 31 , 'Saisie invalide'
    if jour <= nombre_mois(mois,année):
        return 'Date valide'
    return 'Date non valide'
        

