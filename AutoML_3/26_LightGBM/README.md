# Summary of 26_LightGBM

[<< Go back](../README.md)


## LightGBM
- **n_jobs**: -1
- **objective**: binary
- **metric**: binary_logloss
- **num_leaves**: 127
- **learning_rate**: 0.05
- **feature_fraction**: 0.5
- **bagging_fraction**: 0.5
- **min_data_in_leaf**: 20
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
| logloss   | 0.669006 |  nan        |
| auc       | 0.634143 |  nan        |
| f1        | 0.678261 |    0.42941  |
| accuracy  | 0.618182 |    0.48508  |
| precision | 0.75     |    0.722375 |
| recall    | 1        |    0.174293 |
| mcc       | 0.245366 |    0.438422 |


## Confusion matrix (at threshold=0.48508)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                      89 |                      52 |
| Labeled as positive |                      53 |                      81 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
