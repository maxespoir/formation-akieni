# ============================================================
# AKIENI ACADEMY — Projet Sante Publique
# Semaine 3 — Challenge : Tableau de Bord 5 Hopitaux
# ============================================================

# --- VARIABLES DES 5 HOPITAUX ---
h1_nom = 'CHU Brazzaville'
h1_lits_total = 320
h1_lits_occupes = 298
h1_nb_medecins = 47
h1_nb_ruptures = 2
h1_nb_alertes = 2

h2_nom = 'Hopital Pointe-Noire'
h2_lits_total = 180
h2_lits_occupes = 143
h2_nb_medecins = 22
h2_nb_ruptures = 0
h2_nb_alertes = 1

h3_nom = 'Hopital Dolisie'
h3_lits_total = 95
h3_lits_occupes = 91
h3_nb_medecins = 8
h3_nb_ruptures = 1
h3_nb_alertes = 2

h4_nom = 'Hopital Owando'
h4_lits_total = 45
h4_lits_occupes = 32
h4_nb_medecins = 3
h4_nb_ruptures = 3
h4_nb_alertes = 0

h5_nom = 'CMS Impfondo'
h5_lits_total = 20
h5_lits_occupes = 19
h5_nb_medecins = 1
h5_nb_ruptures = 2
h5_nb_alertes = 1

# --- HOPITAL 1 : CALCUL ET CLASSIFICATION ---
h1_taux_occupation = round(h1_lits_occupes / h1_lits_total * 100, 1)

if h1_nb_ruptures >= 2 or h1_taux_occupation > 95:
    h1_niveau_global = 'CRITIQUE'
elif h1_nb_ruptures >= 1 or h1_taux_occupation > 85 or (h1_nb_alertes >= 2 and h1_nb_medecins < 5):
    h1_niveau_global = 'PREOCCUPANT'
else:
    h1_niveau_global = 'SATISFAISANT'

# --- HOPITAL 2 : CALCUL ET CLASSIFICATION ---
h2_taux_occupation = round(h2_lits_occupes / h2_lits_total * 100, 1)

if h2_nb_ruptures >= 2 or h2_taux_occupation > 95:
    h2_niveau_global = 'CRITIQUE'
elif h2_nb_ruptures >= 1 or h2_taux_occupation > 85 or (h2_nb_alertes >= 2 and h2_nb_medecins < 5):
    h2_niveau_global = 'PREOCCUPANT'
else:
    h2_niveau_global = 'SATISFAISANT'

# --- HOPITAL 3 : CALCUL ET CLASSIFICATION ---
h3_taux_occupation = round(h3_lits_occupes / h3_lits_total * 100, 1)

if h3_nb_ruptures >= 2 or h3_taux_occupation > 95:
    h3_niveau_global = 'CRITIQUE'
elif h3_nb_ruptures >= 1 or h3_taux_occupation > 85 or (h3_nb_alertes >= 2 and h3_nb_medecins < 5):
    h3_niveau_global = 'PREOCCUPANT'
else:
    h3_niveau_global = 'SATISFAISANT'

# --- HOPITAL 4 : CALCUL ET CLASSIFICATION ---
h4_taux_occupation = round(h4_lits_occupes / h4_lits_total * 100, 1)

if h4_nb_ruptures >= 2 or h4_taux_occupation > 95:
    h4_niveau_global = 'CRITIQUE'
elif h4_nb_ruptures >= 1 or h4_taux_occupation > 85 or (h4_nb_alertes >= 2 and h4_nb_medecins < 5):
    h4_niveau_global = 'PREOCCUPANT'
else:
    h4_niveau_global = 'SATISFAISANT'

# --- HOPITAL 5 : CALCUL ET CLASSIFICATION ---
h5_taux_occupation = round(h5_lits_occupes / h5_lits_total * 100, 1)

if h5_nb_ruptures >= 2 or h5_taux_occupation > 95:
    h5_niveau_global = 'CRITIQUE'
elif h5_nb_ruptures >= 1 or h5_taux_occupation > 85 or (h5_nb_alertes >= 2 and h5_nb_medecins < 5):
    h5_niveau_global = 'PREOCCUPANT'
else:
    h5_niveau_global = 'SATISFAISANT'

# --- COMPTEUR NATIONAL ---
nb_hopitaux_critiques = 0
if h1_niveau_global == 'CRITIQUE':
    nb_hopitaux_critiques += 1
if h2_niveau_global == 'CRITIQUE':
    nb_hopitaux_critiques += 1
if h3_niveau_global == 'CRITIQUE':
    nb_hopitaux_critiques += 1
if h4_niveau_global == 'CRITIQUE':
    nb_hopitaux_critiques += 1
if h5_niveau_global == 'CRITIQUE':
    nb_hopitaux_critiques += 1

total_ruptures_nationales = h1_nb_ruptures + h2_nb_ruptures + h3_nb_ruptures + h4_nb_ruptures + h5_nb_ruptures

# --- AFFICHAGE TABLEAU DE BORD ---
print('=' * 65)
print(' TABLEAU DE BORD SANITAIRE — MINISTERE DE LA SANTE')
print(' Date : 16 janvier 2026 | Pour le Conseil des Ministres')
print('=' * 65)
print(f' {h1_nom:<25} {h1_taux_occupation}% | {h1_nb_ruptures}R + {h1_nb_alertes}A | [{h1_niveau_global}]')
print(f' {h2_nom:<25} {h2_taux_occupation}% | {h2_nb_ruptures}R + {h2_nb_alertes}A | [{h2_niveau_global}]')
print(f' {h3_nom:<25} {h3_taux_occupation}% | {h3_nb_ruptures}R + {h3_nb_alertes}A | [{h3_niveau_global}]')
print(f' {h4_nom:<25} {h4_taux_occupation}% | {h4_nb_ruptures}R + {h4_nb_alertes}A | [{h4_niveau_global}]')
print(f' {h5_nom:<25} {h5_taux_occupation}% | {h5_nb_ruptures}R + {h5_nb_alertes}A | [{h5_niveau_global}]')
print('-' * 65)
print(f' {nb_hopitaux_critiques} hopitaux sur 5 en situation CRITIQUE')
print(f' {total_ruptures_nationales} ruptures de stock identifiees a l\'echelle nationale')
print(f' RECOMMANDATION PRIORITAIRE : Mobiliser la reserve nationale PNA')
print('=' * 65)