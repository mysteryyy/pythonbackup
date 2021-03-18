# Summary of 70_NearestNeighbors

[<< Go back](../README.md)


## k-Nearest Neighbors (Nearest Neighbors)
- **n_jobs**: -1
- **n_neighbors**: 3
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

0.3 seconds

## Metric details
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 2.23506   |       nan   |
| auc       | 0.543771  |       nan   |
| f1        | 0.644628  |         0   |
| accuracy  | 0.530909  |         0   |
| precision | 0.51938   |         0.5 |
| recall    | 0.873134  |         0   |
| mcc       | 0.0603796 |         0.5 |


## Confusion matrix (at threshold=0.0)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                      29 |                     112 |
| Labeled as positive |                      17 |                     117 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
