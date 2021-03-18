# Summary of 16_Xgboost

[<< Go back](../README.md)


## Extreme Gradient Boosting (Xgboost)
- **n_jobs**: -1
- **objective**: binary:logistic
- **eval_metric**: logloss
- **eta**: 0.1
- **max_depth**: 6
- **min_child_weight**: 50
- **subsample**: 0.9
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

0.6 seconds

## Metric details
|           |      score |   threshold |
|:----------|-----------:|------------:|
| logloss   | 0.692846   |  nan        |
| auc       | 0.502911   |  nan        |
| f1        | 0.655257   |    0.441336 |
| accuracy  | 0.509091   |    0.491017 |
| precision | 0.490909   |    0.490675 |
| recall    | 1          |    0.441336 |
| mcc       | 0.00891012 |    0.490632 |


## Confusion matrix (at threshold=0.491017)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                     113 |                      28 |
| Labeled as positive |                     107 |                      27 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
