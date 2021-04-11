# Summary of 69_CatBoost

[<< Go back](../README.md)


## CatBoost
- **n_jobs**: -1
- **learning_rate**: 0.025
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

95.1 seconds

## Metric details
|           |    score |    threshold |
|:----------|---------:|-------------:|
| logloss   | 0.382157 | nan          |
| auc       | 0.909388 | nan          |
| f1        | 0.834297 |   0.344574   |
| accuracy  | 0.828633 |   0.515031   |
| precision | 1        |   0.984676   |
| recall    | 1        |   0.00315998 |
| mcc       | 0.657167 |   0.515031   |


## Confusion matrix (at threshold=0.515031)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                     373 |                      77 |
| Labeled as positive |                      81 |                     391 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
