# AutoML Leaderboard

| Best model   | name                                                         | model_type     | metric_type   |   metric_value |   train_time |
|:-------------|:-------------------------------------------------------------|:---------------|:--------------|---------------:|-------------:|
|              | [1_DecisionTree](1_DecisionTree/README.md)                   | Decision Tree  | logloss       |       0.801326 |         1.03 |
|              | [2_DecisionTree](2_DecisionTree/README.md)                   | Decision Tree  | logloss       |       1.49663  |         0.42 |
|              | [3_DecisionTree](3_DecisionTree/README.md)                   | Decision Tree  | logloss       |       1.26808  |         0.44 |
|              | [4_Linear](4_Linear/README.md)                               | Linear         | logloss       |       0.651103 |         2.95 |
|              | [5_Default_LightGBM](5_Default_LightGBM/README.md)           | LightGBM       | logloss       |       0.301896 |         1.45 |
|              | [6_Default_Xgboost](6_Default_Xgboost/README.md)             | Xgboost        | logloss       |       0.345206 |         2.14 |
| **the best** | [7_Default_CatBoost](7_Default_CatBoost/README.md)           | CatBoost       | logloss       |       0.292358 |         4.73 |
|              | [8_Default_NeuralNetwork](8_Default_NeuralNetwork/README.md) | Neural Network | logloss       |       0.688063 |         0.98 |

### AutoML Performance
![AutoML Performance](ldb_performance.png)

### AutoML Performance Boxplot
![AutoML Performance Boxplot](ldb_performance_boxplot.png)