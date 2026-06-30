# ============================================================
# MODULE FONDATEUR — Projet Sante Publique / Akieni Academy
# Ce fichier centralise toutes les constantes et variables metier
# Il sera enrichi chaque semaine jusqu'a S24
# ============================================================

# === SECTION A : CONSTANTES NATIONALES ET NORMES OMS ========
TAUX_EUR_FCFA = 655.957
TAUX_USD_FCFA = 600.0
SEUIL_OMS_DENSITE_MEDICALE = 2.3       # medecins pour 1000 habitants
SEUIL_OMS_COUVERTURE_VACCIN = 95.0     # pourcentage minimum OMS
SEUIL_MORTALITE_ALERTE = 2.0           # % deces / hospitalisations
SEUIL_RUPTURE_STOCK_JOURS = 30         # jours minimum de stock

DEPARTEMENTS_CONGO = [                  # 12 departements officiels
    'Brazzaville', 'Pointe-Noire', 'Bouenza', 'Cuvette',
    'Cuvette-Ouest', 'Kouilou', 'Lekoumou', 'Likouala',
    'Niari', 'Plateaux', 'Pool', 'Sangha'
]
# === SECTION B : VARIABLES DES 5 HOPITAUX ===================

# Hopital 1 — CHU de Brazzaville
h1_nom = 'CHU de Brazzaville'
h1_ville = 'Brazzaville'
h1_departement = 'Brazzaville'
h1_type = 'CHU'
h1_nb_lits = 320
h1_nb_lits_occupes = 284
h1_nb_medecins = 47
h1_nb_infirmiers = 123
h1_population_zone = 1_800_000

# Hopital 2 — Hopital General de Pointe-Noire
h2_nom = 'Hopital General de Pointe-Noire'
h2_ville = 'Pointe-Noire'
h2_departement = 'Kouilou'
h2_type = 'Hopital General'
h2_nb_lits = 180
h2_nb_lits_occupes = 143
h2_nb_medecins = 22
h2_nb_infirmiers = 58
h2_population_zone = 128_000

# Hopital 3 — Hopital de Dolisie
h3_nom = 'Hopital de Dolisie'
h3_ville = 'Dolisie'
h3_departement = 'Niari'
h3_type = 'Hopital General'
h3_nb_lits = 120
h3_nb_lits_occupes = 98
h3_nb_medecins = 15
h3_nb_infirmiers = 40
h3_population_zone = 95_000

# Hopital 4 — Hopital de District Owando
h4_nom = 'Hopital de District Owando'
h4_ville = 'Owando'
h4_departement = 'Cuvette'
h4_type = 'Hopital de District'
h4_nb_lits = 60
h4_nb_lits_occupes = 45
h4_nb_medecins = 5
h4_nb_infirmiers = 18
h4_population_zone = 72_000

# Hopital 5 — Centre de Sante de Impfondo
h5_nom = 'Centre de Sante de Impfondo'
h5_ville = 'Impfondo'
h5_departement = 'Likouala'
h5_type = 'Centre de Sante'
h5_nb_lits = 30
h5_nb_lits_occupes = 22
h5_nb_medecins = 2
h5_nb_infirmiers = 8
h5_population_zone = 45_000

# Section D : VARIABLES DES 5 MEDICAMENTS 

# Médicaments
med_h1_nom = "Paracétamol"
med_h1_quantite = 1205674
med_h1_seuil = 50
med_h1_cout = 1150

med_h2_nom = "Ibucape"
med_h2_quantite = 800578
med_h2_seuil = 40
med_h2_cout = 2500

med_h3_nom = "Morphine"
med_h3_quantite = 607235
med_h3_seuil = 30
med_h3_cout = 1485

med_h4_nom = "nifluenrine"
med_h4_quantite = 2006567
med_h4_seuil = 10
med_h4_cout = 3300

med_h5_nom = "cloraphinicole"
med_h5_quantite = 405333
med_h5_seuil = 50
med_h5_cout = 925

# Section D : KPIs calcules 

# Hopital 1 — CHU de Brazzaville

taux_occupations_h1 = h1_nb_lits_occupes / h1_nb_lits * 100
densite_medicale_h1 = h1_nb_medecins / h1_population_zone * 1000 
cout_en_euro = med_h1_cout / TAUX_EUR_FCFA
cout_en_usd = med_h1_cout / TAUX_USD_FCFA

