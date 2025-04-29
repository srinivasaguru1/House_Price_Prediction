import os
import sys
from houseprice.exception.exception import HousePriceException
from houseprice.logger.logger import logging

from houseprice.components.data_ingestion import DataIngestion
from houseprice.components.data_validation import DataValidation
from houseprice.components.data_transformation import DataTransformation
from houseprice.components.model_trainer import ModelTrainer
from houseprice.components.model_evaluation import ModelEvaluation
from houseprice.components.model_pusher import ModelPusher

from networksecurity.entity.config_entity import (
    TrainingPipelineConfig,
    DataIngestionConfig,
    DataValidationConfig,
    DataTransformationConfig,
    ModelTrainerConfig,
    ModelEvaluationConfig,
    ModelPusherConfig

)

from houseprice.entity.config_entity import(
    DataIngestionArtifact,
    DataValidationArtifact,
    DataTransformationArtifact,
    ModelTrainerArtifact,
    ModelEvaluationArtifact,
    ModelPusherArtifact
)

class TrainingPipeline:
    def __init__(self):
        pass

    def start_data_ingestion(self):
        try:
            pass
        except Exception as e:
            raise HousePriceException(e,sys)
        
    def start_data_validation(self):
        try:
            pass
        except Exception as e:
            raise HousePriceException(e,sys)
        
    def start_data_transformation(self):
        try:
            pass
        except Exception as e:
            raise HousePriceException(e,sys)
    def start_model_trainer(self):
        try:
            pass
        except Exception as e:
            raise HousePriceException(e,sys)
        
    def start_model_evaluation(self):
        try:
            pass
        except Exception as e:
            raise HousePriceException(e,sys)
    def start_model_pusher(self):
        try:
            pass
        except Exception as e:
            raise HousePriceException(e,sys)
        

    def run_pipeline(self):
        try:
            pass
        except Exception as e:
            raise HousePriceException(e,sys)
    

