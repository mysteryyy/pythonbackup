# Summary of 85_ExtraTrees

[<< Go back](../README.md)


## Extra Trees Classifier (Extra Trees)
- **n_jobs**: -1
- **criterion**: gini
- **max_features**: 0.9
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

3.4 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.670074 |  nan        |
| auc       | 0.625172 |  nan        |
| f1        | 0.67374  |    0.320198 |
| accuracy  | 0.610909 |    0.502202 |
| precision | 0.636364 |    0.599182 |
| recall    | 1        |    0.153195 |
| mcc       | 0.220738 |    0.497867 |


## Confusion matrix (at threshold=0.502202)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                      92 |                      49 |
| Labeled as positive |                      58 |                      76 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
