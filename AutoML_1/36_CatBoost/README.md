# Summary of 36_CatBoost

[<< Go back](../README.md)


## CatBoost
- **n_jobs**: -1
- **learning_rate**: 0.025
- **depth**: 8
- **rsm**: 1.0
- **loss_function**: Logloss
- **explain_level**: 0

## Validation
 - **validation_type**: kfold
 - **shuffle**: True
 - **stratify**: True
 - **k_folds**: 5

## Optimized metric
logloss

## Training time

8.9 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.657908 |  nan        |
| auc       | 0.640091 |  nan        |
| f1        | 0.63908  |    0.304188 |
| accuracy  | 0.626198 |    0.511671 |
| precision | 0.705882 |    0.625457 |
| recall    | 1        |    0.170977 |
| mcc       | 0.231241 |    0.511671 |


## Confusion matrix (at threshold=0.511671)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                     134 |                      39 |
| Labeled as positive |                      78 |                      62 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
