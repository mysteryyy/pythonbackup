# Summary of 17_Xgboost

[<< Go back](../README.md)


## Extreme Gradient Boosting (Xgboost)
- **n_jobs**: -1
- **objective**: binary:logistic
- **eval_metric**: logloss
- **eta**: 0.15
- **max_depth**: 4
- **min_child_weight**: 25
- **subsample**: 0.7
- **colsample_bytree**: 0.7
- **explain_level**: 0

## Validation
 - **validation_type**: kfold
 - **shuffle**: True
 - **stratify**: True
 - **k_folds**: 10

## Optimized metric
logloss

## Training time

1.1 seconds

## Metric details
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 0.689361  |  nan        |
| auc       | 0.512597  |  nan        |
| f1        | 0.70283   |    0.467753 |
| accuracy  | 0.541818  |    0.467753 |
| precision | 0.555556  |    0.554047 |
| recall    | 1         |    0.467753 |
| mcc       | 0.0221723 |    0.537915 |


## Confusion matrix (at threshold=0.467753)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                       0 |                     126 |
| Labeled as positive |                       0 |                     149 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
