from utils.load_model import modelo
import random

def predecir_sentimiento(texto):

    tokens = texto.lower().split()

    vector = modelo.infer_vector(tokens)

    # temporal hasta tener clasificador real
    resultado = random.choice([
        "😊 Positivo",
        "😡 Negativo"
    ])

    confianza = random.uniform(0.70, 0.99)

    return resultado, confianza
