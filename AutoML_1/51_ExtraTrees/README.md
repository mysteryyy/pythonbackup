# Summary of 51_ExtraTrees

[<< Go back](../README.md)


## Extra Trees Classifier (Extra Trees)
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

3.6 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.676592 |  nan        |
| auc       | 0.576012 |  nan        |
| f1        | 0.625917 |    0.33927  |
| accuracy  | 0.591054 |    0.508323 |
| precision | 0.846154 |    0.585573 |
| recall    | 1        |    0.209095 |
| mcc       | 0.166993 |    0.585573 |


## Confusion matrix (at threshold=0.508323)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                     143 |                      30 |
| Labeled as positive |                      98 |                      42 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
