import streamlit as st

st.title("Analizar Comentario")

comentario = st.text_area(
    "Escribe un comentario de YouTube",
    height=150
)

if st.button("Analizar sentimiento"):

    # Resultado temporal
    resultado = "😊 Positivo"
    confianza = 0.91

    st.subheader("Resultado")

    st.success(resultado)

    st.metric(
        label="Confianza",
        value=f"{confianza*100:.2f}%"
    )

    st.progress(confianza)