import tkinter as tk

def addition():
    try:
        a = float(entrer1.get())
        b = float(entrer2.get())
        result_label.config(text=f"Résultat : {a + b}")
    except ValueError:
        result_label.config(text="Erreur : tape des nombres valides.")

def soustraction():
    try:
        a = float(entrer1.get())
        b = float(entrer2.get())
        result_label.config(text=f"Résultat : {a - b}")
    except ValueError:
        result_label.config(text="Erreur : tape des nombres valides.")

def multiplication():
    try:
        a = float(entrer1.get())
        b = float(entrer2.get())
        result_label.config(text=f"Résultat : {a * b}")
    except ValueError:
        result_label.config(text="Erreur : tape des nombres valides.")

def division():
    try:
        a = float(entrer1.get())
        b = float(entrer2.get())
        if b == 0:
            result_label.config(text="Erreur : division par zéro.")
        else:
            result_label.config(text=f"Résultat : {a / b}")
    except ValueError:
        result_label.config(text="Erreur : tape des nombres valides.")

# --- Interface graphique ---
root = tk.Tk()
root.title("Calculatrice")

# Champs de saisie
entrer1 = tk.Entry(root)
entrer2 = tk.Entry(root)
entrer1.pack()
entrer2.pack()

# Boutons pour chaque opération
tk.Button(root, text="Addition", command=addition).pack()
tk.Button(root, text="Soustraction", command=soustraction).pack()
tk.Button(root, text="Multiplication", command=multiplication).pack()
tk.Button(root, text="Division", command=division).pack()

# Résultat
result_label = tk.Label(root, text="Résultat : ")
result_label.pack()

root.mainloop()