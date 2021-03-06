# Summary of 35_CatBoost

[<< Go back](../README.md)


## CatBoost
- **n_jobs**: -1
- **learning_rate**: 0.1
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

1.4 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.638586 | nan         |
| auc       | 0.665979 | nan         |
| f1        | 0.65974  |   0.344196  |
| accuracy  | 0.629393 |   0.558154  |
| precision | 0.875    |   0.673062  |
| recall    | 1        |   0.0738025 |
| mcc       | 0.271364 |   0.344196  |


## Confusion matrix (at threshold=0.558154)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                     152 |                      21 |
| Labeled as positive |                      95 |                      45 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
