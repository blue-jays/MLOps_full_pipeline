import sys, os
import pandas as pd
import numpy as np
from src.logger import logging
from src.exception import CustomException
from dataclasses import dataclass
from sklearn.model_selection import train_test_split


"""
Using trace back: 
- Takes in data, splits into 3, saves it for next stage.
- The obj is the csv files, split dataset.
- so Init will have the paths, as path is the artifact.

    """
THIS_FILE = os.path.dirname(os.path.abspath(__file__))   # folder of the current file
PROJ_ROOT  = os.path.dirname(os.path.dirname(THIS_FILE))  # 2 levels above. (root)

@dataclass
class DataIngestionConfig:    # paths. for better debugging.
    train_data_path = os.path.join(PROJ_ROOT, "artifacts", "data_ingestion", "train.csv")
    test_data_path = os.path.join(PROJ_ROOT, "artifacts","data_ingestion", "test.csv")
    raw_data_path = os.path.join(PROJ_ROOT,"artifacts","data_ingestion","raw.csv")
    
class DataIngestion:
    def __init__(self):
        self.ingestion =DataIngestionConfig()    # the chararteristic of the object is paths/files.
    
    def  intitate_data_ingestion(self):
        logging.info("Data ingestion has begun")
        
        try:
            logging.info("Reading the csv file by pandas")
            data = pd.read_csv(os.path.join(PROJ_ROOT, "Data", "adult.csv"))
            logging.info("Data has been read")
            
            os.makedirs(os.path.dirname(self.ingestion.raw_data_path), exist_ok= True) # directory creation
            data.to_csv(self.ingestion.raw_data_path, index = False) # save it there. to_csv saves the data to the location
            logging.info("Raw data has been saved")
            
            # because of dirname, csv file is not created
            
            train_data, test_data = train_test_split(data, test_size=0.2, random_state = 42)
            logging.info("Data has been split")
            
            train_data.to_csv(self.ingestion.train_data_path, index = False, header = True)
            test_data.to_csv(self.ingestion.test_data_path, index = False, header = True )
            logging.info("train and test data has been saved")
            # index false means no index, now row numbering, header true means column naming.
            
            logging.info("Data ingesion complete")
            
            return self.ingestion.train_data_path, self.ingestion.test_data_path
            
        except Exception as e:
            logging.info("Could not initiate Data ingestion")
            raise CustomException(e, sys)
            
            
            
if __name__ == "__main__":
    obj = DataIngestion()
    train, test = obj.intitate_data_ingestion()
    print(train, test)
    
    
    
