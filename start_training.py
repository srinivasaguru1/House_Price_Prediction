import os
import sys

from houseprice.exception.exception import HousePriceException
from houseprice.logger.logger import logging

from houseprice.pipeline.training_pipeline import TrainingPipeline


def start_training():
    try:
        model_training=TrainingPipeline()
        model_training.run_pipeline()
    except Exception as e:
        raise HousePriceException(e,sys)
    

if __name__=='__main__':
    start_training()