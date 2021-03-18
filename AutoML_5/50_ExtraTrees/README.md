# Summary of 50_ExtraTrees

[<< Go back](../README.md)


## Extra Trees Classifier (Extra Trees)
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
 - **k_folds**: 10

## Optimized metric
logloss

## Training time

4.7 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.533758 |  nan        |
| auc       | 0.857036 |  nan        |
| f1        | 0.813456 |    0.479477 |
| accuracy  | 0.778182 |    0.479477 |
| precision | 1        |    0.756753 |
| recall    | 1        |    0        |
| mcc       | 0.569904 |    0.547163 |


## Confusion matrix (at threshold=0.479477)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                      81 |                      45 |
| Labeled as positive |                      16 |                     133 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
