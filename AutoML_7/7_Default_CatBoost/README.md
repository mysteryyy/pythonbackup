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

13.3 seconds

## Metric details
|           |    score |    threshold |
|:----------|---------:|-------------:|
| logloss   | 0.41995  | nan          |
| auc       | 0.888663 | nan          |
| f1        | 0.81903  |   0.284809   |
| accuracy  | 0.804772 |   0.498523   |
| precision | 1        |   0.990035   |
| recall    | 1        |   0.00153666 |
| mcc       | 0.609627 |   0.406544   |


## Confusion matrix (at threshold=0.498523)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                     360 |                      90 |
| Labeled as positive |                      90 |                     382 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
