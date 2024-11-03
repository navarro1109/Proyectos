import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np

df_altpe = pd.read_csv('./altura_peso.csv')

# df_altpe.head()
X = df_altpe[['altura']]
y = df_altpe['peso']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

score = model.score(X_test, y_test)
print("Puntuación del modelo: ", score)

try:
    altura_usuario = float(input("Ingresa la altura en metros (por ejemplo, 1.75): "))
    nueva_altura = np.array([[altura_usuario]])

    # Predicción del peso
    peso_predicho = model.predict(nueva_altura)
    print("El peso estimado de una altura: ", altura_usuario, "m es", peso_predicho, "kg")
except ValueError:
    print("Por favor, ingresa un valor numérico válido para la altura.")
