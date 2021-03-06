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
 - **k_folds**: 5

## Optimized metric
logloss

## Training time

0.7 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 1.53978  |  nan        |
| auc       | 0.565937 |  nan        |
| f1        | 0.645503 |    0.122159 |
| accuracy  | 0.571885 |    0.219101 |
| precision | 0.512931 |    0.219101 |
| recall    | 0.935714 |    0        |
| mcc       | 0.234027 |    0.122159 |


## Confusion matrix (at threshold=0.219101)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                      60 |                     113 |
| Labeled as positive |                      21 |                     119 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
