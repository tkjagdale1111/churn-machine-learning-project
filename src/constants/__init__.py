import os,sys
from datetime import datetime

def get_current_time_stamp():
    return f"{datetime.now().strftime('%Y-%m-%d %H-%M-%S')}"

current_time_stamp=get_current_time_stamp()

ROOT_DIR_KEY=os.getcwd()
DATA_DIR="Data"
DATA_DIR_KEY="customer_churn_large_dataset.xlsx"

ARTIFACT_DIR_KEY="Artifact"

DATA_INGESTION_KEY="data_ingstion"
DATA_INGESTION_RAW_DATA_DIR="raw_data_dir"
DATA_INGESTION_INGESTED_DATA_DIR_key="ingested_dir"
RAW_DATA_DIR_KEY="raw.csv"
TRAIN_DATA_DIR_KEY="train.csv"
TEST_DATA_DIR_KEY="test.csv"

# data transformation relted variable
DATA_TRANSFORMATION_ARTIFACT="data_transformation"
DATA_PROCESSOR_DIR="prossor"
DATA_TRANSFORMATION_PROCESSOR_OBJ='processor.pkl'
DATA_TRANSFORMATION_DIR="transformation"
TRANSFORAMTION_TRAIN_DATA_DIR="train.csv"
TRANSFORAMTION_TEST_DATA_DIR="test.csv"



MODEL_TRAINER_KEY="model_trainer"
MODEL_OBJECT="model.pkl"