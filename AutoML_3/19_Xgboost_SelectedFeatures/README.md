# Summary of 19_Xgboost_SelectedFeatures

[<< Go back](../README.md)


## Extreme Gradient Boosting (Xgboost)
- **n_jobs**: -1
- **objective**: binary:logistic
- **eval_metric**: logloss
- **eta**: 0.075
- **max_depth**: 8
- **min_child_weight**: 10
- **subsample**: 1.0
- **colsample_bytree**: 0.7
- **explain_level**: 0

## Validation
 - **validation_type**: kfold
 - **shuffle**: True
 - **stratify**: True
 - **k_folds**: 5

## Optimized metric
logloss

## Training time

1.0 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.65014  |  nan        |
| auc       | 0.655631 |  nan        |
| f1        | 0.677165 |    0.310276 |
| accuracy  | 0.629091 |    0.478428 |
| precision | 0.863636 |    0.6763   |
| recall    | 1        |    0.104155 |
| mcc       | 0.262414 |    0.478428 |


## Confusion matrix (at threshold=0.478428)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                      81 |                      60 |
| Labeled as positive |                      42 |                      92 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
