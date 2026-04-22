# load_data.py

import pandas as pd

def load_raw_data():
    base_path = "../data/raw/"

    q1 = pd.read_excel(base_path + "LCA_Disclosure_Data_FY2024_Q1.xlsx")
    q2 = pd.read_excel(base_path + "LCA_Disclosure_Data_FY2024_Q2.xlsx")
    q3 = pd.read_excel(base_path + "LCA_Disclosure_Data_FY2024_Q3.xlsx")
    q4 = pd.read_excel(base_path + "LCA_Disclosure_Data_FY2024_Q4.xlsx")

    return q1, q2, q3, q4