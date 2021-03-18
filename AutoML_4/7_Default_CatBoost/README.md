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
 - **k_folds**: 5

## Optimized metric
logloss

## Training time

4.5 seconds

## Metric details
|           |    score |    threshold |
|:----------|---------:|-------------:|
| logloss   | 0.292358 | nan          |
| auc       | 0.947534 | nan          |
| f1        | 0.884211 |   0.611683   |
| accuracy  | 0.88     |   0.611683   |
| precision | 1        |   0.983316   |
| recall    | 1        |   0.00134406 |
| mcc       | 0.763633 |   0.611683   |


## Confusion matrix (at threshold=0.611683)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                     116 |                      10 |
| Labeled as positive |                      23 |                     126 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
