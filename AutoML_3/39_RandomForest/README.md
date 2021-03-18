# Summary of 39_RandomForest

[<< Go back](../README.md)


## Random Forest
- **n_jobs**: -1
- **criterion**: gini
- **max_features**: 0.5
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

3.3 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.667254 |  nan        |
| auc       | 0.628824 |  nan        |
| f1        | 0.668421 |    0.333752 |
| accuracy  | 0.610909 |    0.533625 |
| precision | 1        |    0.764136 |
| recall    | 1        |    0.131327 |
| mcc       | 0.223136 |    0.533625 |


## Confusion matrix (at threshold=0.533625)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                     104 |                      37 |
| Labeled as positive |                      70 |                      64 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
