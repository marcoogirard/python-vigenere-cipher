# 🔐 Vigenère Cipher – Encryption & Decryption

## 📌 Description

Implémentation from scratch de l'algorithme de chiffrement de Vigenère en Python.  
Le programme permet de chiffrer ou déchiffrer n'importe quel message texte à partir d'une clé personnalisée.

---

## ⚙️ Comment ça marche

Le chiffrement de Vigenère est une méthode de chiffrement par substitution polyalphabétique. Chaque lettre du message est décalée dans l'alphabet selon la lettre correspondante de la clé, qui se répète en boucle sur toute la longueur du message.

**Exemple :**
```
Message  : hello
Clé      : key
Résultat : rijvs
```

---

## 🚀 Utilisation

```bash
python encryption.py
```

Le programme propose ensuite un menu interactif :

```
=== Vigenère Cipher ===
1. Encrypt a message
2. Decrypt a message

Choose an option (1 or 2): 1
Enter your message: hello world
Enter your key: happycoding

Original message : hello world
Key              : happycoding
Encrypted text   : omwlq tlvnd
```

---

## 🛠️ Stack technique

- **Python 3** – Aucune librairie externe requise

---

## 📄 Licence

Projet personnel – Usage libre pour inspiration ou adaptation.
