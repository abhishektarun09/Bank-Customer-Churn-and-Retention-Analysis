import time
import sys

from src.utils.logger import logging
from src.utils.exception import CustomException

from src.ingestion.ingestion_to_db import load_raw_data

from src.processing.get_summary_table import create_customer_summary, clean_data
from src.ingestion.ingestion_to_db import ingest_db_postgres

from src.database.postgres_session import get_postgres_connection
engine = get_postgres_connection()

try:
  logging.info("----------Starting Raw Data Ingestion Process----------")
  load_raw_data()
  logging.info("----------Loaded Raw Data in DB----------")
except Exception as e:
  raise CustomException(e, sys)

try:
  logging.info("----------Starting Customer Churn Summary Table Creation Process----------")
  start_time = time.time()

  logging.info("----------Creating Customer Summary Table----------")
  summary_df = create_customer_summary(engine=engine)
  logging.info(summary_df.head())

  logging.info("----------Cleaning Data----------")
  clean_df = clean_data(df=summary_df)
  logging.info(clean_df.head())

  logging.info("----------Ingesting data in database----------")
  ingest_db_postgres(df=clean_df, table_name="customer_churn_summary", engine=engine)
  logging.info("----------Ingestion completed----------")

  end_time = time.time()

  time_taken = (end_time - start_time)/60

  logging.info(f"Time taken {time_taken} minutes.")
  logging.info("----------Customer Churn Summary Table Creation Process Completed----------")
  
except Exception as e:
  raise CustomException(e, sys)