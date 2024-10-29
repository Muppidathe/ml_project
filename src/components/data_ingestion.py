import os
import sys
import pandas as pd
import numpy as np
from  src.exception import CustomException
from src.logger import logger
from dataclasses import dataclass
from sklearn.model_selection import train_test_split


@dataclass
class Dataingesionconfig:
    train_data_path=os.path.join("artifact/","train.csv")
    test_data_path=os.path.join("artifact/","test.csv")
    raw_data_path=os.path.join("artifact/","raw.csv")

class Dataingestion:
    def __init__(self):
        self.config=Dataingesionconfig()
    def initialize_dataingestion(self):
        try:    

            logger.info("Initializing data ingestion")
            df=pd.read_csv("notebook/data/stud.csv")
            logger.info("Data has been readed successfully")
            os.makedirs(os.path.dirname(self.config.train_data_path), exist_ok=True)
            df.to_csv(self.config.raw_data_path,index=False)
            logger.info("Raw data has been saved successfully")
            train,test=train_test_split(df,test_size=0.2,random_state=42)
            train.to_csv(self.config.train_data_path,index=False)
            test.to_csv(self.config.test_data_path,index=False)
            logger.info("Train and test data has been saved successfully")
            return (self.config.raw_data_path,self.config.train_data_path,self.config.test_data_path)


        except Exception as e:
            raise CustomException(e,sys)





if __name__=="__main__":
    obj=Dataingestion()
    obj.initialize_dataingestion()
