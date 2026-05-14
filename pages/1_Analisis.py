import streamlit as st
from utils.predict import predecir_sentimiento

st.title("Analizar Comentario")

comentario = st.text_area(
    "Escribe un comentario de YouTube",
    height=150
)

if st.button("Analizar sentimiento"):

    if comentario.strip() == "":
        st.warning("Escribe un comentario primero.")
    else:
        resultado, confianza = predecir_sentimiento(comentario)

        st.subheader("Resultado")

        st.success(resultado)

        st.metric(
            label="Confianza",
            value=f"{confianza*100:.2f}%"
        )

        st.progress(confianza)
