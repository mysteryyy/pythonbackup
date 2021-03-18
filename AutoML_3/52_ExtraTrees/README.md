# Summary of 52_ExtraTrees

[<< Go back](../README.md)


## Extra Trees Classifier (Extra Trees)
- **n_jobs**: -1
- **criterion**: gini
- **max_features**: 0.7
- **min_samples_split**: 50
- **max_depth**: 3
- **explain_level**: 0

## Validation
 - **validation_type**: kfold
 - **shuffle**: True
 - **stratify**: True
 - **k_folds**: 5

## Optimized metric
logloss

## Training time

2.9 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.668151 |  nan        |
| auc       | 0.614296 |  nan        |
| f1        | 0.686486 |    0.340996 |
| accuracy  | 0.607273 |    0.522625 |
| precision | 0.625    |    0.584717 |
| recall    | 1        |    0        |
| mcc       | 0.25032  |    0.340996 |


## Confusion matrix (at threshold=0.522625)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                      85 |                      56 |
| Labeled as positive |                      52 |                      82 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
