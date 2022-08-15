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

st.header("Utilizando File Uploader")

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
     # To read file as bytes:
     bytes_data = uploaded_file.getvalue()
     st.write(bytes_data)

     # To convert to a string based IO:
     stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
     st.write(stringio)

     # To read file as string:
     string_data = stringio.read()
     st.write(string_data)

     # Can be used wherever a "file-like" object is accepted:
     dataframe = pd.read_csv(uploaded_file)
     st.write(dataframe)

st.header("Utilizando Câmera Input")

picture = st.camera_input("Take a picture")

if picture:
     st.image(picture)

st.header("Utilizando Color Picker")

color = st.color_picker('Pick A Color', '#00f900')
st.write('The current color is', color)