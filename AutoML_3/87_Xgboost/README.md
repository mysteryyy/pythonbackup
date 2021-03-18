# Summary of 87_Xgboost

[<< Go back](../README.md)


## Extreme Gradient Boosting (Xgboost)
- **n_jobs**: -1
- **objective**: binary:logistic
- **eval_metric**: logloss
- **eta**: 0.1
- **max_depth**: 6
- **min_child_weight**: 5
- **subsample**: 0.6
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

0.9 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.651832 |  nan        |
| auc       | 0.651212 |  nan        |
| f1        | 0.666667 |    0.326964 |
| accuracy  | 0.632727 |    0.543307 |
| precision | 0.941176 |    0.76839  |
| recall    | 1        |    0.113049 |
| mcc       | 0.270019 |    0.543307 |


## Confusion matrix (at threshold=0.543307)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                     109 |                      32 |
| Labeled as positive |                      69 |                      65 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
