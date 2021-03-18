# Summary of 40_RandomForest

[<< Go back](../README.md)


## Random Forest
- **n_jobs**: -1
- **criterion**: gini
- **max_features**: 0.7
- **min_samples_split**: 30
- **max_depth**: 7
- **explain_level**: 0

## Validation
 - **validation_type**: kfold
 - **shuffle**: True
 - **stratify**: True
 - **k_folds**: 10

## Optimized metric
logloss

## Training time

6.8 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.43197  | nan         |
| auc       | 0.902738 | nan         |
| f1        | 0.833333 |   0.475734  |
| accuracy  | 0.821818 |   0.521671  |
| precision | 1        |   0.991279  |
| recall    | 1        |   0.0209302 |
| mcc       | 0.64448  |   0.521671  |


## Confusion matrix (at threshold=0.521671)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                     106 |                      20 |
| Labeled as positive |                      29 |                     120 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
