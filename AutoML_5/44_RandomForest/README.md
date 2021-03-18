# Summary of 44_RandomForest

[<< Go back](../README.md)


## Random Forest
- **n_jobs**: -1
- **criterion**: gini
- **max_features**: 1.0
- **min_samples_split**: 40
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

5.9 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.441874 |  nan        |
| auc       | 0.879408 |  nan        |
| f1        | 0.827815 |    0.466397 |
| accuracy  | 0.810909 |    0.466397 |
| precision | 1        |    0.981335 |
| recall    | 1        |    0        |
| mcc       | 0.618485 |    0.466397 |


## Confusion matrix (at threshold=0.466397)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                      98 |                      28 |
| Labeled as positive |                      24 |                     125 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
