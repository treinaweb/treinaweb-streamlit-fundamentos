import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

st.header("Iris Flower Prediction App")

st.sidebar.header("UI Parameters")


iris = datasets.load_iris()

X = iris.data
y = iris.target

