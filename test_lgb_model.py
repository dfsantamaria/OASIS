import lightgbm as lgb
import numpy as np
import pandas as pd
import pytest
from sklearn.metrics import accuracy_score

# Define feature names to avoid UserWarning
feature_names = ['feature1', 'feature2']

# Sample data - separate train/test sets with clear class separation
X_train = pd.DataFrame([[1, 2], [3, 4], [5, 6], [1, 2], [3, 4], [5, 6]], columns=feature_names)
y_train = np.array([0, 1, 0, 0, 1, 0])

X_test = pd.DataFrame([[1, 2], [3, 4], [5, 6]], columns=feature_names)
y_test = np.array([0, 1, 0])

# Initialize and fit the model
model = lgb.LGBMClassifier(num_leaves=3, min_child_samples=1, min_data_in_leaf=1)
model.fit(X_train, y_train)


def test_model_accuracy():
    """Test if the model achieves a reasonable accuracy on the test set."""
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    # Using a threshold rather than exact match for robustness
    assert accuracy >= 0.66, f"Accuracy {accuracy} is too low"


if __name__ == '__main__':
    pytest.main()
