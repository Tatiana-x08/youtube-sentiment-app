from utils.load_model import modelo
import joblib

knn = joblib.load("modelo/knn_model.pkl")

def predecir_sentimiento(texto):

    tokens = texto.lower().split()

    vector = modelo.infer_vector(tokens)

    pred = knn.predict([vector])[0]

    if pred == 1:
        resultado = "😊 Positivo"
    else:
        resultado = "😡 Negativo"

    confianza = max(knn.predict_proba([vector])[0])

    return resultado, confianza
