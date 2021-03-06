# Summary of 107_Xgboost_SelectedFeatures

[<< Go back](../README.md)


## Extreme Gradient Boosting (Xgboost)
- **n_jobs**: -1
- **objective**: binary:logistic
- **eval_metric**: logloss
- **eta**: 0.075
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

1.3 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.622907 |  nan        |
| auc       | 0.701631 |  nan        |
| f1        | 0.662757 |    0.368535 |
| accuracy  | 0.670927 |    0.472168 |
| precision | 1        |    0.764142 |
| recall    | 1        |    0.092374 |
| mcc       | 0.345507 |    0.442599 |


## Confusion matrix (at threshold=0.472168)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                     119 |                      54 |
| Labeled as positive |                      49 |                      91 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
