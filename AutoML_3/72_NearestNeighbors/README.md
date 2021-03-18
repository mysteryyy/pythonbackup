# Summary of 72_NearestNeighbors

[<< Go back](../README.md)


## k-Nearest Neighbors (Nearest Neighbors)
- **n_jobs**: -1
- **n_neighbors**: 3
- **weights**: distance
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
| logloss   | 2.24136   |  nan        |
| auc       | 0.542871  |  nan        |
| f1        | 0.644628  |    0        |
| accuracy  | 0.530909  |    0        |
| precision | 0.515625  |    0.510533 |
| recall    | 0.873134  |    0        |
| mcc       | 0.0529304 |    0.510533 |


## Confusion matrix (at threshold=0.0)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                      29 |                     112 |
| Labeled as positive |                      17 |                     117 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