# Hopital 2 — General de Pointe-Noire
taux_occupations_h2 = h2_nb_lits_occupes / h2_nb_lits * 100
densite_medicale_h2 = h2_nb_medecins / h2_population_zone * 1000
cout_en_euro_h2 = med_h2_cout / TAUX_EUR_FCFA
cout_en_usd_h2 = med_h2_cout / TAUX_USD_FCFA

# Hopital 3 — Hopital de Dolisie
taux_occupations_h3 = h3_nb_lits_occupes / h3_nb_lits * 100
densite_medicale_h3 = h3_nb_medecins / h3_population_zone * 1000
cout_en_euro_h3 = med_h3_cout / TAUX_EUR_FCFA
cout_en_usd_h3 = med_h3_cout / TAUX_USD_FCFA

# Hopital 4 — Hopital de District Owando
taux_occupations_h4 = h4_nb_lits_occupes / h4_nb_lits * 100
densite_medicale_h4 = h4_nb_medecins / h4_population_zone * 1000
cout_en_euro_h4 = med_h4_cout / TAUX_EUR_FCFA
cout_en_usd_h4 = med_h4_cout / TAUX_USD_FCFA

# Caculs des KPIS 
taux_occupations_h5 = h5_nb_lits_occupes / h5_nb_lits * 100
densite_medicale_h5 = h5_nb_medecins / h5_population_zone * 1000
cout_en_euro_h5 = med_h5_cout / TAUX_EUR_FCFA
cout_en_usd_h5 = med_h5_cout / TAUX_USD_FCFA

# 1 BRAZZAVILLE (1/5) Affiche des KPIs
# Rapport affiché avec f-strings 
print('='*60) 
print(f" RAPPORT DE L'HOPITAL 1 : {h1_nom} ")
print('='*60) 

print(f"Ville : {h1_ville}")
print(f"Département : {h1_departement}")
print(f"Type : {h1_type}")
print(f"Nombre de lits : {h1_nb_lits}")
print(f"Lits occupés : {h1_nb_lits_occupes}")
print(f"Taux d'occupation : {taux_occupations_h1:.2f}%")
print(f"Nombre de médecins : {h1_nb_medecins}")
print(f"Nombre d'infirmiers : {h1_nb_infirmiers}")
print(f"Ratio infirmiers/médecins : {densite_medicale_h1:.2f}")
print(f"Densité médicale : {densite_medicale_h1:.3f} médecins pour 1000 habitants")

print('_'*60) 
print(f"PRIX DE MEDICAMENT PAR DEVISE, PRODUIT : {med_h1_nom}")

print(f"Coût en FCFA : {med_h1_cout} FCFA")
print(f"Coût en euros : {cout_en_euro:.2f} €")
print(f"Coût en dollars : {cout_en_usd:.2f} $")

print('_'*60) 



# 2 POINT-NOIRE (2/5) Affiche des KPIs
# Rapport affiché avec f-strings 

print(f" RAPPORT DE L'HOPITAL 2 : {h2_nom} ")
print('='*60) 

print(f"Ville : {h2_ville}")
print(f"Département : {h2_departement}")
print(f"Type : {h2_type}")
print(f"Nombre de lits : {h2_nb_lits}")
print(f"Lits occupés : {h2_nb_lits_occupes}")
print(f"Taux d'occupation : {taux_occupations_h2:.2f}%")
print(f"Nombre de médecins : {h2_nb_medecins}")
print(f"Nombre d'infirmiers : {h2_nb_infirmiers}")
print(f"Ratio infirmiers/médecins : {densite_medicale_h2:.2f}")
print(f"Densité médicale : {densite_medicale_h2:.3f} médecins pour 1000 habitants")

print('_'*60) 
print(f"PRIX DE MEDICAMENT PAR DEVISE, PRODUIT : {med_h2_nom}")

print(f"Coût en FCFA : {med_h2_cout} FCFA")
print(f"Coût en euros : {cout_en_euro_h2:.2f} €")
print(f"Coût en dollars : {cout_en_usd_h2:.2f} $")



# 3 DOLISI (3/5) Affiche des KPIs
# Rapport affiché avec f-strings 

print('='*60) 
print(f" RAPPORT DE L'HOPITAL 3 : {h3_nom} ")
print('='*60) 

