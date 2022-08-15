import time
import streamlit as st

st.header("Utilizando Barra de Progresso")

minha_barra = st.progress(00)

for percent_complet in range(20):
    time.sleep(0.1)
    minha_barra.progress(percent_complet + 1)

st.header("Utilizando o Spinner")

with st.spinner("Aguarde ..."):
    time.sleep(1)
st.success("Carregado!")

st.balloons()

st.header("Utilizando o Snowflake")

st.snow()

st.error("Mensagem de erro")

st.warning("Mensagem de warning")

st.info("Mensagem de informação")

e = RuntimeError("Erro X")
st.exception(e)