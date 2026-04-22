import pytest

@pytest.fixture
def lgb_data():
    X_train = np.array([[1, 2], [3, 4], [5, 6], [1, 2], [3, 4], [5, 6]])
    y_train = np.array([0, 1, 0, 0, 1, 0])
    X_test = np.array([[1, 2], [3, 4], [5, 6]])
    y_test = np.array([0, 1, 0])
    return X_train, y_train, X_test, y_test

@pytest.fixture
def lgbm_model(lgb_data):
    X_train, y_train, _, _ = lgb_data
    model = lgb.LGBMClassifier(num_leaves=3, min_child_samples=1, min_data_in_leaf=1)
    model.fit(X_train, y_train)
    return model