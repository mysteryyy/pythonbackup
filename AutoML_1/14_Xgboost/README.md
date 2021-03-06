# Summary of 14_Xgboost

[<< Go back](../README.md)


## Extreme Gradient Boosting (Xgboost)
- **n_jobs**: -1
- **objective**: binary:logistic
- **eval_metric**: logloss
- **eta**: 0.1
- **max_depth**: 7
- **min_child_weight**: 25
- **subsample**: 0.9
- **colsample_bytree**: 0.6
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
| logloss   | 0.664572 |  nan        |
| auc       | 0.620252 |  nan        |
| f1        | 0.635616 |    0.373429 |
| accuracy  | 0.616613 |    0.431675 |
| precision | 0.875    |    0.589456 |
| recall    | 1        |    0.235542 |
| mcc       | 0.242982 |    0.431675 |


## Confusion matrix (at threshold=0.431675)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                      99 |                      74 |
| Labeled as positive |                      46 |                      94 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
