# Summary of 117_CatBoost_SelectedFeatures

[<< Go back](../README.md)


## CatBoost
- **n_jobs**: -1
- **learning_rate**: 0.1
- **depth**: 6
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

1.7 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.637605 | nan         |
| auc       | 0.680801 | nan         |
| f1        | 0.661538 |   0.333028  |
| accuracy  | 0.664537 |   0.519008  |
| precision | 0.9      |   0.712113  |
| recall    | 1        |   0.0857727 |
| mcc       | 0.317224 |   0.512733  |


## Confusion matrix (at threshold=0.519008)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                     128 |                      45 |
| Labeled as positive |                      60 |                      80 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
