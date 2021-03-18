# Summary of 13_Xgboost

[<< Go back](../README.md)


## Extreme Gradient Boosting (Xgboost)
- **n_jobs**: -1
- **objective**: binary:logistic
- **eval_metric**: logloss
- **eta**: 0.1
- **max_depth**: 8
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

1.3 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.676916 |  nan        |
| auc       | 0.58852  |  nan        |
| f1        | 0.661728 |    0.255027 |
| accuracy  | 0.581818 |    0.534968 |
| precision | 0.833333 |    0.675603 |
| recall    | 1        |    0.183399 |
| mcc       | 0.178505 |    0.627282 |


## Confusion matrix (at threshold=0.534968)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                     109 |                      32 |
| Labeled as positive |                      83 |                      51 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
