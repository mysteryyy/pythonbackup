# Summary of 82_Xgboost

[<< Go back](../README.md)


## Extreme Gradient Boosting (Xgboost)
- **n_jobs**: -1
- **objective**: binary:logistic
- **eval_metric**: logloss
- **eta**: 0.1
- **max_depth**: 9
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

3.0 seconds

## Metric details
|           |    score |    threshold |
|:----------|---------:|-------------:|
| logloss   | 0.313866 | nan          |
| auc       | 0.939038 | nan          |
| f1        | 0.894737 |   0.436696   |
| accuracy  | 0.883636 |   0.436696   |
| precision | 1        |   0.962309   |
| recall    | 1        |   0.00585887 |
| mcc       | 0.765514 |   0.436696   |


## Confusion matrix (at threshold=0.436696)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                     107 |                      19 |
| Labeled as positive |                      13 |                     136 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
