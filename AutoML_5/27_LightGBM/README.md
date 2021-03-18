# Summary of 27_LightGBM

[<< Go back](../README.md)


## LightGBM
- **n_jobs**: -1
- **objective**: binary
- **metric**: binary_logloss
- **num_leaves**: 63
- **learning_rate**: 0.05
- **feature_fraction**: 0.9
- **bagging_fraction**: 0.8
- **min_data_in_leaf**: 30
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
|           |    score |    threshold |
|:----------|---------:|-------------:|
| logloss   | 0.336935 | nan          |
| auc       | 0.929637 | nan          |
| f1        | 0.885246 |   0.473998   |
| accuracy  | 0.872727 |   0.473998   |
| precision | 1        |   0.989625   |
| recall    | 1        |   0.00393103 |
| mcc       | 0.743544 |   0.473998   |


## Confusion matrix (at threshold=0.473998)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                     105 |                      21 |
| Labeled as positive |                      14 |                     135 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
