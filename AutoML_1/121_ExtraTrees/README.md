# Summary of 121_ExtraTrees

[<< Go back](../README.md)


## Extra Trees Classifier (Extra Trees)
- **n_jobs**: -1
- **criterion**: gini
- **max_features**: 0.9
- **min_samples_split**: 50
- **max_depth**: 3
- **explain_level**: 0

## Validation
 - **validation_type**: kfold
 - **shuffle**: True
 - **stratify**: True
 - **k_folds**: 5

## Optimized metric
logloss

## Training time

5.1 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.665503 |  nan        |
| auc       | 0.620087 |  nan        |
| f1        | 0.637838 |    0.408842 |
| accuracy  | 0.603834 |    0.500211 |
| precision | 0.714286 |    0.629181 |
| recall    | 1        |    0.132328 |
| mcc       | 0.225177 |    0.410387 |


## Confusion matrix (at threshold=0.500211)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                     133 |                      40 |
| Labeled as positive |                      84 |                      56 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
