# Summary of 11_Default_NearestNeighbors

[<< Go back](../README.md)


## k-Nearest Neighbors (Nearest Neighbors)
- **n_jobs**: -1
- **n_neighbors**: 5
- **weights**: uniform
- **explain_level**: 0

## Validation
 - **validation_type**: kfold
 - **shuffle**: True
 - **stratify**: True
 - **k_folds**: 5

## Optimized metric
logloss

## Training time

0.7 seconds

## Metric details
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 1.15551   |       nan   |
| auc       | 0.541706  |       nan   |
| f1        | 0.648379  |         0   |
| accuracy  | 0.549091  |         0.5 |
| precision | 0.538462  |         0.5 |
| recall    | 0.970149  |         0   |
| mcc       | 0.0969691 |         0.5 |


## Confusion matrix (at threshold=0.5)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                      81 |                      60 |
| Labeled as positive |                      64 |                      70 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
