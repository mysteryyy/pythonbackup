# Summary of 18_Xgboost

[<< Go back](../README.md)


## Extreme Gradient Boosting (Xgboost)
- **n_jobs**: -1
- **objective**: binary:logistic
- **eval_metric**: logloss
- **eta**: 0.1
- **max_depth**: 6
- **min_child_weight**: 5
- **subsample**: 0.5
- **colsample_bytree**: 0.8
- **explain_level**: 0

## Validation
 - **validation_type**: kfold
 - **shuffle**: True
 - **stratify**: True
 - **k_folds**: 5

## Optimized metric
logloss

## Training time

1.4 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.643937 |  nan        |
| auc       | 0.67019  |  nan        |
| f1        | 0.651629 |    0.303804 |
| accuracy  | 0.638978 |    0.464225 |
| precision | 0.714286 |    0.722163 |
| recall    | 1        |    0.112855 |
| mcc       | 0.275958 |    0.464225 |


## Confusion matrix (at threshold=0.464225)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                     111 |                      62 |
| Labeled as positive |                      51 |                      89 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
