# Summary of 33_CatBoost

[<< Go back](../README.md)


## CatBoost
- **n_jobs**: -1
- **learning_rate**: 0.2
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

4.1 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.66803  |  nan        |
| auc       | 0.625939 |  nan        |
| f1        | 0.664921 |    0.317484 |
| accuracy  | 0.610909 |    0.531488 |
| precision | 0.75     |    0.733179 |
| recall    | 1        |    0.206897 |
| mcc       | 0.220738 |    0.511173 |


## Confusion matrix (at threshold=0.531488)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                      96 |                      45 |
| Labeled as positive |                      62 |                      72 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
