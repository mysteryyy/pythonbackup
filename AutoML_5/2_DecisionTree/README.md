# Summary of 2_DecisionTree

[<< Go back](../README.md)


## Decision Tree
- **n_jobs**: -1
- **criterion**: gini
- **max_depth**: 4
- **explain_level**: 0

## Validation
 - **validation_type**: kfold
 - **shuffle**: True
 - **stratify**: True
 - **k_folds**: 10

## Optimized metric
logloss

## Training time

0.5 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 1.37583  |  nan        |
| auc       | 0.790029 |  nan        |
| f1        | 0.776699 |    0.303571 |
| accuracy  | 0.763636 |    0.625    |
| precision | 0.817073 |    0.930247 |
| recall    | 0.912752 |    0        |
| mcc       | 0.528825 |    0.625    |


## Confusion matrix (at threshold=0.625)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                      99 |                      27 |
| Labeled as positive |                      38 |                     111 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
