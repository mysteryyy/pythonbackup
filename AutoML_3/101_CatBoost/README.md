# Summary of 101_CatBoost

[<< Go back](../README.md)


## CatBoost
- **n_jobs**: -1
- **learning_rate**: 0.05
- **depth**: 4
- **rsm**: 0.7
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

3.5 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.650263 |  nan        |
| auc       | 0.659469 |  nan        |
| f1        | 0.670241 |    0.337164 |
| accuracy  | 0.625455 |    0.500464 |
| precision | 1        |    0.704644 |
| recall    | 1        |    0.15175  |
| mcc       | 0.249988 |    0.500464 |


## Confusion matrix (at threshold=0.500464)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                      98 |                      43 |
| Labeled as positive |                      60 |                      74 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
