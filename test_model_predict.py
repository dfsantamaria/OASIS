import numpy as np
import lightgbm as lgb
import pytest

@pytest.fixture
def lgb_data():
    """Return a tiny toy dataset for training and testing.

    Returns:
        Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]: (X_train, y_train, X_test, y_test)
    """
    X_train = np.array([[1, 2], [3, 4], [5, 6], [1, 2], [3, 4], [5, 6]])
    y_train = np.array([0, 1, 0, 0, 1, 0])
    X_test = np.array([[1, 2], [3, 4], [5, 6]])
    y_test = np.array([0, 1, 0])
    return X_train, y_train, X_test, y_test

@pytest.fixture
def lgbm_model(lgb_data):
    """Train a small LightGBM classifier on the toy dataset.

    Use deterministic parameters for reproducible tests.
    """
    X_train, y_train, _, _ = lgb_data
    model = lgb.LGBMClassifier(
        num_leaves=3,
        min_child_samples=1,
        min_data_in_leaf=1,
        random_state=0,
    )
    model.fit(X_train, y_train)
    return model

def test_lgbm_predict_shape(lgbm_model, lgb_data):
    """The model should return predictions for each test sample."""
    _, _, X_test, _ = lgb_data
    preds = lgbm_model.predict(X_test)
    assert preds.shape == (X_test.shape[0],)

def test_lgbm_accuracy_at_least_random_baseline(lgbm_model, lgb_data):
    """Model accuracy should be at or above a simple baseline on this toy data."""
    _, _, X_test, y_test = lgb_data
    acc = lgbm_model.score(X_test, y_test)
    # On this tiny deterministic dataset we expect at least 50% accuracy.
    assert acc >= 0.5