# Summary of 85_RandomForest

[<< Go back](../README.md)


## Random Forest
- **n_jobs**: -1
- **criterion**: entropy
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

7.6 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.442058 | nan         |
| auc       | 0.902871 | nan         |
| f1        | 0.84058  |   0.560227  |
| accuracy  | 0.84     |   0.560227  |
| precision | 1        |   0.869827  |
| recall    | 1        |   0.0208333 |
| mcc       | 0.690817 |   0.560227  |


## Confusion matrix (at threshold=0.560227)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                     115 |                      11 |
| Labeled as positive |                      33 |                     116 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
