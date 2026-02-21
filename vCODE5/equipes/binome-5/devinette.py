# ============================================================
#  Projet        : Jeux de devinette de nombre mistere
#  Version       : 2.0
#  Description   : Jeux de devinette utilisant tkinter pour fournir un GUI a l'user.
#  Auteurs       : Heritier ADAKANOU & sophos
#  Date          : 2/18/2026
# ============================================================



import random
import tkinter as tk
from tkinter import messagebox

fenetre = tk.Tk()
fenetre.title("Jeu du Nombre Mystère")
fenetre.geometry("800x800")
fenetre.config(bg="white")

sysNumber = random.randint(0, 100)
max_attempts = 7
attempts_left = max_attempts
user_name = ""

print(sysNumber)

def register_user(event=None):
    global user_name
    user_name = entry_name.get()
    if user_name.strip() == "":
        messagebox.showerror("Erreur", "Veuillez entrer un nom.") # box d'erreur .......
    else:
        register_frame.pack_forget() # forget .......
        game_frame.pack(fill="both", expand=True)
        systemResponse.config(
            text=f"Bienvenue {user_name} !\n"
                 f"Le système a choisi un nombre entre 0 et 100.\n"
                 f"Vous avez {max_attempts} chances pour le deviner."
        )
        entry_guess.focus_set() # focuss ......

register_frame = tk.Frame(fenetre, bg="white")
register_frame.pack(fill="both", expand=True)

tk.Label(register_frame, text="Inscription", font=("Poppins", 20, "bold"), bg="white").pack(pady=20)
tk.Label(register_frame, text="Entrez votre nom :", bg="white").pack()

entry_name = tk.Entry(register_frame, font=("Poppins", 14))
entry_name.pack(pady=10)

tk.Button(register_frame, text="Commencer", command=register_user, bg="blue", fg="white").pack(pady=20)

entry_name.bind("<Return>", register_user) # le bind .........

game_frame = tk.Frame(fenetre, bg="white")

systemResponse = tk.Label(game_frame, bg="white", font=("Poppins", 12))
systemResponse.pack(pady=20)

entry_guess = tk.Entry(game_frame, font=("Poppins", 14))
entry_guess.pack(pady=10)

def verifyNumber(event=None):
    global attempts_left
    try:
        user_response = int(entry_guess.get())
    except ValueError:
        systemResponse.config(text="Veuillez entrer un nombre valide.")
        return

    if attempts_left > 0:
        if user_response == sysNumber:
            systemResponse.config(text=f"🎉 Bravo {user_name} ! Vous avez trouvé le nombre mystère !")
            button.config(state="disabled")
        else:
            attempts_left -= 1
            if user_response < sysNumber:
                systemResponse.config(text=f"{user_name}, votre nombre est inférieur.\nChances restantes : {attempts_left}")
            else:
                systemResponse.config(text=f"{user_name}, votre nombre est supérieur.\nChances restantes : {attempts_left}")

            if attempts_left == 0:
                systemResponse.config(text=f"Désolé {user_name}, vous avez perdu.\nLe nombre mystère était {sysNumber}.")
                button.config(state="disabled")
    else:
        systemResponse.config(text="Partie terminée. Relancez pour rejouer.")
        button.config(state="disabled") # desactivation .........

button = tk.Button(
    game_frame,
    text="Soumettre",
    command=verifyNumber,
    bg="green",
    fg="white",
    font=("Poppins", 16, "bold"),
    padx=10,
    pady=5
)
button.pack(pady=20)

entry_guess.bind("<Return>", verifyNumber)

fenetre.mainloop()
