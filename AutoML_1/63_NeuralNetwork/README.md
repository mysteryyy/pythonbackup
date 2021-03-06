# Summary of 63_NeuralNetwork

[<< Go back](../README.md)


## Neural Network
- **n_jobs**: -1
- **dense_1_size**: 16
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

1.1 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.687424 | nan         |
| auc       | 0.570603 | nan         |
| f1        | 0.626168 |   0.304079  |
| accuracy  | 0.591054 |   0.521924  |
| precision | 0.666667 |   0.664287  |
| recall    | 1        |   0.0738411 |
| mcc       | 0.152118 |   0.521924  |


## Confusion matrix (at threshold=0.521924)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                     155 |                      18 |
| Labeled as positive |                     110 |                      30 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
