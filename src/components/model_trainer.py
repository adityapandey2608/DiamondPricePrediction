import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression,Ridge,Lasso,ElasticNet
from sklearn.tree import DecisionTreeRegressor
from src.exception import CustomException
from src.logger import logging

from src.utils import save_object
from src.utils import evaluate_model

from dataclasses import dataclass
import sys
import os

@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join('artifacts','model.pkl')

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_training(self,train_array,test_array):
        try:
            logging.info('Splitting Dependent and Independent variables from train and test data')
            X_train,y_train,X_test,y_test = (
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )

            models={
                'LinearRegression':LinearRegression(),
                'Lasso':Lasso(),
                'Ridge':Ridge(),
                'Elasticnet':ElasticNet(),
                'DecisionTree':DecisionTreeRegressor()
            }

            model_report:dict=evaluate_model(X_train,y_train,X_test,y_test,models)
            print(model_report)
            print('='*35)
            print('\n')
            logging.info(f'Model Report : {model_report}')

            ## To get best model score from dictionary
            best_model_name = max(model_report, key=model_report.get)
            best_model_score = model_report[best_model_name]


            best_model = models[best_model_name]

            print(f'Best Model Found, Model Name : {best_model_name}, R2 Score: {best_model_score}')
            print('='*35)
            print('\n')

            logging.info(f'Best Model Found, Model Name : {best_model_name}, R2 Score: {best_model_score}')
            
            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )

        except Exception as e:
            logging.info('Exception occured at Model Training ')
            raise CustomException(e,sys)