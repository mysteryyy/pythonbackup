# Summary of 98_DecisionTree

[<< Go back](../README.md)


## Decision Tree
- **n_jobs**: -1
- **criterion**: entropy
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

0.7 seconds

## Metric details
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 1.19886   |  nan        |
| auc       | 0.548587  |  nan        |
| f1        | 0.653061  |    0        |
| accuracy  | 0.549091  |    0.576067 |
| precision | 0.554348  |    0.576067 |
| recall    | 0.955224  |    0        |
| mcc       | 0.0962468 |    0.429744 |


## Confusion matrix (at threshold=0.576067)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                     100 |                      41 |
| Labeled as positive |                      83 |                      51 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
