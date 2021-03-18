# Summary of 57_NeuralNetwork

[<< Go back](../README.md)


## Neural Network
- **n_jobs**: -1
- **dense_1_size**: 32
- **dense_2_size**: 4
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

0.8 seconds

## Metric details
|           |    score |    threshold |
|:----------|---------:|-------------:|
| logloss   | 0.722876 | nan          |
| auc       | 0.54737  | nan          |
| f1        | 0.656716 |   0.137177   |
| accuracy  | 0.56     |   0.437532   |
| precision | 0.75     |   0.764166   |
| recall    | 1        |   0.00934735 |
| mcc       | 0.121609 |   0.408821   |


## Confusion matrix (at threshold=0.437532)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                      85 |                      56 |
| Labeled as positive |                      65 |                      69 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
