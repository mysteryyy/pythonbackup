# Summary of 6_Default_Xgboost

[<< Go back](../README.md)


## Extreme Gradient Boosting (Xgboost)
- **n_jobs**: -1
- **objective**: binary:logistic
- **eval_metric**: logloss
- **eta**: 0.075
- **max_depth**: 6
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

3.2 seconds

## Metric details
|           |    score |    threshold |
|:----------|---------:|-------------:|
| logloss   | 0.310859 | nan          |
| auc       | 0.941355 | nan          |
| f1        | 0.89404  |   0.470336   |
| accuracy  | 0.883636 |   0.470336   |
| precision | 1        |   0.955931   |
| recall    | 1        |   0.00479413 |
| mcc       | 0.765388 |   0.470336   |


## Confusion matrix (at threshold=0.470336)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                     108 |                      18 |
| Labeled as positive |                      14 |                     135 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
