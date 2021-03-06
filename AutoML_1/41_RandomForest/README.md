# Summary of 41_RandomForest

[<< Go back](../README.md)


## Random Forest
- **n_jobs**: -1
- **criterion**: gini
- **max_features**: 0.8
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

3.6 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.645565 | nan         |
| auc       | 0.65353  | nan         |
| f1        | 0.664921 |   0.248783  |
| accuracy  | 0.642173 |   0.459351  |
| precision | 0.6      |   0.679354  |
| recall    | 1        |   0.0988893 |
| mcc       | 0.291354 |   0.459351  |


## Confusion matrix (at threshold=0.459351)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                     105 |                      68 |
| Labeled as positive |                      44 |                      96 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
