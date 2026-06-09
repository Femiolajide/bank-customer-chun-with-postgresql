import pandas as pd
from db_hidden_connection import get_con
# table name and column name transformation logic
def clean_name(txt:str) -> str:
    """standardize string to snake_case"""
    import re
    txt = str(txt)
    # replace two or more whitespace with one whitespace
    txt = re.sub(r"\s{2,}"," ",txt) 
    # repace anything that is not alphanumeric with an underscore
    txt = re.sub(r"[^aA-zZ0-9_]","_",txt) 
    # to handle CamelCase
    for x in txt:
        if str(x).isupper():
            txt = txt.replace(x,f"_{x}")
    txt = txt.strip("_").lower()
    txt = re.sub(r'_{2,}','_',txt)
    return txt

def load_data_to_postgresql() -> pd.DataFrame:
    """This ETL script loads Bank_Churn_Messy.xlsx to online postgresql servr"""
    import pandas as pd
    bank_churn_messy = pd.read_excel(
        "data/Bank_Churn_Messy.xlsx",sheet_name=None)
    details = []
    for sht_name, df in bank_churn_messy.items():
        # column name transformation 
        df = df.rename(columns=lambda x: clean_name(x))
        df.to_sql(
            name=clean_name(sht_name), # table name transformation
            con=get_con(),
            if_exists="replace",index=False)
        details.append([clean_name(sht_name),df.shape[0],df.shape[1]])
        # getting the names of tables and the number of rows loaded
    return pd.DataFrame(details,columns=["Table","Row","Column"])