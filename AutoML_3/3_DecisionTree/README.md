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

0.5 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 1.8371   |  nan        |
| auc       | 0.556843 |  nan        |
| f1        | 0.65641  |    0        |
| accuracy  | 0.56     |    0.279383 |
| precision | 0.545455 |    0.645455 |
| recall    | 0.955224 |    0        |
| mcc       | 0.146548 |    0.258929 |


## Confusion matrix (at threshold=0.279383)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                      54 |                      87 |
| Labeled as positive |                      34 |                     100 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
