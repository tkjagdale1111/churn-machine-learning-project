
# Create prediction peipeline class -> completed
# create function for load a object -> completed
# Create custome class basd upon our dataset -> completed
# Create function to convert data into Dataframe with the help of DIct

import os, sys
from src.logger import logging
from src.exception import CustomException
import numpy as np
import pandas as pd
from dataclasses import dataclass
from src.utils import load_object

class PredictionPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        preprocessro_path = os.path.join("Artifact/data_transformation/prossor", "processor.pkl")
        model_path = os.path.join("artifacts/model_trainer", "model.pkl")

        processor = load_object(preprocessro_path)
        model = load_object(model_path)


        scaled = processor.transform(features)
        pred = model.predict(scaled)

        return pred


class CustomeClass:
    def __init__(self, 
                  Age:int,
                  Gender:int, 
                  Location:int, 
                  Subscription_Length_Months:int, 
                  Monthly_Bill:int,
                  Total_Usage_GB:int, ): 
                  
        self.Age = Age
        self.Gender = Gender
        self.Location = Location
        self.Subscription_Length_Months = Subscription_Length_Months
        self.Monthly_Bill = Monthly_Bill
        self.Total_Usage_GB = Total_Usage_GB
      


    def get_data_DataFrame(self):
        try:
            custom_input = {
                "Age": [self.Age],
                "Gender": [self.Gender],
                "Location":[self.Location],
                "Subscription_Length_Months":[self.Subscription_Length_Months],
                "Monthly_Bill":[self.Monthly_Bill],
                "Total_Usage_GB":[self.Total_Usage_GB]

            }

            data= pd.DataFrame(custom_input)

            return data
        except Exception as e:
            raise CustmeException(e, sys)












