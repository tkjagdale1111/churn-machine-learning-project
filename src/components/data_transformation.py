from src.constants import *
from src.logger import logging
from src.exception import CustomException
import os, sys
from src.config.configuration import *
from dataclasses import dataclass
from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OrdinalEncoder,OneHotEncoder
from sklearn.pipeline import Pipeline
from src.utils import save_obj
from src.config.configuration import PREPROCESSING_OBJ_FILE,TRANSFORM_TRAIN_FILE_PATH,TRANSFORM_TEST_FILE_PATH,FEATURE_ENG_OBJ_FILE

# FE
# Data transformation

class Feature_Engineering(BaseEstimator, TransformerMixin):
    def __init__(self):
        logging.info("******************feature Engineering started******************")


@dataclass 
class DataTransformationConfig():
    proccessed_obj_file_path = PREPROCESSING_OBJ_FILE
    transform_train_path = TRANSFORM_TRAIN_FILE_PATH
    transform_test_path = TRANSFORM_TEST_FILE_PATH
    feature_engg_obj_path = FEATURE_ENG_OBJ_FILE


class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()


    def get_data_transformation_obj(self):
        try:
           

            categorical_columns = ['Gender','Location']
            numerical_column=['Age','Subscription_Length_Months','Monthly_Bill','Total_Usage_GB']

            # Numerical pipeline
            numerical_pipeline = Pipeline(steps = [
                ('impute', SimpleImputer(strategy = 'constant', fill_value=0)),
                ('scaler', StandardScaler(with_mean=False))
            ])

            # Categorical Pipeline
            categorical_pipeline = Pipeline(steps = [
                ('impute', SimpleImputer(strategy = 'most_frequent')),
                ('onehot', OneHotEncoder(handle_unknown = 'ignore')),
                ('scaler', StandardScaler(with_mean=False))
            ])

            preprocssor = ColumnTransformer([
                ('numerical_pipeline', numerical_pipeline,numerical_column ),
                ('categorical_pipeline', categorical_pipeline,categorical_columns )
            ])

            logging.info("Pipeline Steps Completed")
            return preprocssor

        except Exception as e:
            raise CustomException( e,sys)
        

   
        
    def inititate_data_transformation(self, train_path, test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)


            processinf_obj = self.get_data_transformation_obj()

            traget_columns_name = "Churn"

            X_train = train_df.drop(columns = traget_columns_name, axis = 1)
            y_train = train_df[traget_columns_name]

            X_test = test_df.drop(columns = traget_columns_name, axis = 1)
            y_test = test_df[traget_columns_name]

            X_train = processinf_obj.fit_transform(X_train)
            X_test = processinf_obj.transform(X_test)

            train_arr = np.c_[X_train, np.array(y_train)]
            test_arr = np.c_[X_test, np.array(y_test)]

            df_train = pd.DataFrame(train_arr)
            df_test = pd.DataFrame(test_arr)

            os.makedirs(os.path.dirname(self.data_transformation_config.transform_train_path), exist_ok=True)
            df_train.to_csv(self.data_transformation_config.transform_train_path, index = False, header = True)

            os.makedirs(os.path.dirname(self.data_transformation_config.transform_test_path), exist_ok=True)
            df_test.to_csv(self.data_transformation_config.transform_test_path, index = False, header = True)
            
            save_obj(file_path=self.data_transformation_config.proccessed_obj_file_path,
                        obj=processinf_obj)

            
            return(train_arr,
                   test_arr,
                   self.data_transformation_config.proccessed_obj_file_path)
        
        except Exception as e:
            raise CustomException( e,sys)