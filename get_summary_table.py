import pandas as pd
import numpy as np
import time
import sys

from ingestion_to_db import ingest_db
from src.logger import logging
from src.exception import CustomException
from src.postgres_session import get_postgres_connection

engine = get_postgres_connection()

def create_customer_summary(engine):
    try:
        customer_churn_summary = pd.read_sql("""select * from bank_customer_churn""", engine)
        
        return customer_churn_summary
    
    except Exception as e:
        raise CustomException(e, sys)
    
def clean_data(df):
    try:
        df.columns = df.columns.str.lower()
        df = df.rename(columns={
                                "years_with_bank" : "years",
                                "risk_rating" : "risk",
                                "scheme_type" : "scheme",
                                "mobile_app_adoption" : "mobile_app",
                                "internet_banking_adoption" : "internet_banking",
                                "ussd_banking_adoption" : "ussd_banking",
                                "termloan_status" : "termloan",
                                "last_12_months_credit_volume" : "credit_vol",
                                "last_12_months_debit_volume" : "debit_vol",
                                " last_12_months_debit_value " : "debit_val",
                                " last_12_months_credit_value " : "credit_val",
                                " ave bal " : "ave_bal"
                                }
                       )
        # Cleaning ave_bal column 
        df['ave_bal'] = (df['ave_bal']
                         .astype(str)
                         .str.replace(',', '', regex=False)
                         .str.replace(r'\((.*?)\)', r'-\1', regex=True)
                         .str.strip()
                         .replace(['', '-'], np.nan)
                         .astype(float)
                         )
        
        #Cleaning debit value column and converting to float
        df['debit_val'] = (df['debit_val']
                         .astype(str)
                         .str.replace(',', '', regex=False)
                         .str.replace(r'\((.*?)\)', r'-\1', regex=True)
                         .str.strip()
                         .replace(['', '-'], 0)
                         .astype(float)
                         )
        
        #Cleaning credit value column and converting to float
        df['credit_val'] = (df['credit_val']
                         .astype(str)
                         .str.replace(',', '', regex=False)
                         .str.replace(r'\((.*?)\)', r'-\1', regex=True)
                         .str.strip()
                         .replace(['', '-'], 0)
                         .astype(float)
                         )
        
        df = df.dropna()
        
        cols = ['acct_id', 'risk', 'currency', 'scheme', 'mobile_app', 'internet_banking', 'ussd_banking', 'digital_loan', 'unsecured_loan', 'termloan', 'credit_card', 'subsegment']
        df[cols] = df[cols].apply(lambda col: col.str.strip())
        
        # One hot encoding
        cols = [
            "mobile_app", "internet_banking", "ussd_banking",
            "digital_loan", "unsecured_loan", "termloan", "credit_card"
        ]

        df[cols] = df[cols].replace({"Y": 1, "N": 0}).astype(int)
        
        df['risk'] = df['risk'].replace({"A-HIGH RISK": 'HIGH', "B-LOW RISK": 'MEDIUM', 'C-LOW RISK': 'LOW'})
        
        cols = ["mobile_app", "internet_banking", "ussd_banking"]
        df['digital_channels_used'] = df[cols].sum(axis=1)
        
        return df
        
    except Exception as e:
        raise CustomException(e, sys)
if __name__ == '__main__':
    
    start_time = time.time()
    
    logging.info("----------Creating Customer Summary Table----------")
    summary_df = create_customer_summary(engine=engine)
    logging.info(summary_df.head())
    
    logging.info("----------Cleaning Data----------")
    clean_df = clean_data(df=summary_df)
    logging.info(clean_df.head())
    
    logging.info("----------Ingesting data in database----------")
    ingest_db(df=clean_df, table_name="customer_churn_summary", engine=engine)
    logging.info("----------Ingestion completed----------")
    
    end_time = time.time()
    
    time_taken = (end_time - start_time)/60
    
    logging.info(f"Time taken {time_taken} minutes.")