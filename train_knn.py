import pandas as pd
import joblib

from gensim.models.doc2vec import Doc2Vec
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# cargar dataset
df = pd.read_csv("comentarios.csv")

# cargar Doc2Vec
modelo = Doc2Vec.load("modelo/modelo_doc2vec.model")

X = []
y = []

# crear embeddings
for _, row in df.iterrows():

    texto = row["comentario"]
    etiqueta = row["sentimiento"]

    tokens = texto.lower().split()

    vector = modelo.infer_vector(tokens)

    X.append(vector)
    y.append(etiqueta)

# dividir train/test
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# entrenar KNN
knn = KNeighborsClassifier(n_neighbors=5)

knn.fit(X_train, y_train)

# evaluar
pred = knn.predict(X_test)

accuracy = accuracy_score(y_test, pred)

print("Accuracy:", accuracy)

# guardar modelo
joblib.dump(knn, "modelo/knn_model.pkl")

print("KNN GUARDADO")
