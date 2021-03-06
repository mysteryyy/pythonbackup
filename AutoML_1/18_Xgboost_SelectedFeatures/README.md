# Summary of 18_Xgboost_SelectedFeatures

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
 - **k_folds**: 5

## Optimized metric
logloss

## Training time

1.4 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.622468 | nan         |
| auc       | 0.69967  | nan         |
| f1        | 0.658354 |   0.283226  |
| accuracy  | 0.667732 |   0.480586  |
| precision | 0.857143 |   0.788257  |
| recall    | 1        |   0.0959881 |
| mcc       | 0.327104 |   0.480586  |


## Confusion matrix (at threshold=0.480586)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                     122 |                      51 |
| Labeled as positive |                      53 |                      87 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
