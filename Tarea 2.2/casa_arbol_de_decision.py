# -*- coding: utf-8 -*-
"""casa arbol de decision.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1zjdCEnJUrZ-n_ghS93KsHH9HKo6u--mM
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor, plot_tree
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
import seaborn as sb
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler

dfcasas = pd.read_csv('./housing.csv')
dfcasas.head()

dfcasas.hist(figsize=(10,10), bins=50, edgecolor='red')
plt.show()

dfcasas.dropna(subset=['total_bedrooms'], inplace=True)
dfcasas['housing_median_age'] = np.minimum(dfcasas['housing_median_age'], 50)
dfcasas['median_house_value'] = np.minimum(dfcasas['median_house_value'], 500000)
dfcasas['median_income'] = np.minimum(dfcasas['median_income'], 15)

dfcasas = pd.get_dummies(dfcasas, columns=['ocean_proximity'], drop_first=True)

# Características adicionales
dfcasas['rooms_per_household'] = dfcasas['total_rooms'] / dfcasas['households']
dfcasas['bedrooms_per_room'] = dfcasas['total_bedrooms'] / dfcasas['total_rooms']
dfcasas['population_per_household'] = dfcasas['population'] / dfcasas['households']

X = dfcasas.drop(columns=['median_house_value', 'total_rooms', 'total_bedrooms', 'population', 'households'])
y = dfcasas['median_house_value']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

tree_model = DecisionTreeRegressor(max_depth=5, random_state=42)
tree_model.fit(X_train, y_train)

y_pred = tree_model.predict(X_test)
score = r2_score(y_test, y_pred)

print(f"Puntaje de precisión (R^2): {score:.2f}")

# Predicción de los primeros 5 valores de prueba
print("Predicciones de los primeros 5 valores de prueba:")
print(y_pred[:5])

plt.figure(figsize=(10, 8))
sb.heatmap(dfcasas.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Mapa de correlación entre características")
plt.show()

plt.figure(figsize=(20, 10))
plot_tree(tree_model, feature_names=X.columns, filled=True, rounded=True, fontsize=10)
plt.title("Diagrama del Árbol de Decisión")
plt.show()