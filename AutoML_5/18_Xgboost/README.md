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
 - **k_folds**: 10

## Optimized metric
logloss

## Training time

1.9 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.43995  | nan         |
| auc       | 0.880526 | nan         |
| f1        | 0.83125  |   0.411388  |
| accuracy  | 0.803636 |   0.411388  |
| precision | 1        |   0.956968  |
| recall    | 1        |   0.0113589 |
| mcc       | 0.619604 |   0.618866  |


## Confusion matrix (at threshold=0.411388)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                      88 |                      38 |
| Labeled as positive |                      16 |                     133 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
