# run_pipeline.py

from load_data import load_raw_data
from clean_data import clean_data
from export_to_sql import export_data

def main():
    print("Loading data...")
    q1, q2, q3, q4 = load_raw_data()

    print("Cleaning data...")
    df = clean_data(q1, q2, q3, q4)

    print("Exporting data...")
    export_data(df)

    print(" Pipeline completed!")

if __name__ == "__main__":
    main()