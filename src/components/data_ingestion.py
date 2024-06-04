
import pandas as pd
from dataclasses import dataclass
from src.logger import logging
from src.exception import CustomException
from sklearn.model_selection import train_test_split
import os
import sys
from src.components.data_transformer import DataTransformation
from src.components.data_trainer import ModelTrainer

@dataclass
class DataIngestionConfig:
    train_data_path:str = os.path.join("Artifact","train.csv")
    test_data_path:str = os.path.join("Artifact","test.csv")
    raw_data_path:str = os.path.join("Artifact","raw.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config =DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Data ingestion process initiated")
        try:
            df = pd.read_csv("Notebook\data\stud.csv")
            logging.info('dataset read into dataframe')
            
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok =True)
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header =True)

            logging.info("train test split initated")

            train_data, test_data = train_test_split(df, test_size = 0.2, random_state = 42)

            train_data.to_csv(self.ingestion_config.train_data_path, index = False, header = True)
            test_data.to_csv(self.ingestion_config.test_data_path, index = False, header = True)
            
            logging.info("Ingestion process completed")


            return ( 
                
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        
        except Exception as e:
            raise CustomException(e,sys)

if __name__=="__main__":
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()

    transformation = DataTransformation()
    train_arr,test_arr,_= transformation.initiate_data_transformation(train_data, test_data)

    model_trainer = ModelTrainer()
    print(model_trainer.initiate_model_trainer(train_arr,test_arr))
