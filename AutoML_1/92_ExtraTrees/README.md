# Summary of 92_ExtraTrees

[<< Go back](../README.md)


## Extra Trees Classifier (Extra Trees)
- **n_jobs**: -1
- **criterion**: gini
- **max_features**: 0.6
- **min_samples_split**: 50
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
| logloss   | 0.665085 |  nan        |
| auc       | 0.627849 |  nan        |
| f1        | 0.635071 |    0.352512 |
| accuracy  | 0.610224 |    0.469217 |
| precision | 0.666667 |    0.538117 |
| recall    | 1        |    0.1      |
| mcc       | 0.207645 |    0.469217 |


## Confusion matrix (at threshold=0.469217)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                     116 |                      57 |
| Labeled as positive |                      65 |                      75 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
