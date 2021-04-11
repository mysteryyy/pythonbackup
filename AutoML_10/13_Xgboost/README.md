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
 - **k_folds**: 10

## Optimized metric
logloss

## Training time

7.4 seconds

## Metric details
|           |    score |    threshold |
|:----------|---------:|-------------:|
| logloss   | 0.437473 | nan          |
| auc       | 0.877048 | nan          |
| f1        | 0.814061 |   0.300605   |
| accuracy  | 0.79718  |   0.559659   |
| precision | 1        |   0.987479   |
| recall    | 1        |   0.00261279 |
| mcc       | 0.59489  |   0.559659   |


## Confusion matrix (at threshold=0.559659)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                     365 |                      85 |
| Labeled as positive |                     102 |                     370 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
