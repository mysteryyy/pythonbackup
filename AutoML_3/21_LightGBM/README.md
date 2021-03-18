# Summary of 21_LightGBM

[<< Go back](../README.md)


## LightGBM
- **n_jobs**: -1
- **objective**: binary
- **metric**: binary_logloss
- **num_leaves**: 15
- **learning_rate**: 0.1
- **feature_fraction**: 0.8
- **bagging_fraction**: 0.8
- **min_data_in_leaf**: 10
- **explain_level**: 0

## Validation
 - **validation_type**: kfold
 - **shuffle**: True
 - **stratify**: True
 - **k_folds**: 5

## Optimized metric
logloss

## Training time

0.8 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.67204  |  nan        |
| auc       | 0.614692 |  nan        |
| f1        | 0.666667 |    0.418063 |
| accuracy  | 0.596364 |    0.418063 |
| precision | 0.689655 |    0.615263 |
| recall    | 1        |    0.241695 |
| mcc       | 0.228286 |    0.418063 |


## Confusion matrix (at threshold=0.418063)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                      53 |                      88 |
| Labeled as positive |                      23 |                     111 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
