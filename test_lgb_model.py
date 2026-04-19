import lightgbm as lgb
import numpy as np
import pandas as pd
import pytest
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def test_model_prediction():
    X, y = make_classification(n_samples=100, n_features=20, n_informative=10, random_state=42)
    feature_names = [f"feature_{i}" for i in range(X.shape[1])]
    X_df = pd.DataFrame(X, columns=feature_names)
    X_train, X_test, y_train, y_test = train_test_split(X_df, y, test_size=0.2, random_state=42)

    model = lgb.LGBMClassifier(n_estimators=20, random_state=42, verbosity=-1, min_child_samples=1)
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)

    assert accuracy > 0.7, f"Model accuracy {accuracy} is below threshold!"
    assert len(predictions) == len(y_test)
    assert np.issubdtype(predictions.dtype, np.integer)


if __name__ == '__main__':
    pytest.main()