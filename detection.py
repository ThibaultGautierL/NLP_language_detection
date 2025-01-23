import string
import pandas as pd
import numpy as np
import re
# import marplotlib.pyplot as plt
# import seaborn as sns


#Importer le dataset
df = pd.read_csv('data_set.csv')
print(df.head(5))

#Traitement de la donnée retirer la ponctuation et les majs
def remove_ponctuation(text):
    for pon in string.punctuation:
        text = text.replace(pon, "")
    text = text.lower()
    return(text)

df['Text'] = df['Text'].apply(remove_ponctuation)

print(df.head(5))
