import sys
import os
import numpy as np
import pandas as pd
from sklearn.impute import KNNImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer

from houseprice.constant.training_pipeline import TARGET_COLUMN,NUMERICAL_COLUMNS,CATEGORICAL_COLUMNS
from houseprice.constant.training_pipeline import DATA_TRANSFORMATION_IMPUTER_PARAMS
from houseprice.entity.artifact_entity import (
    DataTransformationArtifact,
    DataValidationArtifact,
)
from houseprice.entity.config_entity import DataTransformationConfig
from houseprice.exception.exception import HousePriceException 
from houseprice.logger.logger import logging
#from houseprice.utils.ml_utils.model.estimator import TargetValueMapping
from houseprice.utils.main_utils.utils import save_numpy_array_data, save_object




class DataTransformation:
    def __init__(self,data_validation_artifact: DataValidationArtifact, 
                    data_transformation_config: DataTransformationConfig,):
        """

        :param data_validation_artifact: Output reference of data ingestion artifact stage
        :param data_transformation_config: configuration for data transformation
        """
        try:
            self.data_validation_artifact: DataValidationArtifact = data_validation_artifact
            self.data_transformation_config: DataTransformationConfig = data_transformation_config

        except Exception as e:
            raise HousePriceException(e, sys)


    @staticmethod
    def read_data(file_path) -> pd.DataFrame:
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            raise HousePriceException(e, sys)


    from sklearn.compose import ColumnTransformer

    def get_data_transformer_object(cls) -> Pipeline:
        """
        Initializes a transformation pipeline that handles both numerical and categorical features.

        Returns:
            A Pipeline object with preprocessing steps.
        """
        logging.info("Entered get_data_transformer_object method of DataTransformation class")

        try:
            imputer = KNNImputer(**DATA_TRANSFORMATION_IMPUTER_PARAMS)
            scaler = StandardScaler()
            encoder = OneHotEncoder()

            logging.info(f"Initializing KNNImputer with {DATA_TRANSFORMATION_IMPUTER_PARAMS}")

            # Defining the transformers for numerical and categorical columns
            numeric_transformer = Pipeline(steps=[
                ("imputer", imputer),
                ("scaler", scaler)
            ])

            categorical_transformer = Pipeline(steps=[
                ("encoder", encoder)
            ])

            # ColumnTransformer to handle both numerical and categorical transformations
            preprocessor = ColumnTransformer(
                transformers=[
                    ("num", numeric_transformer, NUMERICAL_COLUMNS),
                    ("cat", categorical_transformer, CATEGORICAL_COLUMNS)
                ]
            )

            logging.info("Exited get_data_transformer_object method of DataTransformation class")
            return preprocessor

        except Exception as e:
            raise HousePriceException(e, sys)

    
    def initiate_data_transformation(self,) -> DataTransformationArtifact:
        logging.info("Entered initiate_data_transformation method of DataTransformation class")

        try:
            logging.info("Starting data transformation")
            
            #os.makedirs(self.data_transformation_config.transformed_data_dir, exist_ok=True)
            
            train_df = DataTransformation.read_data(self.data_validation_artifact.valid_train_file_path)
            test_df = DataTransformation.read_data(self.data_validation_artifact.valid_test_file_path)
            preprocessor = self.get_data_transformer_object()
            
            logging.info("Got the preprocessor object")

            #training dataframe
            input_feature_train_df = train_df.drop(columns=[TARGET_COLUMN], axis=1)
            target_feature_train_df = train_df[TARGET_COLUMN]

            #testing dataframe
            input_feature_test_df = test_df.drop(columns=[TARGET_COLUMN], axis=1)
            target_feature_test_df = test_df[TARGET_COLUMN]
            
            preprocessor_object = preprocessor.fit(input_feature_train_df)
            transformed_input_train_feature = preprocessor_object.transform(input_feature_train_df)
            transformed_input_test_feature =preprocessor_object.transform(input_feature_test_df)
            

            train_arr = np.c_[transformed_input_train_feature, np.array(target_feature_train_df) ]
            test_arr = np.c_[ transformed_input_test_feature, np.array(target_feature_test_df) ]

            #save numpy array data
            save_numpy_array_data( self.data_transformation_config.transformed_train_file_path, array=train_arr, )
            save_numpy_array_data( self.data_transformation_config.transformed_test_file_path,array=test_arr,)
            save_object( self.data_transformation_config.transformed_object_file_path, preprocessor_object,)
            
            
            #preparing artifact
            data_transformation_artifact = DataTransformationArtifact(
                transformed_object_file_path=self.data_transformation_config.transformed_object_file_path,
                transformed_train_file_path=self.data_transformation_config.transformed_train_file_path,
                transformed_test_file_path=self.data_transformation_config.transformed_test_file_path,
            )
            logging.info(f"Data transformation artifact: {data_transformation_artifact}")
            return data_transformation_artifact
        except Exception as e:
            raise HousePriceException(e, sys) from e