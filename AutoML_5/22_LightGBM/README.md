# Summary of 22_LightGBM

[<< Go back](../README.md)


## LightGBM
- **n_jobs**: -1
- **objective**: binary
- **metric**: binary_logloss
- **num_leaves**: 63
- **learning_rate**: 0.2
- **feature_fraction**: 0.5
- **bagging_fraction**: 1.0
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

1.1 seconds

## Metric details
|           |    score |     threshold |
|:----------|---------:|--------------:|
| logloss   | 0.29011  | nan           |
| auc       | 0.948493 | nan           |
| f1        | 0.890323 |   0.393111    |
| accuracy  | 0.876364 |   0.471207    |
| precision | 1        |   0.965979    |
| recall    | 1        |   9.70196e-05 |
| mcc       | 0.752095 |   0.393111    |


## Confusion matrix (at threshold=0.471207)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                     105 |                      21 |
| Labeled as positive |                      13 |                     136 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
