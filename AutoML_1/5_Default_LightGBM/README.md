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

1.1 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.66263  |  nan        |
| auc       | 0.6205   |  nan        |
| f1        | 0.645161 |    0.339864 |
| accuracy  | 0.607029 |    0.50979  |
| precision | 0.623188 |    0.520088 |
| recall    | 1        |    0.203264 |
| mcc       | 0.216851 |    0.339864 |


## Confusion matrix (at threshold=0.50979)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                     143 |                      30 |
| Labeled as positive |                      93 |                      47 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
