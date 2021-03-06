# Summary of 42_RandomForest

[<< Go back](../README.md)


## Random Forest
- **n_jobs**: -1
- **criterion**: entropy
- **max_features**: 0.6
- **min_samples_split**: 50
- **max_depth**: 6
- **explain_level**: 0

## Validation
 - **validation_type**: kfold
 - **shuffle**: True
 - **stratify**: True
 - **k_folds**: 5

## Optimized metric
logloss

## Training time

5.9 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.632654 | nan         |
| auc       | 0.681007 | nan         |
| f1        | 0.671795 |   0.252666  |
| accuracy  | 0.635783 |   0.443316  |
| precision | 0.6875   |   0.663784  |
| recall    | 1        |   0.0663616 |
| mcc       | 0.307356 |   0.252666  |


## Confusion matrix (at threshold=0.443316)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                      98 |                      75 |
| Labeled as positive |                      39 |                     101 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