print(f"Ville : {h3_ville}")
print(f"Département : {h3_departement}")
print(f"Type : {h3_type}")
print(f"Nombre de lits : {h3_nb_lits}")
print(f"Lits occupés : {h3_nb_lits_occupes}")
print(f"Taux d'occupation : {taux_occupations_h3:.2f}%")
print(f"Nombre de médecins : {h3_nb_medecins}")
print(f"Nombre d'infirmiers : {h3_nb_infirmiers}")
print(f"Ratio infirmiers/médecins : {densite_medicale_h3:.2f}")
print(f"Densité médicale : {densite_medicale_h3:.3f} médecins pour 1000 habitants")

print('_'*60) 
print(f"PRIX DE MEDICAMENT PAR DEVISE, PRODUIT : {med_h3_nom}")

print(f"Coût en FCFA : {med_h3_cout} FCFA")
print(f"Coût en euros : {cout_en_euro_h3:.2f} €")
print(f"Coût en dollars : {cout_en_usd_h3:.2f} $")


# 4 de District Owando (4/5) Affiche des KPIs
# Rapport affiché avec f-strings 

print('='*60) 
print(f" RAPPORT DE L'HOPITAL 4 : {h4_nom} ")
print('='*60) 

print(f"Ville : {h4_ville}")
print(f"Département : {h4_departement}")
print(f"Type : {h4_type}")
print(f"Nombre de lits : {h4_nb_lits}")
print(f"Lits occupés : {h4_nb_lits_occupes}")
print(f"Taux d'occupation : {taux_occupations_h4:.2f}%")
print(f"Nombre de médecins : {h4_nb_medecins}")
print(f"Nombre d'infirmiers : {h4_nb_infirmiers}")
print(f"Ratio infirmiers/médecins : {densite_medicale_h4:.2f}")
print(f"Densité médicale : {densite_medicale_h4:.3f} médecins pour 1000 habitants")

print('_'*60) 
print(f"PRIX DE MEDICAMENT PAR DEVISE, PRODUIT : {med_h4_nom}")

print(f"Coût en FCFA : {med_h4_cout} FCFA")
print(f"Coût en euros : {cout_en_euro_h4:.2f} €")
print(f"Coût en dollars : {cout_en_usd_h4:.2f} $")


# 5 Centre de Sante de Impfondo (5/5) Affiche des KPIs
# Rapport affiché avec f-strings  

print('='*60) 
print(f" RAPPORT DE L'HOPITAL 5 : {h5_nom} ")
print('='*60) 

print(f"Ville : {h5_ville}")
print(f"Département : {h5_departement}")
print(f"Type : {h5_type}")
print(f"Nombre de lits : {h5_nb_lits}")
print(f"Lits occupés : {h5_nb_lits_occupes}")
print(f"Taux d'occupation : {taux_occupations_h5:.2f}%")
print(f"Nombre de médecins : {h5_nb_medecins}")
print(f"Nombre d'infirmiers : {h5_nb_infirmiers}")
print(f"Ratio infirmiers/médecins : {densite_medicale_h5:.2f}")
print(f"Densité médicale : {densite_medicale_h5:.3f} médecins pour 1000 habitants")

print('_'*60) 
print(f"PRIX DE MEDICAMENT PAR DEVISE, PRODUIT : {med_h5_nom}")

print(f"Coût en FCFA : {med_h5_cout} FCFA")
print(f"Coût en euros : {cout_en_euro_h5:.2f} €")
print(f"Coût en dollars : {cout_en_usd_h5:.2f} $")


# SECTION F : CLASSIFICATION STATUT STOCKS MEDICAMENTS (S3) 

# Medicament 1 — Paracétamol
if med_h1_quantite <= med_h1_seuil:
    med_h1_statut = 'RUPTURE CRITIQUE'
elif med_h1_quantite <= med_h1_seuil * 1.5:
    med_h1_statut = 'ALERTE STOCK'
elif med_h1_quantite <= med_h1_seuil * 2.0:
    med_h1_statut = 'STOCK LIMITE'
else:
    med_h1_statut = 'STOCK NORMAL'

# Medicament 2 — Ibucape
if med_h2_quantite <= med_h2_seuil:
    med_h2_statut = 'RUPTURE CRITIQUE'
elif med_h2_quantite <= med_h2_seuil * 1.5:
    med_h2_statut = 'ALERTE STOCK'
