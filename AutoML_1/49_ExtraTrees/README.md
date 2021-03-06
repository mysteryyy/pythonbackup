# Summary of 49_ExtraTrees

[<< Go back](../README.md)


## Extra Trees Classifier (Extra Trees)
- **n_jobs**: -1
- **criterion**: gini
- **max_features**: 0.7
- **min_samples_split**: 30
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

4.1 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.665859 | nan         |
| auc       | 0.62405  | nan         |
| f1        | 0.635171 |   0.349437  |
| accuracy  | 0.619808 |   0.57394   |
| precision | 0.690909 |   0.57394   |
| recall    | 1        |   0.0818182 |
| mcc       | 0.22623  |   0.57394   |


## Confusion matrix (at threshold=0.57394)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                     156 |                      17 |
| Labeled as positive |                     102 |                      38 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
