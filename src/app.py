import streamlit as st
from agente import responder

st.title("💰 BIA do Futuro (Local com LLaMA)")

pergunta = st.text_input("Digite sua pergunta:")

if st.button("Enviar"):
    if pergunta:
        resposta = responder(pergunta)
        st.write("🤖 Resposta:")
        st.write(resposta)
