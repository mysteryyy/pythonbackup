# Summary of 76_LightGBM

[<< Go back](../README.md)


## LightGBM
- **n_jobs**: -1
- **objective**: binary
- **metric**: binary_logloss
- **num_leaves**: 15
- **learning_rate**: 0.05
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

1.7 seconds

## Metric details
|           |    score |     threshold |
|:----------|---------:|--------------:|
| logloss   | 0.304111 | nan           |
| auc       | 0.94242  | nan           |
| f1        | 0.896104 |   0.446509    |
| accuracy  | 0.883636 |   0.446509    |
| precision | 1        |   0.94811     |
| recall    | 1        |   3.63341e-05 |
| mcc       | 0.766272 |   0.446509    |


## Confusion matrix (at threshold=0.446509)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                     105 |                      21 |
| Labeled as positive |                      11 |                     138 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
