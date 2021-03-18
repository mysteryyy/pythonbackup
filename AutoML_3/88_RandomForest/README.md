# Summary of 88_RandomForest

[<< Go back](../README.md)


## Random Forest
- **n_jobs**: -1
- **criterion**: gini
- **max_features**: 0.7
- **min_samples_split**: 40
- **max_depth**: 3
- **explain_level**: 0

## Validation
 - **validation_type**: kfold
 - **shuffle**: True
 - **stratify**: True
 - **k_folds**: 5

## Optimized metric
logloss

## Training time

3.0 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.657544 | nan         |
| auc       | 0.651503 | nan         |
| f1        | 0.675325 |   0.315085  |
| accuracy  | 0.614545 |   0.610966  |
| precision | 0.78125  |   0.670551  |
| recall    | 1        |   0.0710526 |
| mcc       | 0.268979 |   0.625324  |


## Confusion matrix (at threshold=0.610966)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                     125 |                      16 |
| Labeled as positive |                      90 |                      44 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
