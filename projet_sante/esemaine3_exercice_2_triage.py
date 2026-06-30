# ============================================================
# AKIENI ACADEMY — Projet Sante Publique
# Semaine 3 — Exercice 2 : Triage Patient Urgences CHU Brazzaville
# Notions S2 : variables, types, input(), f-strings, conversion
# Notions S3 : if/elif/else, conditions composees or/and/not
# ============================================================
# --- SAISIE DES DONNEES PATIENT ---
nom_patient   = input('Nom du patient : ')
age_patient   = int(input('Age (années) : '))
temperature   = float(input('Température (°C, ex: 38.4) : '))
spo2          = float(input('Saturation O2 en % (ex: 96.0) : '))
tension_syst  = int(input('Tension systolique en mmHg (ex: 135) : '))
douleur       = int(input('Douleur /10 (0=aucune, 10=insupportable) : '))

# --- VERIFICATION TEMPERATURE ---
if temperature < 35.0 or temperature > 43.0:
    print(f'ERREUR : Valeur de température impossible — vérifier la saisie à nouveau.')
    # On redemande toutes les infos
    nom_patient   = input('Nom du patient : ')
    age_patient   = int(input('Age (années) : '))
    temperature   = float(input('Température (°C, ex: 38.4) : '))
    spo2          = float(input('Saturation O2 en % (ex: 96.0) : '))
    tension_syst  = int(input('Tension systolique en mmHg (ex: 135) : '))
    douleur       = int(input('Douleur /10 (0=aucune, 10=insupportable) : '))

# --- TRIAGE (conditions composées avec or) ---
if temperature > 39.5 or spo2 < 90 or tension_syst > 180:
    niveau_triage  = '1 — IMMEDIAT'
    couleur_triage = '[ROUGE]'
    delai_pec      = '0 minute'
    action_triage  = 'Médecin présent immédiatement — code ROUGE activé'

elif temperature > 38.5 or spo2 < 94 or tension_syst > 140:
    niveau_triage  = '2 — URGENT'
    couleur_triage = '[ORANGE]'
    delai_pec      = '10 minutes'
    action_triage  = 'Appel médecin senior — prise en charge rapide'

elif temperature > 37.5 or douleur > 6:
    niveau_triage  = '3 — URGENT DIFFÉRÉ'
    couleur_triage = '[JAUNE]'
    delai_pec      = '30 minutes'
    action_triage  = 'Infirmier — surveillance et soins différés'

else:
    niveau_triage  = '4 — MOINS URGENT'
    couleur_triage = '[VERT]'
    delai_pec      = '120 minutes'
    action_triage  = "File d'attente standard — consultation programmée"


    # --- VERIFICATION SPO2 ---
if spo2 < 50.0 or spo2 > 100.0:
    print(f'ERREUR : SpO2 hors plage — vérifier le capteur')

# --- VERIFICATION TENSION ---
if tension_syst < 50 or tension_syst > 250:
    print(f'ERREUR : Tension hors plage — vérifier le brassard')

# --- VERIFICATION DOULEUR ---
if douleur < 0 or douleur > 10:
    print(f'ERREUR : Douleur doit être entre 0 et 10')

# --- VERIFICATION AGE ---
if age_patient < 0 or age_patient > 120:
    print(f'ERREUR : Age invalide — vérifier la saisie')

    # --- IDENTIFICATION DU MOTIF PRINCIPAL ---
if niveau_triage == '1 — IMMEDIAT':
    if temperature > 39.5:
        motif_principal = f'Température {temperature} C > seuil 39.5 C'
    elif spo2 < 90:
        motif_principal = f'SpO2 {spo2}% < seuil 90%'
    else:
        motif_principal = f'Tension {tension_syst} mmHg > seuil 180 mmHg'

elif niveau_triage == '2 — URGENT':
    if temperature > 38.5:
        motif_principal = f'Température {temperature} C > seuil 38.5 C'
    elif spo2 < 94:
        motif_principal = f'SpO2 {spo2}% < seuil 94%'
    else:
        motif_principal = f'Tension {tension_syst} mmHg > seuil 140 mmHg'

elif niveau_triage == '3 — URGENT DIFFÉRÉ':
    if temperature > 37.5:
        motif_principal = f'Température {temperature} C > seuil 37.5 C'
    else:
        motif_principal = f'Douleur {douleur}/10 > seuil 6'

else:
    motif_principal = 'Tous les paramètres sont dans les normes'

# --- AFFICHAGE FICHE TRIAGE ---
print()
print('=' * 55)
print(f'  RESULTAT TRIAGE — {nom_patient.upper()}')
print('=' * 55)
print(f'Âge         : {age_patient} ans')
print(f'Température : {temperature} °C')
print(f'SpO2        : {spo2} %')
print(f'Tension     : {tension_syst} mmHg')
print(f'Douleur     : {douleur}/10')
print('-' * 55)
print(f'Niveau      : {niveau_triage}')
print(f'Couleur     : {couleur_triage}')
print(f'Délai PEC   : {delai_pec}')
print(f'Action      : {action_triage}')
print('=' * 55)
print(f'  Motif principal : {motif_principal}')