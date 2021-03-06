# Summary of 104_DecisionTree

[<< Go back](../README.md)


## Decision Tree
- **n_jobs**: -1
- **criterion**: entropy
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

0.3 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 1.94327  |  nan        |
| auc       | 0.545273 |  nan        |
| f1        | 0.639175 |    0.219101 |
| accuracy  | 0.552716 |    0.219101 |
| precision | 0.5      |    0.219101 |
| recall    | 0.892857 |    0        |
| mcc       | 0.207093 |    0.219101 |


## Confusion matrix (at threshold=0.219101)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                      49 |                     124 |
| Labeled as positive |                      16 |                     124 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
