# Summary of 61_NeuralNetwork

[<< Go back](../README.md)


## Neural Network
- **n_jobs**: -1
- **dense_1_size**: 64
- **dense_2_size**: 16
- **learning_rate**: 0.01
- **explain_level**: 0

## Validation
 - **validation_type**: kfold
 - **shuffle**: True
 - **stratify**: True
 - **k_folds**: 5

## Optimized metric
logloss

## Training time

1.6 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.714594 | nan         |
| auc       | 0.55801  | nan         |
| f1        | 0.62963  |   0.202227  |
| accuracy  | 0.587859 |   0.524092  |
| precision | 0.58209  |   0.524092  |
| recall    | 1        |   0.0122926 |
| mcc       | 0.150917 |   0.479215  |


## Confusion matrix (at threshold=0.524092)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                     145 |                      28 |
| Labeled as positive |                     101 |                      39 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
