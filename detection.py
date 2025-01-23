import string
import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn import feature_extraction
from sklearn import pipeline
from sklearn import linear_model
from sklearn import metrics


#Importer le dataset
df = pd.read_csv('data_set.csv')
# print(df.head(5))

#Traitement de la donnée retirer la ponctuation et les majs
def remove_ponctuation(text):
    for pon in string.punctuation:
        text = text.replace(pon, "")
    text = text.lower()
    return(text)

df['Text'] = df['Text'].apply(remove_ponctuation)

# print(df.head(5))

X = df.iloc[:,0]
Y = df.iloc[:,1]

#0,3% pour les resultats et ,7% pour l'entrainement
X_traindata, X_testdata, Y_traindata, Y_testdata = train_test_split(X, Y, test_size = 0.4)

#Prend du unigramme au trigramme
vector= feature_extraction.text.TfidfVectorizer(ngram_range=(1,3), analyzer= 'char')

model_pipe = pipeline.Pipeline([('vector', vector), ('clf', linear_model.LogisticRegression())])
model_pipe.fit(X_traindata, Y_traindata)

predicted_value = model_pipe.predict(X_testdata)
print(f"{metrics.accuracy_score(Y_testdata, predicted_value) * 100:.2f} %")
