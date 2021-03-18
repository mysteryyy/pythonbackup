# Summary of 31_CatBoost

[<< Go back](../README.md)


## CatBoost
- **n_jobs**: -1
- **learning_rate**: 0.1
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

4.6 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.656563 | nan         |
| auc       | 0.65489  | nan         |
| f1        | 0.6759   |   0.386924  |
| accuracy  | 0.618182 |   0.578632  |
| precision | 1        |   0.791663  |
| recall    | 1        |   0.0894123 |
| mcc       | 0.264896 |   0.578632  |


## Confusion matrix (at threshold=0.578632)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                     124 |                      17 |
| Labeled as positive |                      88 |                      46 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
