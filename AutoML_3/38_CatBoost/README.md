# Summary of 38_CatBoost

[<< Go back](../README.md)


## CatBoost
- **n_jobs**: -1
- **learning_rate**: 0.025
- **depth**: 7
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

5.4 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.669646 |  nan        |
| auc       | 0.634911 |  nan        |
| f1        | 0.655257 |    0.209184 |
| accuracy  | 0.621818 |    0.538819 |
| precision | 0.833333 |    0.684817 |
| recall    | 1        |    0.209184 |
| mcc       | 0.261514 |    0.538819 |


## Confusion matrix (at threshold=0.538819)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                     119 |                      22 |
| Labeled as positive |                      82 |                      52 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
