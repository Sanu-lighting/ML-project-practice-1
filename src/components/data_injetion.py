import sys
from dataclasses import dataclass
from src.exception import customException
from src.logger import logging
import numpy as np
import pandas as pd
import os
from sklearn.model_selection import train_test_split

@dataclass
class DataInjetionConfig:
    train_data_path=os.path.join('artifacts','train.csv')
    test_data_path=os.path.join('artifacts','test.csv')
    raw_data_path=os.path.join('artifacts','raw.csv')
class DataInjetion:
    def __init__(self):
        self.ingetion_config=DataInjetionConfig()
    def initiate_data_injetion(self):
        logging.info("Entered the data injetion method or component")
        try:
            df=pd.read_csv("Notebook/data/stud.csv")
            logging.info("Exported and read the dataset")
            os.makedirs(os.path.dirname(self.ingetion_config.train_data_path),exist_ok=True)
            df.to_csv(self.ingetion_config.raw_data_path,index=False,header=True)
            logging.info("train_test_split initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)
            train_set.to_csv(self.ingetion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingetion_config.test_data_path,index=False,header=True)
            logging.info("Injetion of the data is completed")
            return(
                self.ingetion_config.train_data_path,self.ingetion_config.test_data_path,
            ) 
        except Exception as e:
            raise customException(e,sys)

if __name__=="__main__":
    obj=DataInjetion()
    obj.initiate_data_injetion()



