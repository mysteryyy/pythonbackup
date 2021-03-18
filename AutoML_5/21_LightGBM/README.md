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
 - **k_folds**: 10

## Optimized metric
logloss

## Training time

1.5 seconds

## Metric details
|           |    score |     threshold |
|:----------|---------:|--------------:|
| logloss   | 0.296782 | nan           |
| auc       | 0.94535  | nan           |
| f1        | 0.886076 |   0.290013    |
| accuracy  | 0.872727 |   0.610356    |
| precision | 1        |   0.969397    |
| recall    | 1        |   0.000253229 |
| mcc       | 0.746673 |   0.638044    |


## Confusion matrix (at threshold=0.610356)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                     112 |                      14 |
| Labeled as positive |                      21 |                     128 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
