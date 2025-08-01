from sklearn.impute import SimpleImputer ## Handling missing values
from sklearn.preprocessing import StandardScaler # Handling Feature Scaling
from sklearn.preprocessing import OrdinalEncoder # Ordinal Encoding

## Pipelines
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
import os
import sys
import numpy as np
import pandas as pd

from dataclasses import dataclass
from src.logger import logging
from src.exception import CustomException

from src.utils import save_object


## Data Transformation config

@dataclass
class DataTransformationconfig:
    preprocessor_obj_file_path=os.path.join('artifacts','preprocesssor.pkl')



## Data Transformation config Class 

class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationconfig()
        

    def get_data_transformation_objects(self):
        try:
            logging.info('Data Transformation initiated')
            # numerical and categorical cols
            categorical_cols = ['cut', 'color', 'clarity']
            numerical_cols = ['carat', 'depth', 'table', 'x', 'y', 'z']

            # Define the custom rankings for each ordinal variable
            cut_categories = ['Fair','Good','Very Good','Premium','Ideal']
            color_categories = ['D','E','F','G','H','I','J']
            clarity_categories = ['I1','SI2','SI1','VS2','VS1','VVS2','VVS1','IF']

            logging.info('Pipeline Initiated')

            ## Numerical Pipeline
            num_pipeline = Pipeline(
            steps=[
                   ('imputer',SimpleImputer(strategy='median')),
                   ('scaler',StandardScaler())
                ]
            )

            ## Categorical Column
            cat_pipeline = Pipeline(
            steps=[
                  ('imputer',SimpleImputer(strategy='most_frequent')),
                  ('ordinalEncoder',OrdinalEncoder(categories=[cut_categories,color_categories,clarity_categories])),
                  ('scaler',StandardScaler())
                ]
            )

            preprocessor = ColumnTransformer([
                  ('num_pipeline',num_pipeline,numerical_cols),
                  ('cat_pipeline',cat_pipeline,categorical_cols)
            ])

            return preprocessor
            
            logging.info('Pipeline Completed')

        except Exception as e:
            logging.info("Error in Data Transformation")
            raise CustomException(e,sys)
        




    def initiate_data_transformation(self,train_path,test_path):
        try:
            # Reading train and test data
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info('Read train and test data completed')
            logging.info(f'Train Dataframe head: \n{train_df.head().to_string()}')
            logging.info(f'Train Dataframe head: \n{test_df.head().to_string()}')

            logging.info('Obtaining preprocessing object')

            preprocessing_obj = self.get_data_transformation_objects()

            target_column_name = 'price'
            drop_columns = [target_column_name,'id']

            ## Feature into dependent and independent feature
            input_feature_train_df = train_df.drop(columns=drop_columns,axis=1)
            target_feature_train_df = train_df[target_column_name]

            input_feature_test_df = test_df.drop(columns=drop_columns,axis=1)
            target_feature_test_df = test_df[target_column_name]

            ## Applying Transformation

            input_feature_train_arr = preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessing_obj.transform(input_feature_test_df)

            logging.info('Applying preprocessing object on training and testing datasets')

            train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_arr,np.array(target_feature_test_df)]


            save_object(
                file_path = self.data_transformation_config.preprocessor_obj_file_path,
                obj = preprocessing_obj
            )

            logging.info('Preprocessor pickle is created')


            return(
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path

            )
        
        except Exception as e:
            logging.info("Exception occured in the initiate_datatransformation")

            raise CustomException(e, sys)