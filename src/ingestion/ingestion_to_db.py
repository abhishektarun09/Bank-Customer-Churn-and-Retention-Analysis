import pandas as pd
import os
import time
import sys
import pandas_gbq

from utils.logger import logging
from utils.exception import CustomException
from database.postgres_session import get_postgres_connection
from google.oauth2 import service_account

from dotenv import load_dotenv

load_dotenv()

gbq_project_id = os.getenv("BigQuery_Project_ID")
gbq_json_path = os.getenv("BigQuery_Service_Account_JSON")
gbq_dataset = os.getenv("BigQuery_Dataset")

credentials = service_account.Credentials.from_service_account_file(gbq_json_path)

engine = get_postgres_connection()

def ingest_db_postgres(df, table_name, engine):
    """This function ingests data into SQL Database"""
    
    try:
        df.to_sql(table_name, con = engine, if_exists = 'replace', index = False)
        
    except Exception as e:
        raise CustomException(e, sys)
    
def ingest_db_gbq(df, table_name, project_id, credentials):
    """This function ingests data into Google BigQuery"""
    
    try:
        pandas_gbq.to_gbq(dataframe=df, destination_table=table_name, project_id=project_id, if_exists='replace', credentials=credentials)
        
    except Exception as e:
        raise CustomException(e, sys)
    

def load_raw_data():    
    """This function will load CSV files as pandas dataframe and ingest into db"""
    
    try:
        start_time = time.time()
        for file in os.listdir('data'):
            if '.csv' in file:
                df = pd.read_csv('data/'+file)
                logging.info(f"Ingesting {file} in db.")
                ingest_db_postgres(df, file[:-4], engine)
                #ingest_db_gbq(df=df, table_name=f"{gbq_dataset}.{file[:-4]}", project_id=gbq_project_id, credentials=credentials)
        end_time = time.time()
        logging.info("----------Ingestion Completed----------")
        total_time = (end_time - start_time)/60
        logging.info(f"Time taken {total_time} minutes.")
        
    except Exception as e:
        raise CustomException(e, sys)
