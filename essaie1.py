def condition_erreur(nombre1, operateur, nombre2):
    if not (0 <= nombre1 <= 10 and 0 <= nombre2 <= 10):
        return "Erreur : Les nombres doivent être entre 0 et 10."
    if operateur == "/" and nombre2 == 0 and nombre1 == 0:
        return "Erreur : Division par zéro."
    return None

def effectuer_operation(nombre1, operateur, nombre2):
    if operateur == "/":
        return nombre1 / nombre2
    elif operateur == "*":
        return nombre1 * nombre2
    elif operateur == "+":
        return nombre1 + nombre2
    elif operateur == "-":
        return nombre1 - nombre2
    else:
        return "Erreur : opérateur invalide."


#fonction principale
def calculatrice():

    nombre1 = int(input("Entrez le premier nombre (entre 0 et 10) : "))
    operateur = input("Entrez l'opérateur (+, -, *, /) : ")
    nombre2 = int(input("Entrez le deuxième nombre (entre 0 et 10) : "))

    erreur = condition_erreur(nombre1, operateur, nombre2)
    if erreur:
        print(erreur)
        return

    # Calcul du résultat
    resultat = effectuer_operation(nombre1, operateur, nombre2)
    print(f"Résultat : {resultat}")

# Appel de la calculatrice
calculatrice()