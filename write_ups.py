title = """End-to-End Bank Customer Churn Analysis UsingPostgreSQL and Streamlit"""
description = """This app analyses bank customer churn using 
PostgreSQL, Python, SQLAlchemy, and Streamlit. Each section 
displays the SQL query used for data quality checks, data cleaning, 
or business analysis. Click :green-badge[RUN] to execute a query, view the result, 
and read a short insight explaining what the output reveals about 
customer churn and the dataset generally where applicable."""
data_source = """
The dataset used in this project is the Bank Customer Churn dataset 
downloaded from the
[Maven Analytics free dataset collection](https://maven-datasets.s3.amazonaws.com/Bank+Customer+Churn/Bank+Customer+Churn.zip)
on June 9, 2026. The compressed dataset file contains a data dictionary and different 
versions of the bank churn data. This project uses :gray-badge[Bank_Churn_Messy.xlsx], 
the messy Excel version of the dataset, so that the workflow begins from raw data instead 
of an already cleaned table. The workbook contains two sheets, :gray-badge[Customer_Info] 
and :gray-badge[Account_Info], and each sheet is loaded into the remote PostgreSQL database 
as a separate table through the Streamlit app and the ETL script designed for this repository.
"""
etl = """
This section performs the ETL step for the project. The ETL script extracts raw data from :gray-badge[_Bank_Churn_Messy.xlsx_], 
standardises the table names and column names into :gray-badge[_snake_case_],
and loads each sheet into the remote PostgreSQL database.
The :gray-badge[_Customer_Info_] sheet is loaded as 
:gray-badge[_customer_info_], while the :gray-badge[_Account_info_] 
sheet is loaded as :gray-badge[_account_Info_].
"""