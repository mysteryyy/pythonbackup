# Summary of 108_Xgboost_SelectedFeatures

[<< Go back](../README.md)


## Extreme Gradient Boosting (Xgboost)
- **n_jobs**: -1
- **objective**: binary:logistic
- **eval_metric**: logloss
- **eta**: 0.15
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

1.2 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.62401  | nan         |
| auc       | 0.702581 | nan         |
| f1        | 0.666667 |   0.390738  |
| accuracy  | 0.661342 |   0.527569  |
| precision | 0.75     |   0.776331  |
| recall    | 1        |   0.0840544 |
| mcc       | 0.323161 |   0.390738  |


## Confusion matrix (at threshold=0.527569)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                     135 |                      38 |
| Labeled as positive |                      68 |                      72 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
