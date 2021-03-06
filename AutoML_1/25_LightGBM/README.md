# Summary of 25_LightGBM

[<< Go back](../README.md)


## LightGBM
- **n_jobs**: -1
- **objective**: binary
- **metric**: binary_logloss
- **num_leaves**: 63
- **learning_rate**: 0.2
- **feature_fraction**: 0.5
- **bagging_fraction**: 1.0
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

0.9 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.650086 |  nan        |
| auc       | 0.655202 |  nan        |
| f1        | 0.65928  |    0.378581 |
| accuracy  | 0.619808 |    0.454783 |
| precision | 0.666667 |    0.609711 |
| recall    | 1        |    0.149312 |
| mcc       | 0.284214 |    0.378581 |


## Confusion matrix (at threshold=0.454783)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                     107 |                      66 |
| Labeled as positive |                      53 |                      87 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
