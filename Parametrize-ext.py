@pytest.mark.parametrize("expected_accuracy", [0.66])
def test_model_accuracy(lgbm_model, lgb_data, expected_accuracy):
    _, _, X_test, y_test = lgb_data
    predictions = lgbm_model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    assert accuracy >= expected_accuracy
    np.testing.assert_array_equal(predictions, y_test)