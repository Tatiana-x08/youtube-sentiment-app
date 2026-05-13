import streamlit as st

st.set_page_config(
    page_title="YouTube Sentiment AI",
    page_icon="🎬",
    layout="centered"
)

st.title("🎬 Analizador de Sentimientos")

st.write("""
Esta aplicación analiza comentarios
de YouTube usando Inteligencia Artificial.
""")

st.subheader("¿Qué hace esta IA?")

st.write("""
- Detecta sentimientos positivos 😊
- Detecta sentimientos negativos 😡
- Usa NLP + Doc2Vec + KNN
""")

st.success("Proyecto de IA en Streamlit")