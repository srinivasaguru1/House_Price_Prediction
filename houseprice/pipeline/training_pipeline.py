import os
import sys
from houseprice.exception.exception import HousePriceException
from houseprice.logger.logger import logging

from houseprice.components.data_ingestion import DataIngestion
# from houseprice.components.data_validation import DataValidation
# from houseprice.components.data_transformation import DataTransformation
# from houseprice.components.model_trainer import ModelTrainer
# from houseprice.components.model_evaluation import ModelEvaluation
# from houseprice.components.model_pusher import ModelPusher

from houseprice.entity.config_entity import (
    TrainingPipelineConfig,
    DataIngestionConfig,
    DataValidationConfig,
    DataTransformationConfig,
    ModelTrainerConfig,
    ModelEvaluationConfig,
    ModelPusherConfig

)

from houseprice.entity.artifact_entity import(
    DataIngestionArtifact,
    DataValidationArtifact,
    DataTransformationArtifact,
    ModelTrainerArtifact,
    ModelEvaluationArtifact,
    ModelPusherArtifact
)

class TrainingPipeline:
    def __init__(self):
        self.training_pipeline_config = TrainingPipelineConfig()

    def start_data_ingestion(self):
        try:
            self.data_ingestion_config=DataIngestionConfig(training_pipeline_config=self.training_pipeline_config)
            logging.info("Starting data ingestion")
            data_ingestion=DataIngestion(data_ingestion_config=self.data_ingestion_config)
            data_ingestion_artifact=data_ingestion.initiate_data_ingestion()
            logging.info(f"Data ingestion completed and artifact: {data_ingestion_artifact}")
            return data_ingestion_artifact
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
            data_ingestion_artifact= self.start_data_ingestion()
            #print(data_ingestion_artifact)
            data_validation= self.start_data_validataion()
            print(data_validation)
        except Exception as e:
            raise HousePriceException(e,sys)

