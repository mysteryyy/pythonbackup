# Summary of 6_Default_Xgboost

[<< Go back](../README.md)


## Extreme Gradient Boosting (Xgboost)
- **n_jobs**: -1
- **objective**: binary:logistic
- **eval_metric**: logloss
- **eta**: 0.075
- **max_depth**: 6
- **min_child_weight**: 1
- **subsample**: 1.0
- **colsample_bytree**: 1.0
- **explain_level**: 0

## Validation
 - **validation_type**: kfold
 - **shuffle**: True
 - **stratify**: True
 - **k_folds**: 5

## Optimized metric
logloss

## Training time

1.5 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.677681 |  nan        |
| auc       | 0.594871 |  nan        |
| f1        | 0.666667 |    0.387368 |
| accuracy  | 0.589091 |    0.526245 |
| precision | 0.777778 |    0.737201 |
| recall    | 1        |    0.125738 |
| mcc       | 0.183148 |    0.526245 |


## Confusion matrix (at threshold=0.526245)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                     110 |                      31 |
| Labeled as positive |                      82 |                      52 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