elif med_h2_quantite <= med_h2_seuil * 2.0:
    med_h2_statut = 'STOCK LIMITE'
else:
    med_h2_statut = 'STOCK NORMAL'

# Medicament 3 — Morphine
if med_h3_quantite <= med_h3_seuil:
    med_h3_statut = 'RUPTURE CRITIQUE'
elif med_h3_quantite <= med_h3_seuil * 1.5:
    med_h3_statut = 'ALERTE STOCK'
elif med_h3_quantite <= med_h3_seuil * 2.0:
    med_h3_statut = 'STOCK LIMITE'
else:
    med_h3_statut = 'STOCK NORMAL'

# Medicament 4 — nifluenrine
if med_h4_quantite <= med_h4_seuil:
    med_h4_statut = 'RUPTURE CRITIQUE'
elif med_h4_quantite <= med_h4_seuil * 1.5:
    med_h4_statut = 'ALERTE STOCK'
elif med_h4_quantite <= med_h4_seuil * 2.0:
    med_h4_statut = 'STOCK LIMITE'
else:
    med_h4_statut = 'STOCK NORMAL'

# Medicament 5 — cloraphinicole
if med_h5_quantite <= med_h5_seuil:
    med_h5_statut = 'RUPTURE CRITIQUE'
elif med_h5_quantite <= med_h5_seuil * 1.5:
    med_h5_statut = 'ALERTE STOCK'
elif med_h5_quantite <= med_h5_seuil * 2.0:
    med_h5_statut = 'STOCK LIMITE'
else:
    med_h5_statut = 'STOCK NORMAL'


# === SECTION G : CLASSIFICATION OCCUPATION HOPITAUX (S3) ===

if taux_occupations_h1 > 95:
    h1_niveau_occupation = 'ALERTE CRITIQUE'
elif taux_occupations_h1 > 85:
    h1_niveau_occupation = 'ALERTE ELEVEE'
elif taux_occupations_h1 > 70:
    h1_niveau_occupation = 'SITUATION OPTIMALE'
else:
    h1_niveau_occupation = 'SOUS-UTILISATION'

if taux_occupations_h2 > 95:
    h2_niveau_occupation = 'ALERTE CRITIQUE'
elif taux_occupations_h2 > 85:
    h2_niveau_occupation = 'ALERTE ELEVEE'
elif taux_occupations_h2 > 70:
    h2_niveau_occupation = 'SITUATION OPTIMALE'
else:
    h2_niveau_occupation = 'SOUS-UTILISATION'

if taux_occupations_h3 > 95:
    h3_niveau_occupation = 'ALERTE CRITIQUE'
elif taux_occupations_h3 > 85:
    h3_niveau_occupation = 'ALERTE ELEVEE'
elif taux_occupations_h3 > 70:
    h3_niveau_occupation = 'SITUATION OPTIMALE'
else:
    h3_niveau_occupation = 'SOUS-UTILISATION'

if taux_occupations_h4 > 95:
    h4_niveau_occupation = 'ALERTE CRITIQUE'
elif taux_occupations_h4 > 85:
    h4_niveau_occupation = 'ALERTE ELEVEE'
elif taux_occupations_h4 > 70:
    h4_niveau_occupation = 'SITUATION OPTIMALE'
else:
    h4_niveau_occupation = 'SOUS-UTILISATION'

if taux_occupations_h5 > 95:
    h5_niveau_occupation = 'ALERTE CRITIQUE'
elif taux_occupations_h5 > 85:
    h5_niveau_occupation = 'ALERTE ELEVEE'
elif taux_occupations_h5 > 70:
    h5_niveau_occupation = 'SITUATION OPTIMALE'
else:
    h5_niveau_occupation = 'SOUS-UTILISATION'


# === SECTION H : CLASSIFICATION COUVERTURE VACCINALE (S3) ===

dept1_nom = 'Brazzaville'
dept1_population_cible = 450000
dept1_personnes_vaccinees = 418500
dept1_taux = dept1_personnes_vaccinees / dept1_population_cible * 100

dept2_nom = 'Pointe-Noire'
dept2_population_cible = 280000
dept2_personnes_vaccinees = 229600
dept2_taux = dept2_personnes_vaccinees / dept2_population_cible * 100

dept3_nom = 'Pool'
dept3_population_cible = 120000
dept3_personnes_vaccinees = 54000
dept3_taux = dept3_personnes_vaccinees / dept3_population_cible * 100

