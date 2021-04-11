# Summary of 10_Default_ExtraTrees

[<< Go back](../README.md)


## Extra Trees Classifier (Extra Trees)
- **n_jobs**: -1
- **criterion**: gini
- **max_features**: 0.9
- **min_samples_split**: 30
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

7.9 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.635354 |  nan        |
| auc       | 0.752615 |  nan        |
| f1        | 0.728638 |    0.491202 |
| accuracy  | 0.699566 |    0.513177 |
| precision | 1        |    0.701986 |
| recall    | 1        |    0.202537 |
| mcc       | 0.398658 |    0.513177 |


## Confusion matrix (at threshold=0.513177)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                     309 |                     141 |
| Labeled as positive |                     136 |                     336 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
