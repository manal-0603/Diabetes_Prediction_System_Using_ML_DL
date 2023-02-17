# **<center><font style="color:rgb(100,109,254)">Diabetes Prediction Using Machine learning And Deep Learning</font> </center>**

<center>
<img src='https://www.cdc.gov/diabetes/images/library/spotlights/diabetes-stats-report-724px.png?_=42420' with="100%"></center>

## Introduction

Le diabète est une maladie chronique caractérisée par une glycémie élevée qui peut causer des complications graves telles que des maladies cardiovasculaires, des lésions rénales, des troubles de la vue, etc. Dans le monde entier, le nombre de personnes atteintes de diabète augmente, ce qui rend la détection précoce de la maladie plus importante que jamais.

C'est là que les algorithmes de machine learning et de deep learning peuvent être utiles. Ces approches d'apprentissage automatique peuvent être utilisées pour analyser de grandes quantités de données de santé et identifier les caractéristiques clés qui indiquent une probabilité accrue de développer le diabète. Ces caractéristiques peuvent être utilisées pour créer un modèle de prédiction qui peut évaluer la probabilité qu'une personne soit atteinte de diabète.

Le projet Diabetes_Prediction_System_Using_ML_DeepLearning utilise les algorithmes de machine learning et de deep learning pour prédire si un utilisateur est diabétique ou non en fonction de diverses caractéristiques. Le modèle de prédiction est créé à partir de données de patients atteints de diabète, analysées à l'aide de différentes techniques d'apprentissage automatique. Les résultats sont ensuite utilisés pour créer une interface utilisateur qui permet à l'utilisateur de tester lui-même s'il est diabétique ou non.

Ce projet est un exemple de la façon dont la technologie peut être utilisée pour aider à détecter les maladies chroniques comme le diabète. En utilisant les algorithmes de machine learning et de deep learning, nous pouvons créer des modèles de prédiction qui peuvent aider les professionnels de la santé à identifier les patients à risque et à leur fournir des soins préventifs pour prévenir les complications de la maladie.

Le projet comporte deux parties distinctes : la première utilise les algorithmes de machine learning pour effectuer les prédictions, tandis que la seconde utilise le deep learning avec Keras.

## Partie 1 : Algorithmes de machine learning

Dans la première partie du projet, nous avons suivi les étapes suivantes :

1. Téléchargement des données
2. Analyse exploratoire des données (EDA)
3. Visualisation des données
4. Standardisation des données
5. Division des données en ensembles d'apprentissage et de test
6. Mise en œuvre de l'approche Random Forest
7. Mise en œuvre de l'approche k-nearest neighbors
8. Mise en œuvre de l'approche Support Vector Machine
9. Test du modèle le plus performant

## Partie 2 : Interface utilisateur en Deep Learning

La deuxième partie du projet implique la création d'une interface utilisateur à l'aide de la bibliothèque customTkinter. Les étapes suivantes ont été suivies :

1. Chargement et préparation des données
2. Préparation de l'ensemble de données avant la création du modèle
3. Création du modèle Deep Learning
4. Compilation du modèle en spécifiant la fonction de perte, l'optimiseur et les métriques à utiliser
5. Entraînement du modèle
6. Évaluation des performances du modèle en utilisant les données de test et en comparant les prédictions avec les vraies valeurs
7. Utilisation du modèle préparé et affichage de son diagramme à l'aide de la fonction plot_model
8. Compilation du modèle à nouveau en utilisant le paramètre validation_split
9. Analyse visuelle des performances du modèle à l'aide de la bibliothèque Matplotlib
10. Prédiction sur les données de test
11. Optimisation des hyperparamètres

Le code source de l'application est disponible dans ce dépôt Github, ainsi que les données utilisées pour entraîner les modèles.

## **Aperçu du test de l'application**

![screenshot](project_diabets.gif)
