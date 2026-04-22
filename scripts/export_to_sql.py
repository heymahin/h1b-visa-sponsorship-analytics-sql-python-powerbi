# export_to_sql.py

from sqlalchemy import create_engine

def export_data(df):

    # Save CSV
    df.to_csv("../data/processed/h1b_clean_2024.csv", index=False)

    # MySQL connection
    engine = create_engine("mysql+pymysql://root:mahin%40123@localhost:3306/h1b_project")

    # Upload
    df.to_sql("h1b_clean", con=engine, if_exists="replace", index=False, chunksize=5000)

    print(" Data exported successfully")