# Summary of 81_Xgboost

[<< Go back](../README.md)


## Extreme Gradient Boosting (Xgboost)
- **n_jobs**: -1
- **objective**: binary:logistic
- **eval_metric**: logloss
- **eta**: 0.1
- **max_depth**: 7
- **min_child_weight**: 1
- **subsample**: 1.0
- **colsample_bytree**: 1.0
- **explain_level**: 0

## Validation
 - **validation_type**: kfold
 - **shuffle**: True
 - **stratify**: True
 - **k_folds**: 10

## Optimized metric
logloss

## Training time

3.3 seconds

## Metric details
|           |    score |    threshold |
|:----------|---------:|-------------:|
| logloss   | 0.31478  | nan          |
| auc       | 0.937227 | nan          |
| f1        | 0.88961  |   0.392365   |
| accuracy  | 0.876364 |   0.392365   |
| precision | 1        |   0.961743   |
| recall    | 1        |   0.00391076 |
| mcc       | 0.751494 |   0.392365   |


## Confusion matrix (at threshold=0.392365)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                     104 |                      22 |
| Labeled as positive |                      12 |                     137 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
