# Summary of 90_ExtraTrees

[<< Go back](../README.md)


## Extra Trees Classifier (Extra Trees)
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

3.4 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.664382 |  nan        |
| auc       | 0.626919 |  nan        |
| f1        | 0.675462 |    0.364962 |
| accuracy  | 0.614545 |    0.534912 |
| precision | 0.769231 |    0.636201 |
| recall    | 1        |    0.141295 |
| mcc       | 0.238013 |    0.534912 |


## Confusion matrix (at threshold=0.534912)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                     113 |                      28 |
| Labeled as positive |                      78 |                      56 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
