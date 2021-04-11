# Summary of 66_NearestNeighbors

[<< Go back](../README.md)


## k-Nearest Neighbors (Nearest Neighbors)
- **n_jobs**: -1
- **n_neighbors**: 7
- **weights**: uniform
- **explain_level**: 0

## Validation
 - **validation_type**: kfold
 - **shuffle**: True
 - **stratify**: True
 - **k_folds**: 10

## Optimized metric
logloss

## Training time

1.0 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.640914 |  nan        |
| auc       | 0.734967 |  nan        |
| f1        | 0.71205  |    0.142857 |
| accuracy  | 0.671367 |    0.428571 |
| precision | 0.9      |    0.928571 |
| recall    | 0.997881 |    0        |
| mcc       | 0.34273  |    0.428571 |


## Confusion matrix (at threshold=0.428571)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                     303 |                     147 |
| Labeled as positive |                     156 |                     316 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
