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
 - **k_folds**: 5

## Optimized metric
logloss

## Training time

3.6 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.644122 | nan         |
| auc       | 0.662841 | nan         |
| f1        | 0.650246 |   0.237352  |
| accuracy  | 0.632588 |   0.638463  |
| precision | 1        |   0.799884  |
| recall    | 1        |   0.0209513 |
| mcc       | 0.26203  |   0.638463  |


## Confusion matrix (at threshold=0.638463)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                     159 |                      14 |
| Labeled as positive |                     101 |                      39 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
