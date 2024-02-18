<h1 align="center">Projet NSI de Cryptologie</h1></p>

<p align="center"> <img src="https://github.com/Grogny/NSI-Cryptologie/blob/main/NSI_Cryptologie_logo.png"></p>


<p align="center"> <strong>NSI Cryptologie</strong> est un projet collaboratif à 3 : <a href="https://github.com/Fare-spec"> Fare-spec </a>, <a href="https://github.com/YottGG"> YottGG </a> et <a href="https://github.com/Grogny"> Grogny </a>. Qui permet de chiffrer et de déchiffrer un message en <strong>XOR</strong>, <strong>Hill</strong> et en <strong>RSA</strong> !</p>


<h2> Unpeu Plus Sur Notre Sujet : </h2>

### Qu'est ce que la cryptologie ?

Du grec kryptos (caché) et logos (science), « cryptologie » signifie littéralement science du secret et a pour objet de cacher les informations d'un message. Elle englobe la cryptographie : l'écriture secrète, et la cryptanalyse :  l'analyse de la cryptographie.

©futura-sciences.com

---

### Cryptographie et Cryptanalyse

La cryptographie est une des disciplines de la cryptologie s'attachant à protéger des messages (assurant confidentialité, authenticité et intégrité) en s'aidant souvent de secrets ou clés.

La cryptographie se scinde en deux parties nettement différenciées :

- d'une part la cryptographie à clef secrète, encore appelée symétrique ou bien classique.
- d'autre part la cryptographie à clef publique, dite également asymétrique ou moderne.

La cryptanalyse est la branche de la cryptologie qui étudie la manière de casser des codes et des cryptosystèmes. Elle développe des techniques pour casser les systèmes cryptographiques

©Wikipedia, ©developer.mozilla.org

---

### XOR, HILL et RSA

La fonction OU exclusif, souvent appelée <strong>XOR</strong> (e<strong>X</strong>clusive <strong>OR</strong>), est un operateur logique À deux opérandes, qui peuvent avoir chacun la valeur VRAI ou FAUX. Son symbole est traditionnellement un signe plus dans un cercle : « ⊕ ». La méthode de chiffrement <strong>XOR</strong> est symétrique.

En cryptographie symétrique, le <strong>chiffrement de Hill</strong> est un modèle simple d'extension du chiffrement affine à un bloc. Ce système étudié par Lester S. Hill, utilise les propriétés de l'arithmétique modulaire et des matrices.

Le chiffrement <strong>RSA</strong> (nommé par les initiales de ses trois inventeurs : Ronald <strong>R</strong>ivest, Adi <strong>S</strong>hamir et Leonard <strong>A</strong>dleman), est un algorithme de cryptographie asymétrique, très utilisé dans le commerce électronique, et plus généralement pour échanger des données confidentielles sur internet.

©Wikipedia

<h2> Notre Programme : </h2>

### Projet et Objectif

Notre projet est donc un projet de cryptologie dans lequel nous devons coder un programme en [Python](https://github.com/python) permettant de Crypter et Décrypter un message avec 3 méthode différentes (En l'occurence nous avons choisi <strong>XOR</strong>, <strong>HILL</strong> et <strong>RSA</strong>).

---

### Réalisation

Le code est reparti en 3 parties :

- Fare-spec / Elouan : Chiffrement XOR
- Grogny / Alexis : Chiffrement de Hill
- YottGG / Eliott : RSA

Chacun des collaborateurs à coder deux fonctions. Une fonction permettant de crypter les messages (Cryptographie) et une fonction permettant de décrypter les messages. Par la suite ces 6 fonctions ont été rassemblées dans un seul programme qui permet de répondre à l'objectif demandé.

Ce programme se présente sous la forme d'une interface graphique réalisée avec Tkinter dans laquel nous devons choisir notre méthode de chiffrement, une clé (ou plusieurs dans le cas de RSA), puis chiffrer / déchiffrer un message.

---

### Utilisation 

<strong>Veuillez suivre les instructions suivantes : </strong>

Dans un terminal,

Cloner le repository
```bash
git clone https://github.com/Grogny/NSI-Cryptologie
```

---
Se rendre dans le repository
```bash
cd NSI-Cryptologie
```

---
Se rendre dans le fichier qui contient le code
```bash
cd code
```

---

Installer les modules nécessaires au programme
```bash
pip install -r requirements.txt
```

---

S'amuser en utilisant notre programme :)
```bash
python3 main.py
```
---
### Modules utilisés

- math
- [NumPy](https://github.com/numpy)
- random
- Tkinter

---
