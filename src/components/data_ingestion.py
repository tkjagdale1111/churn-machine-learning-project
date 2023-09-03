import os
import sys
from src.constants import *

from src.config.configuration import *
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.logger import logging
from src.exception import CustomException
from src.components.data_transformation import DataTransformation, DataTransformationConfig
from src.components.model_trainer import ModelTrainer 

@dataclass
class DataIngectionConfig:
    train_data_path:str =TRAIN_FILE_PATH
    test_data_path:str =TEST_FILE_PATH 
    raw_data_path:str = RAW_FILE_PATH
    
    
class DataIngestion:
    def __init__(self):
        self.data_ingection_config=DataIngectionConfig()
        
        
    def initiate_data_ingestion(self):
        try:
            df=pd.read_excel(DATASET_PATH)
            os.makedirs(os.path.dirname(self.data_ingection_config.raw_data_path),exist_ok=True)
            df.to_csv(self.data_ingection_config.raw_data_path,index=False)
            train_set,test_set=train_test_split(df,test_size=0.20,random_state=42)
            
            os.makedirs(os.path.dirname(self.data_ingection_config.train_data_path),exist_ok=True)
            train_set.to_csv(self.data_ingection_config.train_data_path,header=True)
            
            os.makedirs(os.path.dirname(self.data_ingection_config.test_data_path),exist_ok=True)
            test_set.to_csv(self.data_ingection_config.test_data_path,header=True)
            
            return(
                self.data_ingection_config.train_data_path,
                self.data_ingection_config.test_data_path
                )
            
        except Exception as e:
            raise CustomException(e,sys)
        
        
        
#if __name__ == "__main__":
    #obj=DataIngection()
    #train_data,test_data=obj.initiate_data_ingection()
    
    #data_transformation=DataTransformation()
    #train_arr,test_arr=data_transformation.inititate_data_transformation(train_data,test_data)
    
    
    
# model trainer
if __name__ == "__main__":
    obj=DataIngestion()
    train_data_path,test_data_path=obj.initiate_data_ingestion()
    
    data_transformation=DataTransformation()
    train_arr,test_arr,_=data_transformation.inititate_data_transformation(train_data_path,test_data_path)
    
    model_trainer=ModelTrainer()
    print(model_trainer.inititate_model_trainer(train_arr,test_arr))