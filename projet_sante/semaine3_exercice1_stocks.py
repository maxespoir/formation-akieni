# ============================================================
# AKIENI ACADEMY — Projet Santé Publique
# Semaine 3 — Exercice 1 : Classification Stocks Médicaments
# ============================================================

# --- DONNÉES : Variables médicaments (S2 réutilisées) ---
m1_nom           = 'Artemether-Lumefantrine'
m1_stock         = 3200
m1_seuil_rupture = 2000
m1_cout_unitaire = 250   # FCFA par unité

m2_nom           = 'Amoxicilline 500mg'
m2_stock         = 950
m2_seuil_rupture = 800
m2_cout_unitaire = 100   # FCFA par unité

m3_nom           = 'Paracetamol 500mg'
m3_stock         = 12400
m3_seuil_rupture = 3000
m3_cout_unitaire = 50    # FCFA par unité

m4_nom           = 'SRO (sachets)'
m4_stock         = 4200
m4_seuil_rupture = 5000
m4_cout_unitaire = 75    # FCFA par unité

m5_nom           = 'Vaccin DTP-HepB-Hib'
m5_stock         = 820
m5_seuil_rupture = 1000
m5_cout_unitaire = 500   # FCFA par unité

# --- FONCTION DE CLASSIFICATION ---
def classer_stock(stock, seuil):
    if stock <= seuil:
        return "RUPTURE CRITIQUE", "[ROUGE]", "Alerte immédiate PNA — commande express sous 24h"
    elif stock <= seuil * 1.5:
        return "ALERTE STOCK", "[ORANGE]", "Commande urgente à déclencher sous 72h"
    elif stock <= seuil * 2.0:
        return "STOCK LIMITE", "[JAUNE]", "Surveillance renforcée — planifier commande"
    else:
        return "STOCK NORMAL", "[VERT]", "Situation normale — suivi standard"

# --- CLASSIFICATION DES 5 MÉDICAMENTS ---
m1_statut, m1_couleur, m1_action = classer_stock(m1_stock, m1_seuil_rupture)
m2_statut, m2_couleur, m2_action = classer_stock(m2_stock, m2_seuil_rupture)
m3_statut, m3_couleur, m3_action = classer_stock(m3_stock, m3_seuil_rupture)
m4_statut, m4_couleur, m4_action = classer_stock(m4_stock, m4_seuil_rupture)
m5_statut, m5_couleur, m5_action = classer_stock(m5_stock, m5_seuil_rupture)

# --- RAPPORT FINAL (sans utiliser les coûts pour rester fidèle à l'exercice) ---
print("=" * 65)
print("  RAPPORT DE STOCK — PHARMACIE NATIONALE D'APPROVISIONNEMENT")
print("  Date : 15 janvier 2026")
print("=" * 65)

for nom, stock, seuil, statut, couleur, action in [
    (m1_nom, m1_stock, m1_seuil_rupture, m1_statut, m1_couleur, m1_action),
    (m2_nom, m2_stock, m2_seuil_rupture, m2_statut, m2_couleur, m2_action),
    (m3_nom, m3_stock, m3_seuil_rupture, m3_statut, m3_couleur, m3_action),
    (m4_nom, m4_stock, m4_seuil_rupture, m4_statut, m4_couleur, m4_action),
    (m5_nom, m5_stock, m5_seuil_rupture, m5_statut, m5_couleur, m5_action),
]:
    print(f"  {couleur} {nom}")
    print(f"      Stock : {stock} unités | Seuil rupture : {seuil}")
    print(f"      Statut : {statut}")
    print(f"      Action : {action}")
    print("-" * 65)

print("=" * 65)
print( "ALERTE PRIORITAIRE : 2 medicaments en RUPTURE CRITIQUE !! \n  Transmettre immediatement au Dr. MOUKALA (PNA)" )



print("=" * 65)
