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

0.6 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 1.8371   |  nan        |
| auc       | 0.556791 |  nan        |
| f1        | 0.654639 |    0        |
| accuracy  | 0.56     |    0.279383 |
| precision | 0.546296 |    0.645455 |
| recall    | 0.947761 |    0        |
| mcc       | 0.144681 |    0.258929 |


## Confusion matrix (at threshold=0.279383)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                      55 |                      86 |
| Labeled as positive |                      35 |                      99 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
