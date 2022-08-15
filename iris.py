import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

st.header("Iris Flower Prediction App")

st.sidebar.header("UI Parameters")

def ui_parameters():
    sepal_length = st.sidebar.slider('Sepal length', 4.3, 7.9, 5.0)
    sepal_width = st.sidebar.slider('Sepal width', 2.0, 4.4, 3.2)
    petal_length = st.sidebar.slider('Petal length', 1.0, 6.9, 2.5)
    petal_width = st.sidebar.slider('Petal width', 0.1, 2.5, 0.5)

    data = {
        'sepal_length' : sepal_length,
        'sepal_width'  : sepal_width,
        'petal_length' : petal_length,
        'petal_width'  : petal_width
    }
    parametros = pd.DataFrame(data, index=[0])
    return parametros

df = ui_parameters()

st.subheader("UI parâmetros")
st.write(df)

iris = datasets.load_iris()

X = iris.data
y = iris.target

