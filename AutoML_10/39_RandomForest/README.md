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
 - **k_folds**: 10

## Optimized metric
logloss

## Training time

8.7 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.613441 | nan         |
| auc       | 0.750737 | nan         |
| f1        | 0.719665 |   0.421423  |
| accuracy  | 0.690889 |   0.519365  |
| precision | 0.95     |   0.756039  |
| recall    | 1        |   0.0516314 |
| mcc       | 0.384695 |   0.519365  |


## Confusion matrix (at threshold=0.519365)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                     330 |                     120 |
| Labeled as positive |                     165 |                     307 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
