import os 
import sys
from dataclasses import dataclass
from sklearn.ensemble import  AdaBoostRegressor,GradientBoostingRegressor,RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from xgboost import XGBRegressor
from src.exception import customException
from src.logger import logging
from src.utils import save_object, evaluate_model
from catboost import CatBoostRegressor

@dataclass 
class ModelTrainerConfig:
    trained_model_file_path=os.path.join("artifacts","model.pkl")
class ModeTrainer:
    def __init__(self):
        self.model_trainer_config=ModelTrainerConfig()
    def initiate_model_trainer(self,train_array,test_array):
        try:
            logging.info("Split train and test input data")
            X_train,y_train,X_test,y_test=(
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )
            models={
                "RF":RandomForestRegressor(),
                "DT":DecisionTreeRegressor(),
                "Gradiant Boost":GradientBoostingRegressor(),
                "Linear Reg":LinearRegression(),
                "KNN":KNeighborsRegressor(),
                "XGB":XGBRegressor(),
                "CatBoost":CatBoostRegressor(),
                "AdaBoost":AdaBoostRegressor()
            }
            model_report:dict=evaluate_model(X_train=X_train,y_train=y_train,X_test=X_test,y_test=y_test,models=models)
            best_model_score=max(sorted(model_report.values()))
            best_model_name=list(model_report.keys())[list(model_report.values()).index(best_model_score)]
            best_model=models[best_model_name]
            if best_model_score<0.6:
                raise customException("No Best Model Found")
            logging.info("Best model Found")
            
            save_object(file_path=self.model_trainer_config.trained_model_file_path,
                        obj=best_model)
            predicted=best_model.predict(X_test)
            r2s=r2_score(y_test,predicted)
            return r2s
        except Exception as e:
            raise customException(e,sys)



