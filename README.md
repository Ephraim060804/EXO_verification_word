# EXO_verification_word


# Vérification de mot avec Colorama et PyFiglet

Ce projet est un petit programme interactif en Python qui utilise les bibliothèques **Colorama** et **PyFiglet** pour rendre l'expérience utilisateur plus visuelle et agréable dans le terminal.  
Il permet de saisir du texte, vérifier certaines conditions, et proposer un menu pour continuer ou quitter.

---

## 🎨 Fonctionnalités

- Affichage stylisé du titre avec **PyFiglet** (ASCII art).
- Utilisation de **Colorama** pour colorer les textes dans le terminal :
  - Bleu pour les invites de saisie.
  - Vert pour les réponses correctes.
  - Rouge pour les erreurs ou mauvaises réponses.
  - Jaune pour le menu.
- Vérification simple du mot **"bonjour"** :
  - Si l’utilisateur écrit "bonjour " → réponse **ok**.
  - Si l’utilisateur écrit "BONJOUR" (en majuscules) → réponse **C'est correcte**.
  - Sinon → réponse **non**.
- Menu interactif :
  - **1. Continuer** → relance la vérification.
  - **2. Quitter** → affiche "Au revoir" et termine le programme.
- Gestion des erreurs avec `try/except` pour éviter les plantages lors des saisies invalides.

---

## 📦 Installation

1. Clonez le dépôt :
   ```bash
   git clone https://github.com/Ephraim060804/EXO_verification_word.git
   cd EXO_verification_word
