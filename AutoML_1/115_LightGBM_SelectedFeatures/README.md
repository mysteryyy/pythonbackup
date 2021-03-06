# Summary of 115_LightGBM_SelectedFeatures

[<< Go back](../README.md)


## LightGBM
- **n_jobs**: -1
- **objective**: binary
- **metric**: binary_logloss
- **num_leaves**: 31
- **learning_rate**: 0.05
- **feature_fraction**: 0.9
- **bagging_fraction**: 0.8
- **min_data_in_leaf**: 30
- **explain_level**: 0

## Validation
 - **validation_type**: kfold
 - **shuffle**: True
 - **stratify**: True
 - **k_folds**: 5

## Optimized metric
logloss

## Training time

1.1 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.631101 |  nan        |
| auc       | 0.692465 |  nan        |
| f1        | 0.659847 |    0.291596 |
| accuracy  | 0.661342 |    0.451111 |
| precision | 0.666667 |    0.628415 |
| recall    | 1        |    0.114333 |
| mcc       | 0.32284  |    0.451111 |


## Confusion matrix (at threshold=0.451111)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                     113 |                      60 |
| Labeled as positive |                      46 |                      94 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
