# ============================================================
# AKIENI ACADEMY — Projet Sante Publique
# Semaine 2 — Exercice 1 : Fiche Patient CHU Brazzaville
# Votre nom : Max MONGO
# Date : 26/06/2026
# ============================================================

# --- SECTION 1 : VARIABLES PATIENT --- 
# TODO : Voici toutes les variables patient ci-dessous 
nom_patient: str = 'MAVOUNGOU Celestine'  
age_patient: str = "42" 
sexe_patient: str = 'F'  
departement_patient: str = 'Brazzaville' 
couverture_sociale: str= 'CNSS' 
 
# --- SECTION 2 : VARIABLES CONSULTATION --- 
# TODO : Voici les variables consultation 
type_consultation: str = 'Urgences' 
cout_consultation_fcfa: int = 15000  
nb_consultations: int = 1 
remise_cnss_pct: float = 30.0 
diagnostic_principal: str= 'Paludisme grave'
 
 
# --- SECTION 3 : VARIABLES HOPITAL --- 
# TODO : Voici les variables hopital 
nom_hopital: str = 'CHU de Brazzaville'
ville_hopital: str = 'Brazzaville' 
nb_lits_total: int = 320 
nb_lits_occupes: int = 284 
nb_medecins_actifs: int = 47 
  # --- IMPORTANT nb signifie: nombre. Ex : nombre de lit 


# --- SECTION 4 : CALCULS --- 
# TODO :  le cout total apres remise CNSS 
cout_total_fcfa = cout_consultation_fcfa * nb_consultations  * (1 - remise_cnss_pct / 100)
 
# TODO : le taux d'occupation (en pourcentage, arrondi a 1 decimale) 
taux_occupation_pct = round(nb_lits_occupes / nb_lits_total * 100, 2) 
 
# TODO : le ratio consultations par medecin (ce jour) 
# Hypothese : 120 consultations ont eu lieu ce matin dans tout l'hopital 
nb_consultations_hopital: int = 120 
ratio_consultations_medecin = round(nb_consultations_hopital / nb_medecins_actifs, 1) 
 
# --- SECTION 5 : AFFICHAGE --- 
# TODO : Affichage de la fiche complete avec f-strings
print('='*60) 
print(f'  FICHE PATIENT — {nom_patient}') 
print('='*60) 
print(f'Age : {age_patient}')
print(f'Sexe : {sexe_patient}')
print(f'Departement : {departement_patient}')
print(f'Couverture : {couverture_sociale}')

print('='*60) 

print(f'CONSULTATIONS')
print(f'Type : {type_consultation}')
print(f'Diagnostiquec : {diagnostic_principal}') 
print(f'Cout Unitaire : {cout_consultation_fcfa:,} FCFA' .replace(",", " "))
print(f'Remise CNSS : {remise_cnss_pct} %')
print(f'COUT TOTAL : {cout_total_fcfa:,} FCFA' .replace(",", " "))

print('='*60) 

print(f'HOPITAL : CHU de Brazzaville')
print(f'Ville : {ville_hopital}')
print(f"lits occupes : { nb_lits_occupes} / {nb_lits_total}, ( {taux_occupation_pct}% )")
print(f'Medecins actifs : {nb_medecins_actifs}')
print(f'Ration consult. : {ratio_consultations_medecin} consultations / ce matin')

print('='*60) 
print("STATUT : Prise en charges vqlidee")

# ...Affichage Terminer 
 
# --- La suite du projet au deuxieme ficher 
