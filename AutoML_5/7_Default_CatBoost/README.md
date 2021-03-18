# Summary of 7_Default_CatBoost

[<< Go back](../README.md)


## CatBoost
- **n_jobs**: -1
- **learning_rate**: 0.1
- **depth**: 6
- **rsm**: 1
- **loss_function**: Logloss
- **explain_level**: 0

## Validation
 - **validation_type**: kfold
 - **shuffle**: True
 - **stratify**: True
 - **k_folds**: 10

## Optimized metric
logloss

## Training time

8.4 seconds

## Metric details
|           |    score |    threshold |
|:----------|---------:|-------------:|
| logloss   | 0.27747  | nan          |
| auc       | 0.953233 | nan          |
| f1        | 0.89172  |   0.32464    |
| accuracy  | 0.883636 |   0.606067   |
| precision | 1        |   0.956732   |
| recall    | 1        |   0.00224188 |
| mcc       | 0.767227 |   0.606067   |


## Confusion matrix (at threshold=0.606067)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                     113 |                      13 |
| Labeled as positive |                      19 |                     130 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
