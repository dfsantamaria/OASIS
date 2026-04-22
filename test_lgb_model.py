import lightgbm as lgb
import numpy as np
import pandas as pd
import pytest
from sklearn.metrics import accuracy_score

feature_names = ['feature1', 'feature2']

X_train = pd.DataFrame([[1, 2], [3, 4], [5, 6], [1, 2], [3, 4], [5, 6]], columns=feature_names)
y_train = np.array([0, 1, 0, 0, 1, 0])

X_test = pd.DataFrame([[1, 2], [3, 4], [5, 6]], columns=feature_names)
y_test = np.array([0, 1, 0])

model = lgb.LGBMClassifier(num_leaves=3, min_child_samples=1, min_data_in_leaf=1)
model.fit(X_train, y_train)

def test_model_accuracy():
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    assert accuracy >= 0.66, f"Accuracy {accuracy} is too low"

if __name__ == '__main__':
    pytest.main()
