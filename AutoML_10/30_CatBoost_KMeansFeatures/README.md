# Summary of 30_CatBoost_KMeansFeatures

[<< Go back](../README.md)


## CatBoost
- **n_jobs**: -1
- **learning_rate**: 0.05
- **depth**: 8
- **rsm**: 0.8
- **loss_function**: Logloss
- **explain_level**: 0

## Validation
 - **validation_type**: kfold
 - **shuffle**: True
 - **stratify**: True
 - **k_folds**: 10

## Optimized metric
logloss

## Training time

96.0 seconds

## Metric details
|           |    score |    threshold |
|:----------|---------:|-------------:|
| logloss   | 0.440038 | nan          |
| auc       | 0.876271 | nan          |
| f1        | 0.809331 |   0.46339    |
| accuracy  | 0.796095 |   0.46339    |
| precision | 1        |   0.989483   |
| recall    | 1        |   0.00234611 |
| mcc       | 0.593551 |   0.46339    |


## Confusion matrix (at threshold=0.46339)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                     335 |                     115 |
| Labeled as positive |                      73 |                     399 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
