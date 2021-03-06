# Summary of 110_Xgboost_SelectedFeatures

[<< Go back](../README.md)


## Extreme Gradient Boosting (Xgboost)
- **n_jobs**: -1
- **objective**: binary:logistic
- **eval_metric**: logloss
- **eta**: 0.15
- **max_depth**: 6
- **min_child_weight**: 5
- **subsample**: 0.6
- **colsample_bytree**: 0.8
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
| logloss   | 0.630735 |  nan        |
| auc       | 0.688068 |  nan        |
| f1        | 0.668435 |    0.330561 |
| accuracy  | 0.642173 |    0.522774 |
| precision | 0.823529 |    0.696671 |
| recall    | 1        |    0.109061 |
| mcc       | 0.299618 |    0.330561 |


## Confusion matrix (at threshold=0.522774)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                     128 |                      45 |
| Labeled as positive |                      67 |                      73 |

## Learning curves
![Learning curves](learning_curves.png)

[<< Go back](../README.md)
