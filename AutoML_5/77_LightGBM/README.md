# Summary of 77_LightGBM

[<< Go back](../README.md)


## LightGBM
- **n_jobs**: -1
- **objective**: binary
- **metric**: binary_logloss
- **num_leaves**: 15
- **learning_rate**: 0.2
- **feature_fraction**: 0.8
- **bagging_fraction**: 0.8
- **min_data_in_leaf**: 10
- **explain_level**: 0

## Validation
 - **validation_type**: kfold
 - **shuffle**: True
 - **stratify**: True
 - **k_folds**: 10

## Optimized metric
logloss

## Training time

1.2 seconds

## Metric details
|           |    score |     threshold |
|:----------|---------:|--------------:|
| logloss   | 0.293316 | nan           |
| auc       | 0.946522 | nan           |
| f1        | 0.88961  |   0.41931     |
| accuracy  | 0.876364 |   0.41931     |
| precision | 1        |   0.977788    |
| recall    | 1        |   3.29126e-05 |
| mcc       | 0.751494 |   0.41931     |


## Confusion matrix (at threshold=0.41931)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                     104 |                      22 |
| Labeled as positive |                      12 |                     137 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
