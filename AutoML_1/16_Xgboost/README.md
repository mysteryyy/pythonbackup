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
| logloss   | 0.687554   |  nan        |
| auc       | 0.503468   |  nan        |
| f1        | 0.618102   |    0.399755 |
| accuracy  | 0.533546   |    0.451303 |
| precision | 0.451613   |    0.448271 |
| recall    | 1          |    0.399755 |
| mcc       | 0.00705148 |    0.448271 |


## Confusion matrix (at threshold=0.451303)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                     139 |                      34 |
| Labeled as positive |                     112 |                      28 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
