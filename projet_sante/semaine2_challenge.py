# ============================================================
# AKIENI ACADEMY — Projet Sante Publique
# Semaine 2 — Challenge : 3 Hopitaux du Pool
# ============================================================

# --- h1 Ou H&1 et h3 Signifie juste hopital 1, 2 ou 3 pour representer les 3 hopitaux du Pool. h1 = Hopital 1, h2 = Hopital 2, h3 = Hopital 3 ---

# --- HOPITAL 1 : District Kinkala ---
h1_nom = 'Hopital District Kinkala'
h1_budget = 12_500_000
h1_consultations = 1847
h1_hospitalisations = 312
h1_deces = 8
h1_lits_total = 45
h1_lits_occupes = 41
h1_medecins = 3
h1_population = 85_000

# --- HOPITAL 2 : CMS de Vindza ---
h2_nom = 'CMS de Vindza'
h2_budget = 6_800_000
h2_consultations = 923
h2_hospitalisations = 87
h2_deces = 2
h2_lits_total = 20
h2_lits_occupes = 14
h2_medecins = 1
h2_population = 42_000

# --- HOPITAL 3 : Hopital de Kindamba ---
h3_nom = 'Hopital de Kindamba'
h3_budget = 9_200_000
h3_consultations = 1234
h3_hospitalisations = 201
h3_deces = 11
h3_lits_total = 35
h3_lits_occupes = 33
h3_medecins = 2
h3_population = 67_000
# --- CALCULS HOPITAL 1 ---
h1_cout_moyen = round(h1_budget / h1_consultations, 2)
h1_taux_occupation = round(h1_lits_occupes / h1_lits_total * 100, 1)
h1_densite_medicale = round(h1_medecins / h1_population * 1000, 2)
h1_taux_mortalite = round(h1_deces / h1_hospitalisations * 100, 2)

# --- CALCULS HOPITAL 2 ---
h2_cout_moyen = round(h2_budget / h2_consultations, 2)
h2_taux_occupation = round(h2_lits_occupes / h2_lits_total * 100, 1)
h2_densite_medicale = round(h2_medecins / h2_population * 1000, 2)
h2_taux_mortalite = round(h2_deces / h2_hospitalisations * 100, 2)

# --- CALCULS HOPITAL 3 ---
h3_cout_moyen = round(h3_budget / h3_consultations, 2)
h3_taux_occupation = round(h3_lits_occupes / h3_lits_total * 100, 1)
h3_densite_medicale = round(h3_medecins / h3_population * 1000, 2)
h3_taux_mortalite = round(h3_deces / h3_hospitalisations * 100, 2)

# --- BONUS : Budget total suffisant pour 5 medecins chacun ? ---
budget_total = h1_budget + h2_budget + h3_budget
cout_5_medecins = 5 * 1_200_000 * 3  # 5 medecins x 1 200 000 x 3 hopitaux
budget_suffisant = budget_total >= cout_5_medecins
# --- AFFICHAGE RAPPORT ---
print('=' * 60)
print('  RAPPORT COMPARATIF — 3 HOPITAUX DU POOL')
print('  Demande : Dr. ELENGA Pascal, Directeur DSS')
print('=' * 60)

print(f'\n--- {h1_nom} ---')
print(f'  Cout moyen / patient : {h1_cout_moyen:,} FCFA'.replace(',', ' '))
print(f'  Taux occupation      : {h1_taux_occupation}%')
print(f'  Densite medicale     : {h1_densite_medicale} medecins / 1000 hab')
print(f'  Taux mortalite       : {h1_taux_mortalite}%')
if h1_taux_mortalite > 2 or h1_densite_medicale < 0.05:
    print(f'  ⚠ ALERTE CRITIQUE : {h1_nom} en situation critique !')

print(f'\n--- {h2_nom} ---')
print(f'  Cout moyen / patient : {h2_cout_moyen:,} FCFA'.replace(',', ' '))
print(f'  Taux occupation      : {h2_taux_occupation}%')
print(f'  Densite medicale     : {h2_densite_medicale} medecins / 1000 hab')
print(f'  Taux mortalite       : {h2_taux_mortalite}%')
if h2_taux_mortalite > 2 or h2_densite_medicale < 0.05:
    print(f'  ⚠ ALERTE CRITIQUE : {h2_nom} en situation critique !')

print(f'\n--- {h3_nom} ---')
print(f'  Cout moyen / patient : {h3_cout_moyen:,} FCFA'.replace(',', ' '))
print(f'  Taux occupation      : {h3_taux_occupation}%')
print(f'  Densite medicale     : {h3_densite_medicale} medecins / 1000 hab')
print(f'  Taux mortalite       : {h3_taux_mortalite}%')
if h3_taux_mortalite > 2 or h3_densite_medicale < 0.05:
    print(f'  ⚠ ALERTE CRITIQUE : {h3_nom} en situation critique !')

print('\n' + '=' * 60)
print('  BONUS — Budget suffisant pour 5 medecins chacun ?')
print(f'  Budget total         : {budget_total:,} FCFA'.replace(',', ' '))
print(f'  Cout 5 medecins x3   : {cout_5_medecins:,} FCFA'.replace(',', ' '))
print(f'  Suffisant            : {"OUI" if budget_suffisant else "NON"}')
print('=' * 60)