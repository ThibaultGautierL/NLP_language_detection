Détection de langue avec scikit-learn
=====================================

Table des matières
------------------
1. À propos
2. Prérequis
3. Description du modèle
4. Exécution
5. Résultats
6. Conclusion
7. Licence

---

1. À propos
-----------
Ce projet utilise la bibliothèque scikit-learn pour construire un modèle de classification qui détecte la langue d'un texte donné.  
L'approche repose sur l'extraction de caractéristiques à l'aide de la méthode TF-IDF et l'entraînement d'un modèle de régression logistique pour effectuer des prédictions.  

---

2. Prérequis
------------
Aucun prérequis spécifique pour le système d'exploitation ou la version de Python.  

Dépendances Python :
- pandas
- scikit-learn

Les dépendances peuvent être installées avec la commande suivante :
pip install pandas scikit-learn


---

3. Description du modèle
-------------------------
### Données d'entrée
Le projet utilise un fichier CSV nommé `data_set.csv`.  
Ce fichier doit contenir deux colonnes :
1. **Text** : Les phrases ou textes à analyser.
2. **Language** : La langue associée à chaque texte (étiquettes cibles).

### Prétraitement
- Les données textuelles sont nettoyées en supprimant la ponctuation et en convertissant les caractères en minuscules.

### Extraction de caractéristiques
- Les n-grammes (de 1 à 3 caractères) sont extraits à l'aide de la méthode TF-IDF (Term Frequency-Inverse Document Frequency).

### Modèle
- Le modèle utilisé est une régression logistique implémentée avec scikit-learn.
- La pipeline inclut l'étape de vectorisation et la classification pour simplifier le flux de travail.

---

4. Exécution
------------
Étape 1 : Préparer les données  
Assurez-vous d'avoir un fichier `data_set.csv` dans le répertoire du projet avec les colonnes "Text" et "Language".

Étape 2 : Installer les dépendances  
Installez les dépendances nécessaires.

Étape 3 : Lancer le projet  
Exécutez le script Python pour entraîner le modèle et détecter la langue d'une phrase


Après l'entraînement, vous pourrez saisir une phrase pour détecter sa langue.  
Pour quitter, tapez `quitter`.

---

5. Résultats
------------
Le modèle affiche les résultats suivants :
- **Précision** : La précision est calculée en pourcentage après la prédiction sur le jeu de test.
- **Matrice de confusion** : Une matrice de confusion est générée pour analyser les performances du modèle.

---

6. Conclusion
-------------
Ce projet montre comment utiliser scikit-learn pour résoudre un problème de classification de texte avec une approche simple et efficace.  

### Améliorations possibles :
- Ajouter des données supplémentaires pour couvrir plus de langues.
- Optimiser les hyperparamètres du modèle.
- Tester d'autres algorithmes de classification pour améliorer la précision.

---

7. Licence
----------
Aucune licence spécifique n'est définie pour ce projet.


