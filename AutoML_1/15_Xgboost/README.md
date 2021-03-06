# Summary of 15_Xgboost

[<< Go back](../README.md)


## Extreme Gradient Boosting (Xgboost)
- **n_jobs**: -1
- **objective**: binary:logistic
- **eval_metric**: auc
- **eta**: 0.15
- **max_depth**: 8
- **min_child_weight**: 25
- **subsample**: 0.6
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

8.8 seconds

## Metric details
|           |      score |   threshold |
|:----------|-----------:|------------:|
| logloss   | 0.691451   |  nan        |
| auc       | 0.498844   |  nan        |
| f1        | 0.618102   |    0.439521 |
| accuracy  | 0.507987   |    0.492547 |
| precision | 0.448      |    0.488822 |
| recall    | 1          |    0.439521 |
| mcc       | 0.00286722 |    0.488822 |


## Confusion matrix (at threshold=0.492547)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                     103 |                      70 |
| Labeled as positive |                      84 |                      56 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
