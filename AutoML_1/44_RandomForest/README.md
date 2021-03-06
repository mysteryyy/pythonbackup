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
 - **k_folds**: 5

## Optimized metric
logloss

## Training time

4.6 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.645247 | nan         |
| auc       | 0.662552 | nan         |
| f1        | 0.664756 |   0.378392  |
| accuracy  | 0.626198 |   0.378392  |
| precision | 1        |   0.742807  |
| recall    | 1        |   0.0833834 |
| mcc       | 0.307177 |   0.378392  |


## Confusion matrix (at threshold=0.378392)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                      80 |                      93 |
| Labeled as positive |                      24 |                     116 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
