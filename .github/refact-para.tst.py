import lightgbm as lgb
import numpy as np
import pytest
from sklearn.metrics import accuracy_score

# Sample data (train/test splits)
test_cases = [
    # (X_train, y_train, X_test, y_test, expected_accuracy)
    (
        np.array([[1, 2], [3, 4], [5, 6], [1, 2], [3, 4], [5, 6]]),
        np.array([0, 1, 0, 0, 1, 0]),
        np.array([[1, 2], [3, 4], [5, 6]]),
        np.array([0, 1, 0]),
        0.66
    ),
    # Add more cases as needed
]

@pytest.mark.parametrize(
    "X_train, y_train, X_test, y_test, expected_accuracy", test_cases
)
def test_model_accuracy(X_train, y_train, X_test, y_test, expected_accuracy):
    model = lgb.LGBMClassifier(num_leaves=3, min_child_samples=1, min_data_in_leaf=1)
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    assert accuracy >= expected_accuracy, f"Accuracy {accuracy} is less than {expected_accuracy}"
    np.testing.assert_array_equal(predictions, y_test)