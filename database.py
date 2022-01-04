import mysql.connector
import streamlit as st

st.cache(allow_output_mutation=True, hash_funcs={"_thread.RLock": lambda _: None})
def init_connection():
    return mysql.connector.connect(**st.secrets["mysql"])

cnn = init_connection()
#cnn = mysql.connector.connect(user='root', password='aline', host='localhost', database='crud_escola')
cursor = cnn.cursor()