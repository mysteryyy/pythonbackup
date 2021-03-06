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

3.1 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.658366 |  nan        |
| auc       | 0.635343 |  nan        |
| f1        | 0.651515 |    0.375553 |
| accuracy  | 0.613419 |    0.443127 |
| precision | 0.692308 |    0.592728 |
| recall    | 1        |    0.132065 |
| mcc       | 0.245906 |    0.443127 |


## Confusion matrix (at threshold=0.443127)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                      93 |                      80 |
| Labeled as positive |                      41 |                      99 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
