# Summary of 20_Xgboost

[<< Go back](../README.md)


## Extreme Gradient Boosting (Xgboost)
- **n_jobs**: -1
- **objective**: binary:logistic
- **eval_metric**: logloss
- **eta**: 0.05
- **max_depth**: 7
- **min_child_weight**: 1
- **subsample**: 0.9
- **colsample_bytree**: 0.9
- **explain_level**: 0

## Validation
 - **validation_type**: kfold
 - **shuffle**: True
 - **stratify**: True
 - **k_folds**: 5

## Optimized metric
logloss

## Training time

2.8 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.668292 |  nan        |
| auc       | 0.61507  |  nan        |
| f1        | 0.639344 |    0.444051 |
| accuracy  | 0.603834 |    0.545938 |
| precision | 1        |    0.791787 |
| recall    | 1        |    0.141914 |
| mcc       | 0.228253 |    0.444051 |


## Confusion matrix (at threshold=0.545938)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                     152 |                      21 |
| Labeled as positive |                     103 |                      37 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
