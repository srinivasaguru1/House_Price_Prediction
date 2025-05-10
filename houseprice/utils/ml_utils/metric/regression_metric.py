from houseprice.entity.artifact_entity import RegressionMetricArtifact
from houseprice.exception.exception import HousePriceException
from sklearn.metrics import mean_absolute_error, mean_squared_error,root_mean_squared_error,r2_score
import os, sys

def get_regression_score(y_true, y_pred) -> RegressionMetricArtifact:
    try:
        # Calculating regression metrics
        model_mae = mean_absolute_error(y_true, y_pred)
        model_mse = mean_squared_error(y_true, y_pred)
        model_rmse = root_mean_squared_error(y_true, y_pred)
        model_r2 = r2_score(y_true, y_pred)

        # Creating a RegressionMetricArtifact object
        regression_metric = RegressionMetricArtifact(
            mae=model_mae,
            mse=model_mse,
            rmse=model_rmse,
            r2_score=model_r2
        )
        return regression_metric

    except Exception as e:
        raise HousePriceException(e, sys)