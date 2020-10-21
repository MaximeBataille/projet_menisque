#maxime
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('ml_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():



    age = request.form['age']
    int_ext = request.form['type de rupture']
    delais = request.form['delais']
    acl = request.form['acl']
    anse_seau = request.form['anse de seau']
    poids = request.form['poids']
    taille = request.form['taille']


    #conversion des réponses de type button
    dic_conversion = {'oui' : 1, 'non' : 0}
    anse_seau_bin = dic_conversion[anse_seau]
    acl_bin = dic_conversion[acl]

    dic_conversion = {'interne' : 1, 'externe' : 0}
    int_ext_bin = dic_conversion[int_ext]

    #calcul de l'imc
    poids = float(poids)
    taille = float(taille) / 100

    imc = round(poids / (taille * taille), 2)

    #features input modèle
    int_features = [age, int_ext_bin, delais, acl_bin, imc, anse_seau_bin]

    #mise en forme au bon format
    final_features = pd.DataFrame(data = int_features).T
    final_features.columns = ['age', 'int_ext', 'delay', 'ACL', 'IMC', 'new_BH']
    final_features['age'] = final_features['age'].astype('int')

    #calcul de la prédiction
    proba_prediction = model.predict_proba(final_features)

    output_proba = round(100 * proba_prediction[0][0], 1)

    return render_template('index.html', prediction_text='La suture a {} %  de chance de réussir'.format(output_proba),
        age = age,
        int_ext = int_ext,
        delais = delais, 
        acl = acl,
        anse_seau = anse_seau,
        poids = poids,
        taille = taille * 100,
        imc = imc)


if __name__ == "__main__":
    app.run(debug=True)
