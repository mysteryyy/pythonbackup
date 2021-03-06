# Summary of 8_Default_NeuralNetwork

[<< Go back](../README.md)


## Neural Network
- **n_jobs**: -1
- **dense_1_size**: 32
- **dense_2_size**: 16
- **learning_rate**: 0.05
- **explain_level**: 0

## Validation
 - **validation_type**: kfold
 - **shuffle**: True
 - **stratify**: True
 - **k_folds**: 5

## Optimized metric
logloss

## Training time

1.0 seconds

## Metric details
|           |    score |     threshold |
|:----------|---------:|--------------:|
| logloss   | 0.814585 | nan           |
| auc       | 0.579975 | nan           |
| f1        | 0.624709 |   0.0855268   |
| accuracy  | 0.584665 |   0.647446    |
| precision | 0.625    |   0.955571    |
| recall    | 1        |   0.000367964 |
| mcc       | 0.159944 |   0.40366     |


## Confusion matrix (at threshold=0.647446)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                     145 |                      28 |
| Labeled as positive |                     102 |                      38 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
