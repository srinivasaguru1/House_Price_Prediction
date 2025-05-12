import os
import sys
import numpy as np
import pandas as pd

"""
defining common constant variable for training pipeline
"""
NUMERICAL_COLUMNS = ['area','bedrooms','bathrooms','stories','parking']
CATEGORICAL_COLUMNS = ['mainroad','guestroom','basement','hotwaterheating','airconditioning','prefarea','furnishingstatus']
TARGET_COLUMN = "price"
PIPELINE_NAME: str = "HousePrice"
ARTIFACT_DIR: str = "Artifacts"
FILE_NAME: str ="HousePrice.csv"
TRAIN_FILE_NAME: str ="train.csv"
TEST_FILE_NAME:str ="test.csv"
PREPROCESSING_OBJECT_FILE_NAME ="preprocessing.pkl"
MODEL_FILE_NAME="model.pkl"
SCHEMA_FILE_PATH=os.path.join("data_schema","schema.yaml")
SCHEMA_DROP_COLS="drop_columns"
SAVED_MODEL_DIR=os.path.join("saved_models")

"""
data ingestion related constant srart with data_ingestion var name
"""
DATA_INGESTION_COLLECTION_NAME: str = "HousePriceData"
DATA_INGESTION_DATABASE_NAME: str = "SRINIVAS"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2

"""
data validation related constant start with data_validation var name
"""
DATA_VALIDATION_DIR_NAME: str = "data_validation"
DATA_VALIDATION_VALID_DIR: str = "validated"
DATA_VALIDATION_INVALID_DIR: str = "invalid"
DATA_VALIDATION_DRIFT_REPORT_DIR: str = "drift_report"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME: str = "report.yaml"
"""
data transformation related constant start with data_transformation var name
"""
DATA_TRANSFORMATION_DIR_NAME: str = "data_transformation"
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR: str = "transformed"
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR: str = "transformed_object"

DATA_TRANSFORMATION_IMPUTER_PARAMS: dict = {
    "missing_values": np.nan,
    "n_neighbors": 3,
    "weights": "uniform",
}

DATA_TRANSFORMATION_TRAIN_FILE_PATH: str = "train.npy"

DATA_TRANSFORMATION_TEST_FILE_PATH: str = "test.npy"
"""
model trainer related constant start with model trainer var name

"""
MODEL_TRAINER_DIR_NAME: str = "model_trainer"
MODEL_TRAINER_TRAINED_MODEL_DIR: str = "trained_model"
MODEL_TRAINER_TRAINED_MODEL_NAME: str = "model.pkl"
MODEL_TRAINER_EXPECTED_SCORE: float = 0.6
MODEL_TRAINER_OVER_FIITING_UNDER_FITTING_THRESHOLD: float = 0.25
PARAM_GRID = {
    'n_estimators': [100, 200, 300, 400],  # Higher estimators for better performance
    'max_features': ['sqrt', 'log2'],  # These two are common best practices
    'max_depth': [10, 20, 30, None],  # Limited depth prevents overfitting
    'min_samples_split': [2, 10, 20],  # Increase to avoid overfitting
    'min_samples_leaf': [1, 2, 4, 6],  # Minimum samples per leaf for balance
    'bootstrap': [True, False],  # Bootstrap is often beneficial for Random Forest
    'random_state': [42]  # Fixing random state for reproducibility
}

"""
Model Evaluation related constant start with MODEL_EVALUATION VAR NAME
"""
MODEL_EVALUATION_DIR_NAME: str = "model_evaluation"
MODEL_EVALUATION_CHANGED_THRESHOLD_SCORE: float = 0.02
MODEL_EVALUATION_REPORT_NAME= "report.yaml"

"""
Model Pusher related constant start with MODEL_PUSHER VAR NAME
"""
MODEL_PUSHER_DIR_NAME = "model_pusher"
MODEL_PUSHER_SAVED_MODEL_DIR = SAVED_MODEL_DIR

TRAINING_BUCKET_NAME = "houseprice12"
PREDICTION_BUCKET_NAME = "my-house-datasource"
PREDICTION_DIR= "prediction"
