import streamlit as st
from PIL import Image

st.header("Utilizando Imagens")

imagem1 = Image.open("Recursos/img1.png")

st.image(imagem1, caption="Logo da Treinaweb")

imagem2 = Image.open("Recursos/img2.png")

st.image(imagem2, caption="Segunda logo da Treinaweb")

st.header("Utilizando Audio")

audio_arquivo = open("Recursos/full_preview.mp3", "rb")
audio_bytes = audio_arquivo.read()

st.audio(audio_bytes, format='audio/mp3')

st.header("Utilizando Vídeo")

video_arquivo = open("Recursos/Curso.mp4", "rb")
video_bytes = video_arquivo.read()

st.video(video_bytes)
