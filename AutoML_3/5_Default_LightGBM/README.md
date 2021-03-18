# Summary of 5_Default_LightGBM

[<< Go back](../README.md)


## LightGBM
- **n_jobs**: -1
- **objective**: binary
- **metric**: binary_logloss
- **num_leaves**: 63
- **learning_rate**: 0.05
- **feature_fraction**: 0.9
- **bagging_fraction**: 0.9
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

1.0 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.674363 |  nan        |
| auc       | 0.612549 |  nan        |
| f1        | 0.664865 |    0.36192  |
| accuracy  | 0.596364 |    0.534324 |
| precision | 0.714286 |    0.690972 |
| recall    | 1        |    0.114781 |
| mcc       | 0.204773 |    0.534324 |


## Confusion matrix (at threshold=0.534324)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                     116 |                      25 |
| Labeled as positive |                      86 |                      48 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
