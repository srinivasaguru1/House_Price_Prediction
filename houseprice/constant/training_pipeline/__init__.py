import os
import sys
import numpy as np
import pandas as pd

"""
defining common constant variable for training pipeline
"""
TARGET_COLUMN = "Result"
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

"""
model trainer related constant start with model trainer var name

"""
