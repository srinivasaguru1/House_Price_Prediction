from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import RandomizedSearchCV
import os
import sys
from houseprice.exception.exception import HousePriceException
from houseprice.logger.logger import logging
from houseprice.entity.artifact_entity import DataTransformationArtifact, ModelTrainerArtifact
from houseprice.entity.config_entity import ModelTrainerConfig
from houseprice.utils.ml_utils.model.estimator import HouseModel
from houseprice.utils.main_utils.utils import save_object, load_object
from houseprice.utils.main_utils.utils import load_numpy_array_data
from houseprice.utils.ml_utils.metric.regression_metric import get_regression_score
from houseprice.constant.training_pipeline import PARAM_GRID

class ModelTrainer:

    def __init__(self, model_trainer_config: ModelTrainerConfig,
                 data_transformation_artifact: DataTransformationArtifact):
        try:
            self.model_trainer_config = model_trainer_config
            self.data_transformation_artifact = data_transformation_artifact
        except Exception as e:
            raise HousePriceException(e, sys)

    def train_model_with_hyperparameter_tuning(self, x_train, y_train):
        try:
            # Initialize RandomForestRegressor
            rf_reg = RandomForestRegressor(random_state=42)



            # RandomizedSearchCV to tune hyperparameters (using RandomForestRegressor)
            random_search = RandomizedSearchCV(estimator=rf_reg, param_distributions=PARAM_GRID, 
                                               n_iter=100, cv=3, verbose=2, random_state=42, n_jobs=-1)

            # Train the model with the best parameters found from the search
            random_search.fit(x_train, y_train)
            logging.info(f"Best parameters found: {random_search.best_params_}")
            logging.info(f"Best score from RandomizedSearchCV: {random_search.best_score_}")

            # Return the best estimator
            return random_search.best_estimator_

        except Exception as e:
            raise HousePriceException(e, sys)

    def initiate_model_trainer(self) -> ModelTrainerArtifact:
        try:
            train_file_path = self.data_transformation_artifact.transformed_train_file_path
            test_file_path = self.data_transformation_artifact.transformed_test_file_path

            # Load training and testing data
            train_arr = load_numpy_array_data(train_file_path)
            test_arr = load_numpy_array_data(test_file_path)

            x_train, y_train, x_test, y_test = (
                train_arr[:, 1:],  # Features from train data
                train_arr[:, 0],   # Target from train data
                test_arr[:, 1:],   # Features from test data
                test_arr[:, 0],    # Target from test data
            )

            # Train the model using hyperparameter tuning
            model = self.train_model_with_hyperparameter_tuning(x_train, y_train)

            # Predictions and evaluation on training data
            y_train_pred = model.predict(x_train)
            train_metric = get_regression_score(y_true=y_train, y_pred=y_train_pred)

            if train_metric.r2_score <= self.model_trainer_config.expected_accuracy:
                print("Trained model is not good to provide expected accuracy")

            # Predictions and evaluation on test data
            y_test_pred = model.predict(x_test)
            test_metric = get_regression_score(y_true=y_test, y_pred=y_test_pred)

            # Overfitting and underfitting check (percentage difference)
            diff = abs(train_metric.r2_score - test_metric.r2_score) / max(abs(train_metric.r2_score), abs(test_metric.r2_score))
            if diff > self.model_trainer_config.overfitting_underfitting_threshold:
                print(diff)
                raise Exception("Model is not good, try to do more experimentation.")

            # Load preprocessor and save the model
            preprocessor = load_object(self.data_transformation_artifact.transformed_object_file_path)
            house_model = HouseModel(preprocessor=preprocessor, model=model)
            save_object(self.model_trainer_config.trained_model_file_path, obj=house_model)

            # Create model trainer artifact
            model_trainer_artifact = ModelTrainerArtifact(
                trained_model_file_path=self.model_trainer_config.trained_model_file_path,
                train_metric_artifact=train_metric,
                test_metric_artifact=test_metric
            )

            logging.info(f"Model trainer artifact created: {model_trainer_artifact}")
            return model_trainer_artifact

        except Exception as e:
            raise HousePriceException(e, sys)