# Summary of 69_NearestNeighbors

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

0.7 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.508355 |  nan        |
| auc       | 0.814185 |  nan        |
| f1        | 0.774373 |    0.285714 |
| accuracy  | 0.730909 |    0.5      |
| precision | 0.916667 |    0.785714 |
| recall    | 1        |    0        |
| mcc       | 0.458368 |    0.642857 |


## Confusion matrix (at threshold=0.5)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                      86 |                      40 |
| Labeled as positive |                      34 |                     115 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
