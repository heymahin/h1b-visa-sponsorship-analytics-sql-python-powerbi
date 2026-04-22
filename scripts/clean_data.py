# clean_data.py

import pandas as pd

def clean_data(q1, q2, q3, q4):

    relevant_cols = [
        'CASE_NUMBER','CASE_STATUS','RECEIVED_DATE','DECISION_DATE','VISA_CLASS',
        'JOB_TITLE','SOC_CODE','SOC_TITLE','FULL_TIME_POSITION',
        'BEGIN_DATE','END_DATE','TOTAL_WORKER_POSITIONS',
        'EMPLOYER_NAME','EMPLOYER_CITY','EMPLOYER_STATE','NAICS_CODE',
        'WORKSITE_CITY','WORKSITE_STATE','WORKSITE_POSTAL_CODE',
        'WAGE_RATE_OF_PAY_FROM','WAGE_RATE_OF_PAY_TO','WAGE_UNIT_OF_PAY',
        'PREVAILING_WAGE','PW_WAGE_LEVEL'
    ]

    q1 = q1[relevant_cols]
    q2 = q2[relevant_cols]
    q3 = q3[relevant_cols]
    q4 = q4[relevant_cols]

    q1["quarter"] = "Q1"
    q2["quarter"] = "Q2"
    q3["quarter"] = "Q3"
    q4["quarter"] = "Q4"

    df = pd.concat([q1, q2, q3, q4], ignore_index=True)

    df.drop_duplicates(inplace=True)

    # Convert dates
    for col in ['RECEIVED_DATE','DECISION_DATE','BEGIN_DATE','END_DATE']:
        df[col] = pd.to_datetime(df[col], errors='coerce')

    # Numeric
    for col in ['WAGE_RATE_OF_PAY_FROM','WAGE_RATE_OF_PAY_TO','PREVAILING_WAGE','TOTAL_WORKER_POSITIONS']:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    # Fix salary units
    df.loc[(df['WAGE_UNIT_OF_PAY']=='Hour') & (df['WAGE_RATE_OF_PAY_FROM']>500),'WAGE_UNIT_OF_PAY']='Year'
    df.loc[(df['WAGE_UNIT_OF_PAY']=='Month') & (df['WAGE_RATE_OF_PAY_FROM']>50000),'WAGE_UNIT_OF_PAY']='Year'

    # Convert to annual
    def convert(row):
        w = row['WAGE_RATE_OF_PAY_FROM']
        u = row['WAGE_UNIT_OF_PAY']
        if pd.isna(w): return None
        if u=='Hour': return w*40*52
        elif u=='Week': return w*52
        elif u=='Bi-Weekly': return w*26
        elif u=='Month': return w*12
        else: return w

    df['ANNUAL_SALARY'] = df.apply(convert, axis=1)

    # Remove unrealistic salaries
    df = df[(df['ANNUAL_SALARY']>=30000) & (df['ANNUAL_SALARY']<=500000)]

    return df