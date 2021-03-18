# Summary of 79_RandomForest

[<< Go back](../README.md)


## Random Forest
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

3.0 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.661036 |  nan        |
| auc       | 0.648777 |  nan        |
| f1        | 0.674772 |    0.39488  |
| accuracy  | 0.629091 |    0.489699 |
| precision | 1        |    0.789557 |
| recall    | 1        |    0.116009 |
| mcc       | 0.25726  |    0.489699 |


## Confusion matrix (at threshold=0.489699)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                      92 |                      49 |
| Labeled as positive |                      53 |                      81 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
