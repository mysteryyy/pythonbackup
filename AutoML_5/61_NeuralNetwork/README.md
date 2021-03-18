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
 - **k_folds**: 10

## Optimized metric
logloss

## Training time

2.5 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.57973  | nan         |
| auc       | 0.762011 | nan         |
| f1        | 0.766773 |   0.492763  |
| accuracy  | 0.734545 |   0.492763  |
| precision | 0.958333 |   0.860883  |
| recall    | 1        |   0.0156142 |
| mcc       | 0.463249 |   0.492763  |


## Confusion matrix (at threshold=0.492763)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                      82 |                      44 |
| Labeled as positive |                      29 |                     120 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
