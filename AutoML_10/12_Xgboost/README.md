# Summary of 12_Xgboost

[<< Go back](../README.md)


## Extreme Gradient Boosting (Xgboost)
- **n_jobs**: -1
- **objective**: binary:logistic
- **eval_metric**: logloss
- **eta**: 0.05
- **max_depth**: 8
- **min_child_weight**: 5
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

9.2 seconds

## Metric details
|           |    score |    threshold |
|:----------|---------:|-------------:|
| logloss   | 0.494823 | nan          |
| auc       | 0.838291 | nan          |
| f1        | 0.797742 |   0.375707   |
| accuracy  | 0.776573 |   0.428392   |
| precision | 1        |   0.977592   |
| recall    | 1        |   0.00772598 |
| mcc       | 0.558126 |   0.428392   |


## Confusion matrix (at threshold=0.428392)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                     311 |                     139 |
| Labeled as positive |                      67 |                     405 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
