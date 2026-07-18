
"""j'ai definer a et b comme mes variables de base"""
"""et la fonction demander_deux_nombres() la base de tout le code """
def demander_deux_nombres():
    while True:
        try:
            a = float(input("Entre le premier nombre : "))
            b = float(input("Entre le deuxième nombre : "))
            return a, b
        except ValueError:
            print("Erreur : tape des nombres valides (entiers ou décimaux).")

def calculatrice():
   
    while True:
        print(f"\n=== MENU CALCULATRICE ===")
        print(f"1 - Addition")
        print(f"2 - Soustraction")
        print(f"3 - Multiplication")
        print(f"4 - Division")
        print(f"FIN - Pour quitter la calculatrice")

        choix = input("Entre le numéro de ton choix : ")

        if choix.upper() == "FIN":
            print(f"À bientôt !")
            break

        if choix in ["1", "2", "3", "4"]:
            num1, num2 = demander_deux_nombres()

            if choix == "1":
                resultat = num1 + num2
            elif choix == "2":
                resultat = num1 - num2
            elif choix == "3":
                resultat = num1 * num2
            elif choix == "4":
                if num2 == 0:
                    print(f"Tu es bete ou quoi depuis quand en divise un nombre par zéro.")
                    continue
                resultat = num1 / num2

            print(f"Le résultat est : {resultat}")
        else:
            print(f"Tape un numéro valide entre (1 et 4) ou 'FIN' pour quitter.")

# Pour appeler  la calculatrice 
calculatrice()
