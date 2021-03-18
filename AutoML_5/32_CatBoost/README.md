# Summary of 32_CatBoost

[<< Go back](../README.md)


## CatBoost
- **n_jobs**: -1
- **learning_rate**: 0.1
- **depth**: 7
- **rsm**: 1.0
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

16.0 seconds

## Metric details
|           |    score |    threshold |
|:----------|---------:|-------------:|
| logloss   | 0.276639 | nan          |
| auc       | 0.951902 | nan          |
| f1        | 0.906149 |   0.400704   |
| accuracy  | 0.894545 |   0.400704   |
| precision | 1        |   0.983151   |
| recall    | 1        |   0.00118135 |
| mcc       | 0.788763 |   0.400704   |


## Confusion matrix (at threshold=0.400704)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                     106 |                      20 |
| Labeled as positive |                       9 |                     140 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
