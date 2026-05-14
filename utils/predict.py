from utils.load_model import modelo
import joblib

knn = joblib.load("modelo/knn_model.pkl")

def predecir_sentimiento(texto):

    texto_lower = texto.lower()

    positivas = [
        "love", "like", "amazing", "good", "great", "excellent",
        "me encanta", "me gusta", "bueno", "genial", "excelente"
    ]

    negativas = [
        "hate", "bad", "terrible", "horrible", "awful",
        "odio", "mierda", "malo", "fatal", "asco"
    ]

    if any(p in texto_lower for p in positivas):
        return "😊 Positivo", 0.95

    if any(n in texto_lower for n in negativas):
        return "😡 Negativo", 0.95

    tokens = texto_lower.split()
    vector = modelo.infer_vector(tokens)

    pred = knn.predict([vector])[0]

    if pred == 0:
        resultado = "😊 Positivo"
    else:
        resultado = "😡 Negativo"

    confianza = max(knn.predict_proba([vector])[0])

    return resultado, confianza
