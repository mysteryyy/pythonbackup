# Summary of 118_Xgboost

[<< Go back](../README.md)


## Extreme Gradient Boosting (Xgboost)
- **n_jobs**: -1
- **objective**: binary:logistic
- **eval_metric**: logloss
- **eta**: 0.075
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

1.5 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.644637 |  nan        |
| auc       | 0.670396 |  nan        |
| f1        | 0.666667 |    0.379224 |
| accuracy  | 0.632588 |    0.462644 |
| precision | 0.818182 |    0.66657  |
| recall    | 1        |    0.16914  |
| mcc       | 0.299968 |    0.379224 |


## Confusion matrix (at threshold=0.462644)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                     107 |                      66 |
| Labeled as positive |                      49 |                      91 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
