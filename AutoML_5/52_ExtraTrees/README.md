# Summary of 52_ExtraTrees

[<< Go back](../README.md)


## Extra Trees Classifier (Extra Trees)
- **n_jobs**: -1
- **criterion**: gini
- **max_features**: 0.7
- **min_samples_split**: 50
- **max_depth**: 3
- **explain_level**: 0

## Validation
 - **validation_type**: kfold
 - **shuffle**: True
 - **stratify**: True
 - **k_folds**: 10

## Optimized metric
logloss

## Training time

5.2 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.567995 |  nan        |
| auc       | 0.811415 |  nan        |
| f1        | 0.757475 |    0.516571 |
| accuracy  | 0.738182 |    0.549775 |
| precision | 1        |    0.852185 |
| recall    | 1        |    0.171429 |
| mcc       | 0.494581 |    0.556266 |


## Confusion matrix (at threshold=0.549775)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                     105 |                      21 |
| Labeled as positive |                      51 |                      98 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
