import pytest
import numpy as np
import pandas as pd
from ml.data import process_data
from ml.model import compute_model_metrics, inference, train_model

# TODO: implement the first test. Change the function name and input as needed
def test_process_data():
    """
    Test that process_data returns the expected number of rows
    """
    data = pd.DataFrame(
        {
            "age": [25,40,60],
            "workclass": ["Private", "State-gov", "Private"],
            "salary": ["<=50K", ">50K", ">50K"],
        }
    )

    X, y, encoder, lb = process_data(
        data,
        categorical_features=["workclass"],
        label="salary",
        training=True,
    )

    assert X.shape[0] == 3
    assert len(y) == 3
    assert encoder is not None
    assert lb is not None

# TODO: implement the second test. Change the function name and input as needed
def test_train_model_and_inference():
    """
    Test that the model trains and returns predictions.
    """
    X = np.array(
        [
            [20,0],
            [25,0],
            [50,1],
            [60,1],
        ]
    )
    y = np.array([0,0,1,1,])

    model = train_model(X, y)
    preds = inference(model, X)

    assert len(preds) == len(y)
    assert set(preds).issubset({0,1})


# TODO: implement the third test. Change the function name and input as needed
def test_compute_model_metrics():
    """
    Test that model metrics return expected values.
    """
    y = np.array([0,1,1,0])
    preds = np.array([0,1,0,0])

    precision, recall, fbeta = compute_model_metrics(y, preds)

    assert precision == 1.0
    assert recall == 0.5
    assert round(fbeta,4) == 0.6667
