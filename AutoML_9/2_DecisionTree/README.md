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

0.9 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.895981 |  nan        |
| auc       | 0.629    |  nan        |
| f1        | 0.676492 |    0.135135 |
| accuracy  | 0.597614 |    0.553581 |
| precision | 0.829787 |    0.945195 |
| recall    | 0.980932 |    0        |
| mcc       | 0.209893 |    0.593641 |


## Confusion matrix (at threshold=0.553581)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                     313 |                     137 |
| Labeled as positive |                     234 |                     238 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
