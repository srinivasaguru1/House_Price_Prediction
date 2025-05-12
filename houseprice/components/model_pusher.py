from houseprice.exception.exception import HousePriceException
from houseprice.logger.logger import logging
from houseprice.entity.artifact_entity import ModelPusherArtifact, ModelTrainerArtifact, ModelEvaluationArtifact
from houseprice.entity.config_entity import ModelEvaluationConfig, ModelPusherConfig
import os, sys
from houseprice.utils.ml_utils.metric.regression_metric import get_regression_score
from houseprice.utils.main_utils.utils import save_object, load_object, write_yaml_file
import shutil

class ModelPusher:

    def __init__(self, model_pusher_config: ModelPusherConfig, model_eval_artifact: ModelEvaluationArtifact):
        try:
            self.model_pusher_config = model_pusher_config
            self.model_eval_artifact = model_eval_artifact
        except Exception as e:
            raise HousePriceException(e, sys)

    def initiate_model_pusher(self) -> ModelPusherArtifact:
        try:
            trained_model_path = self.model_eval_artifact.trained_model_path

            # Creating model pusher dir to save model
            model_file_path = self.model_pusher_config.model_file_path
            os.makedirs(os.path.dirname(model_file_path), exist_ok=True)
            shutil.copy(src=trained_model_path, dst=model_file_path)

            # Saved model dir
            saved_model_path = self.model_pusher_config.saved_model_path
            os.makedirs(os.path.dirname(saved_model_path), exist_ok=True)
            shutil.copy(src=trained_model_path, dst=saved_model_path)

            # Prepare artifact
            model_pusher_artifact = ModelPusherArtifact(
                saved_model_path=saved_model_path, model_file_path=model_file_path)
            logging.info(f"Model pusher artifact created: {model_pusher_artifact}")
            return model_pusher_artifact
        except Exception as e:
            raise HousePriceException(e, sys)
