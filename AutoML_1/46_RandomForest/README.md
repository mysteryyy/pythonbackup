# Summary of 46_RandomForest

[<< Go back](../README.md)


## Random Forest
- **n_jobs**: -1
- **criterion**: gini
- **max_features**: 0.6
- **min_samples_split**: 20
- **max_depth**: 4
- **explain_level**: 0

## Validation
 - **validation_type**: kfold
 - **shuffle**: True
 - **stratify**: True
 - **k_folds**: 5

## Optimized metric
logloss

## Training time

6.2 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.655615 | nan         |
| auc       | 0.641701 | nan         |
| f1        | 0.654639 |   0.293896  |
| accuracy  | 0.610224 |   0.449007  |
| precision | 1        |   0.751963  |
| recall    | 1        |   0.0466093 |
| mcc       | 0.257112 |   0.331306  |


## Confusion matrix (at threshold=0.449007)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                      99 |                      74 |
| Labeled as positive |                      48 |                      92 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
