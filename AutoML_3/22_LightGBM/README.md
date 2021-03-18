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
 - **k_folds**: 5

## Optimized metric
logloss

## Training time

0.7 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.663059 |  nan        |
| auc       | 0.640865 |  nan        |
| f1        | 0.664935 |    0.31817  |
| accuracy  | 0.636364 |    0.481913 |
| precision | 0.769231 |    0.707345 |
| recall    | 1        |    0.118047 |
| mcc       | 0.272554 |    0.481913 |


## Confusion matrix (at threshold=0.481913)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                      90 |                      51 |
| Labeled as positive |                      49 |                      85 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
