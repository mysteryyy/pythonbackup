# Summary of 68_NearestNeighbors

[<< Go back](../README.md)


## k-Nearest Neighbors (Nearest Neighbors)
- **n_jobs**: -1
- **n_neighbors**: 7
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

0.8 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.813838 |  nan        |
| auc       | 0.506627 |  nan        |
| f1        | 0.616408 |    0        |
| accuracy  | 0.578275 |    0.783771 |
| precision | 0.9      |    0.783771 |
| recall    | 0.992857 |    0        |
| mcc       | 0.16541  |    0.783771 |


## Confusion matrix (at threshold=0.783771)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                     172 |                       1 |
| Labeled as positive |                     131 |                       9 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
