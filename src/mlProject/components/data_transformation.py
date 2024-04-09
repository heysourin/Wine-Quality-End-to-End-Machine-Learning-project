# Components
import os
from mlProject import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from mlProject.entity.config_entity import DataTransformationConfig


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

        """
        You can add data cleaning code here, if required!!!!
        - EDA 
        - Scaling
        - Cleaing
        - etc
        
        You just have to create a function to do that, 
        then pass the data to the next function of train-test-split
        
        """

    def train_test_spliting(self):
        data = pd.read_csv(self.config.data_path)
        # splitting the data
        train, test = train_test_split(data)

        train.to_csv(os.path.join(
            self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(
            self.config.root_dir, "test.csv"), index=False)

        logger.info("Splitting data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)
