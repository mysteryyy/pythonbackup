# Summary of 48_ExtraTrees

[<< Go back](../README.md)


## Extra Trees Classifier (Extra Trees)
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

5.6 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.517509 |  nan        |
| auc       | 0.860312 |  nan        |
| f1        | 0.818462 |    0.486827 |
| accuracy  | 0.785455 |    0.486827 |
| precision | 1        |    0.853203 |
| recall    | 1        |    0        |
| mcc       | 0.572308 |    0.486827 |


## Confusion matrix (at threshold=0.486827)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                      83 |                      43 |
| Labeled as positive |                      16 |                     133 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
