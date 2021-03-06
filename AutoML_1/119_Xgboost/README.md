# Summary of 119_Xgboost

[<< Go back](../README.md)


## Extreme Gradient Boosting (Xgboost)
- **n_jobs**: -1
- **objective**: binary:logistic
- **eval_metric**: logloss
- **eta**: 0.15
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

1.3 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.640396 | nan         |
| auc       | 0.671965 | nan         |
| f1        | 0.641509 |   0.239991  |
| accuracy  | 0.651757 |   0.558215  |
| precision | 1        |   0.860476  |
| recall    | 1        |   0.0805039 |
| mcc       | 0.2881   |   0.558215  |


## Confusion matrix (at threshold=0.558215)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                     145 |                      28 |
| Labeled as positive |                      81 |                      59 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