dept4_nom = 'Sangha'
dept4_population_cible = 85000
dept4_personnes_vaccinees = 35700
dept4_taux = dept4_personnes_vaccinees / dept4_population_cible * 100

if dept1_taux < 50:
    dept1_statut = 'ZONE CRITIQUE'
elif dept1_taux < 80:
    dept1_statut = 'ZONE A RISQUE'
elif dept1_taux < SEUIL_OMS_COUVERTURE_VACCIN:
    dept1_statut = 'ZONE INSUFFISANTE'
else:
    dept1_statut = 'ZONE OMS CONFORME'

if dept2_taux < 50:
    dept2_statut = 'ZONE CRITIQUE'
elif dept2_taux < 80:
    dept2_statut = 'ZONE A RISQUE'
elif dept2_taux < SEUIL_OMS_COUVERTURE_VACCIN:
    dept2_statut = 'ZONE INSUFFISANTE'
else:
    dept2_statut = 'ZONE OMS CONFORME'

if dept3_taux < 50:
    dept3_statut = 'ZONE CRITIQUE'
elif dept3_taux < 80:
    dept3_statut = 'ZONE A RISQUE'
elif dept3_taux < SEUIL_OMS_COUVERTURE_VACCIN:
    dept3_statut = 'ZONE INSUFFISANTE'
else:
    dept3_statut = 'ZONE OMS CONFORME'

if dept4_taux < 50:
    dept4_statut = 'ZONE CRITIQUE'
elif dept4_taux < 80:
    dept4_statut = 'ZONE A RISQUE'
elif dept4_taux < SEUIL_OMS_COUVERTURE_VACCIN:
    dept4_statut = 'ZONE INSUFFISANTE'
else:
    dept4_statut = 'ZONE OMS CONFORME'


# === SECTION I : RAPPORT D'ETAT GLOBAL AVEC ALERTES (S3) ===

nb_ruptures_medicaments = 0
if med_h1_statut == 'RUPTURE CRITIQUE':
    nb_ruptures_medicaments += 1
if med_h2_statut == 'RUPTURE CRITIQUE':
    nb_ruptures_medicaments += 1
if med_h3_statut == 'RUPTURE CRITIQUE':
    nb_ruptures_medicaments += 1
if med_h4_statut == 'RUPTURE CRITIQUE':
    nb_ruptures_medicaments += 1
if med_h5_statut == 'RUPTURE CRITIQUE':
    nb_ruptures_medicaments += 1

nb_hopitaux_saturation = 0
if h1_niveau_occupation == 'ALERTE CRITIQUE':
    nb_hopitaux_saturation += 1
if h2_niveau_occupation == 'ALERTE CRITIQUE':
    nb_hopitaux_saturation += 1
if h3_niveau_occupation == 'ALERTE CRITIQUE':
    nb_hopitaux_saturation += 1
if h4_niveau_occupation == 'ALERTE CRITIQUE':
    nb_hopitaux_saturation += 1
if h5_niveau_occupation == 'ALERTE CRITIQUE':
    nb_hopitaux_saturation += 1

nb_zones_critiques = 0
if dept1_statut == 'ZONE CRITIQUE':
    nb_zones_critiques += 1
if dept2_statut == 'ZONE CRITIQUE':
    nb_zones_critiques += 1
if dept3_statut == 'ZONE CRITIQUE':
    nb_zones_critiques += 1
if dept4_statut == 'ZONE CRITIQUE':
    nb_zones_critiques += 1

print('='*60)
print(' RAPPORT D\'ETAT GLOBAL — SECTION S3')
print('='*60)
print(f' Medicaments en RUPTURE CRITIQUE : {nb_ruptures_medicaments}')
print(f' Hopitaux en ALERTE CRITIQUE     : {nb_hopitaux_saturation}')
print(f' Zones vaccinales CRITIQUES      : {nb_zones_critiques}')
print('-'*60)
print(f' {dept1_nom} : {dept1_taux:.1f}% — {dept1_statut}')
print(f' {dept2_nom} : {dept2_taux:.1f}% — {dept2_statut}')
print(f' {dept3_nom} : {dept3_taux:.1f}% — {dept3_statut}')
print(f' {dept4_nom} : {dept4_taux:.1f}% — {dept4_statut}')
print('='*60)