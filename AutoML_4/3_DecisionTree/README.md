# Summary of 3_DecisionTree

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

0.2 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 1.26808  |  nan        |
| auc       | 0.816129 |  nan        |
| f1        | 0.798742 |    0.244624 |
| accuracy  | 0.770909 |    0.416667 |
| precision | 0.863248 |    0.84     |
| recall    | 0.932886 |    0        |
| mcc       | 0.555143 |    0.84     |


## Confusion matrix (at threshold=0.416667)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                      89 |                      37 |
| Labeled as positive |                      26 |                     123 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
