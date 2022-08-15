# Vídeo 1 =========

import streamlit as st
import pandas as pd
import numpy as np
import datetime
from io import StringIO

st.header("Botão")

if st.button("Mensagem"):
    st.write("Olá mundo")
else:
    st.write("Adeus")

st.header("Botão de Download")

@st.cache

def convert_df(df):
    return df.to_csv().encode('utf-8')

dataframe = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)
csv = convert_df(dataframe)

st.download_button(
    label = "Download data as CSV",
    data = csv,
    file_name="dataframe.csv",
    mime = "text/csv"
)

st.header("Utilizando checkbox")

aceito = st.checkbox("Eu aceito o termo de uso")

if aceito:
    st.write("Parabéns por ter aceito os termos de uso")
else:
    st.write("Leia os termos de uso")

st.header("Utilizando RadioBox")

genero = st.radio(
    "Qual gênero de filme preferido?",
    ('Comédia', 'Drama', 'Documentário')
)

if genero == 'Comédia':
    st.write("Você selecionou o gênero comédia")
else:
    st.write("Você não gosta de comédia")

