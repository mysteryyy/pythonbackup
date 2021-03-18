# Summary of 32_CatBoost

[<< Go back](../README.md)


## CatBoost
- **n_jobs**: -1
- **learning_rate**: 0.1
- **depth**: 7
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

2.7 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.672803 |  nan        |
| auc       | 0.614587 |  nan        |
| f1        | 0.655257 |    0.177659 |
| accuracy  | 0.603636 |    0.473534 |
| precision | 0.8      |    0.720381 |
| recall    | 1        |    0.177659 |
| mcc       | 0.218997 |    0.473534 |


## Confusion matrix (at threshold=0.473534)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                      69 |                      72 |
| Labeled as positive |                      37 |                      97 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
