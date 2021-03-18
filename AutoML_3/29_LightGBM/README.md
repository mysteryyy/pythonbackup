# Summary of 29_LightGBM

[<< Go back](../README.md)


## LightGBM
- **n_jobs**: -1
- **objective**: binary
- **metric**: binary_logloss
- **num_leaves**: 15
- **learning_rate**: 0.05
- **feature_fraction**: 1.0
- **bagging_fraction**: 0.5
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

0.8 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.66389  |  nan        |
| auc       | 0.641341 |  nan        |
| f1        | 0.663014 |    0.35143  |
| accuracy  | 0.610909 |    0.500478 |
| precision | 0.785714 |    0.722096 |
| recall    | 1        |    0.140459 |
| mcc       | 0.230613 |    0.447157 |


## Confusion matrix (at threshold=0.500478)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                      98 |                      43 |
| Labeled as positive |                      64 |                      70 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
