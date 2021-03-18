# Summary of 80_Xgboost

[<< Go back](../README.md)


## Extreme Gradient Boosting (Xgboost)
- **n_jobs**: -1
- **objective**: binary:logistic
- **eval_metric**: logloss
- **eta**: 0.075
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

3.7 seconds

## Metric details
|           |    score |    threshold |
|:----------|---------:|-------------:|
| logloss   | 0.317229 | nan          |
| auc       | 0.937467 | nan          |
| f1        | 0.886731 |   0.411175   |
| accuracy  | 0.872727 |   0.475246   |
| precision | 1        |   0.979443   |
| recall    | 1        |   0.00262148 |
| mcc       | 0.744375 |   0.411175   |


## Confusion matrix (at threshold=0.475246)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                     107 |                      19 |
| Labeled as positive |                      16 |                     133 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
