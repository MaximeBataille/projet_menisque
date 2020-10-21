# projet_menisque



Objectif : Pr�dire la r�ussite d'une suture de m�nisque



## Environnement

1. Pandas

2. Numpy

3. Flask

4. Pickle



## - Installation



`pip install scikit-learn pandas numpy flask os pickle`



## - Organisation des dossiers

-FINAL
   - data

   - static
      - css
         - style.css

   - templates
      - index.html

   - app.py

   - ml_model.pkl

## - Fichiers
app.py : app, configuration de l'API Flask
style.css : feuille de style css
index.html : template html de l'interface
ml_model.pkl : model sauvegard� et cr�� sur Notebook KNN.ipynb


## - Lancement



Run avec la commande

`python chemin_du_fichier/app.py`
...
...Attendre quelques instants
Copier l'URL http://127.0.0.1:5000/ dans un navigateur

## - Probl�mes �ventuels

Ouvrir le fichier app.py et modifier la ligne 8
==> model = pickle.load(open('FINAL/ml_model.pkl', 'rb'))
==> Modifier le chemin 'FINAL/ml_model.pkl' par le chemin complet
	selon l'emplacement du dossier FINAL
==>Sauvegarder !!! 
