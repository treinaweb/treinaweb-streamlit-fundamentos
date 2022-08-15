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

# Vídeo 2

st.header("Utilizando MultiSelect")

opcoes = st.multiselect(
    'Quais suas cores preferidas?',
    ['Verde', 'Amarelo', 'Vermelho', 'Azul', 'Preto']
)

st.write('Você selecionou: ', opcoes)

st.header("Utilizando Slider")

idade = st.slider('Quantos anos você tem?', 0, 100, 30)
st.write("Eu tenho ", idade, " anos de vida")

st.header("Utilizando o Select Slider")

cor = st.select_slider(
    'Selecione a cor',
    options=['red', 'orange', 'yellow', 'green', 'blue', 'grey'])

st.write('Cor favorita é: ', cor)

st.header("Number Input")

numero = st.number_input("Insira um número")
st.write("Número digitado foi: ", numero)

st.header("Utilizando o TextArea")

txt = st.text_area('Text to analyze', '''
     It was the best of times, it was the worst of times, it was
     the age of wisdom, it was the age of foolishness, it was
     the epoch of belief, it was the epoch of incredulity, it
     was the season of Light, it was the season of Darkness, it
     was the spring of hope, it was the winter of despair, (...)
     ''')
st.write('O texto é:', txt)

st.header("Utilizando Date Input")

d = st.date_input(
     "When's your birthday",
     datetime.date(2019, 7, 6))
st.write('Your birthday is:', d)

st.header("Utilizando Time Input")

t = st.time_input('Set an alarm for', datetime.time(8, 45))
st.write('Alarm is set for', t)