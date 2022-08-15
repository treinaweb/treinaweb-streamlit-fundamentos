import streamlit as st

st.title("App Streamlit Sample")
st.markdown("Streamlit **é** **divertido**.")
st.header("Adicionando um Cabeçalho")
st.subheader("Adicionando um Subcabeçalho")
st.caption("O texto está pequeno")
st.code("v=Sicrano + v = Fulano")
st.text("Olá mundo")
st.latex(r'''
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''')