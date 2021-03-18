# Summary of 15_Xgboost

[<< Go back](../README.md)


## Extreme Gradient Boosting (Xgboost)
- **n_jobs**: -1
- **objective**: binary:logistic
- **eval_metric**: auc
- **eta**: 0.15
- **max_depth**: 8
- **min_child_weight**: 25
- **subsample**: 0.6
- **colsample_bytree**: 0.6
- **explain_level**: 0

## Validation
 - **validation_type**: kfold
 - **shuffle**: True
 - **stratify**: True
 - **k_folds**: 5

## Optimized metric
logloss

## Training time

9.1 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.693043 |  nan        |
| auc       | 0.494178 |  nan        |
| f1        | 0.655257 |    0.442395 |
| accuracy  | 0.501818 |    0.493662 |
| precision | 0.487273 |    0.442395 |
| recall    | 1        |    0.442395 |
| mcc       | 0        |    0.442395 |


## Confusion matrix (at threshold=0.493662)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                     112 |                      29 |
| Labeled as positive |                     108 |                      26 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
