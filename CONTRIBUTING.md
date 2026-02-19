# Guide de contribution » vCODE-c2p

Ce document explique comment soumettre ton travail dans ce repo en tant que membre actif de C2P.

---

## ▸ Avant de commencer

```
● Assure-toi d'etre dans le bon dossier de session : vCODE[N]/equipes/binome-[X]/
● Ne modifie jamais le travail d'un autre binome
● Ne pousse pas de fichiers inutiles (voir section "Ce qu'il ne faut pas pousser")
```

---

## ▸ Structure d'un depot de session

Ton travail doit aller uniquement dans :

```
vCODE[N]/
└── equipes/
    └── binome-[X]/
        ├── index.html       (ou main.py, Main.java, etc.)
        ├── style.css 
        └── ...
```

---

## ▸ Conventions de nommage

```
● Dossiers       → en minuscules avec tirets    : binome-1, mon-projet
● Fichiers       → en minuscules avec tirets    : index.html, calculatrice.py
● Commits        → format strict (voir ci-dessous)
```

---

## ▸ Format des commits

Respecte toujours ce format :

```
vCODE[N] | binome-[X] : description courte

Exemples :
  vCODE5 | binome-1 : ajout de la fonction de tri
  vCODE5 | binome-2 : correction du bug d'affichage
  vCODE5 | binome-1 : solution finale
```

---

## ▸ Etapes pour soumettre son code

```bash
# 1. Clone le repo (une seule fois)
git clone https://github.com/Paskod121/vCODEc2p.git
cd vCODEc2p

# 2. Va dans ton dossier de binome
cd vCODE[N]/equipes/binome-[X]

# 3. Ajoute tes fichiers
git add .

# 4. Fais un commit avec le bon format
git commit -m "vCODE5 | binome-1 : solution finale"

# 5. Pousse
git push origin main
```

---

## ▸ Pull Request 

```
1. Pousse ta branche
2. Va sur GitHub → "Compare & pull request"
3. Titre    : vCODE[N] | binome-[X] : description
4. Description : explique brievement ce que tu as fait
5. Assigne le PR a @Paskod121
```

---

## ▸ Ce qu'il ne faut pas pousser

```
▸ node_modules/
▸ .env
▸ fichiers de cache (.DS_Store, Thumbs.db, __pycache__)
▸ fichiers de configuration locaux (.vscode/settings.json)
▸ fichiers de build (/dist, /build, /out)
```

Ajoute un fichier `.gitignore` dans ton dossier si necessaire.

---

## ▸ En cas de probleme

Pose ta question directement dans le groupe WhatsApp de la communaute.

→ https://chat.whatsapp.com/GNtDfxG6SzEHmDXRpovN3m

---

<div align="center">
<sub>Code Premier Pas (C2P) &nbsp;»&nbsp; Lome, Togo</sub>
</div>