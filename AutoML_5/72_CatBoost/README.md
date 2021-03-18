# Summary of 72_CatBoost

[<< Go back](../README.md)


## CatBoost
- **n_jobs**: -1
- **learning_rate**: 0.05
- **depth**: 8
- **rsm**: 1.0
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

40.3 seconds

## Metric details
|           |    score |    threshold |
|:----------|---------:|-------------:|
| logloss   | 0.268122 | nan          |
| auc       | 0.957654 | nan          |
| f1        | 0.899654 |   0.623816   |
| accuracy  | 0.894545 |   0.653537   |
| precision | 1        |   0.938737   |
| recall    | 1        |   0.00321731 |
| mcc       | 0.792828 |   0.653537   |


## Confusion matrix (at threshold=0.653537)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                     118 |                       8 |
| Labeled as positive |                      21 |                     128 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
