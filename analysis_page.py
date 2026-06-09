import streamlit as st
import pandas as pd 
from sqlalchemy import text
from etl_script import load_data_to_postgresql,get_con,clean_name
import queries as q
import write_ups as w
import insights as i

# coding editor 
def code(query:str):
    return st.code(query,language="sql",
                   line_numbers=True)
# run button
def run(num:int):
    return st.button(":green-badge[RUN]",key=num)
# query result

def query_it(query:str):
    @st.cache_data(ttl=300,show_spinner="running query...")
    def run_query(query:str) -> pd.DataFrame:
        query = query
        eng = get_con()
        res = pd.read_sql(text(query),con=eng)
        return res
    return st.dataframe(run_query(query),hide_index=True,width="content")

st.title(w.title)
st.write("---")
st.write(w.description)
st.write("---")
st.markdown("#### :blue[1. Data Setup]")
with st.expander("__1.1 Data source__", expanded=False):
    st.markdown(w.data_source)
with st.expander("__1.2 Data Dictionary__", expanded=False):
    a = pd.read_csv(r"data\Bank_Churn_Data_Dictionary.csv")
    a = a.rename(columns={"Field":"Field (source)"})
    a["Field (standardized)"] = a["Field (source)"].map(lambda x: clean_name(x))
    a = a[["Field (source)","Field (standardized)","Description"]]
    b = pd.read_excel(r"data\Bank_Churn_Messy.xlsx",nrows=1)
    c = pd.read_excel(r"data\Bank_Churn_Messy.xlsx",sheet_name=1,nrows=1)
    sht_name = pd.ExcelFile(r"data\Bank_Churn_Messy.xlsx").sheet_names
    sht_name = [clean_name(x) for x in sht_name]
    st.write(f"#### :blue-badge[{sht_name[0]}]")
    st.table(a[a["Field (source)"].isin(b.columns)],hide_index=True)
    st.write(f"#### :blue-badge[{sht_name[1]}]")
    st.table(a[a["Field (source)"].isin(c.columns)],hide_index=True)

with st.expander("__1.3 ETL: Load :gray-badge[_Bank_Churn_Messy.xlsx_] into PostgreSQL__"):
    st.markdown(w.etl)
    if st.button(":green-badge[__Load Bank_Churn_Messy.xlsx into PostgreSQL__]"):
        with st.spinner(":green[Loading data into postgreSQL. Please wait...]"):
            rows_loaded = load_data_to_postgresql()
        st.success(f":material/task_alt: `Data loaded successfully into bank_customer database`")
        st.write("__Details__")
        st.markdown(rows_loaded.to_markdown(index=False))
with st.expander("__1.4  Preview Raw Table__"):
    code(q.head_1)
    if run(1):
        query_it(q.head_1)
        st.write(i.col_name)
    code(q.head_2)
    if run(2):
        query_it(q.head_2)
        st.write(i.col_name)