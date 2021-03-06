# Summary of 60_NeuralNetwork

[<< Go back](../README.md)


## Neural Network
- **n_jobs**: -1
- **dense_1_size**: 32
- **dense_2_size**: 32
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
| logloss   | 0.838587 | nan           |
| auc       | 0.538728 | nan           |
| f1        | 0.630491 |   0.18108     |
| accuracy  | 0.565495 |   0.696933    |
| precision | 0.6      |   0.696933    |
| recall    | 1        |   2.98235e-05 |
| mcc       | 0.181476 |   0.18108     |


## Confusion matrix (at threshold=0.696933)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                     165 |                       8 |
| Labeled as positive |                     128 |                      12 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
