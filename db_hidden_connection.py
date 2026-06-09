import streamlit as st
from sqlalchemy import create_engine, URL
@st.cache_resource # to create my database connection engine once...
def get_con():
    db = st.secrets["database"] # accesing my hidden online database connection details
    # creating connection string 
    con_url = URL.create(
        drivername="postgresql+psycopg2",
        username=db["user"],
        password=db["psw"],
        host=db["host"],
        database=db["db_name"],
        query={"sslmode":db["sslmode"]}
        )
    # creating connection engine 
    con = create_engine(con_url,
                        pool_pre_ping=True # recreate it if it is dead
                        )
    return con