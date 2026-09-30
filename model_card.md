# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details

The model is a Random Forest classifier built using scikit-learn.  It predicts wether a person's yearly salary is greater than $50,000 or less that or equal to $50,000.  This information is based on census data.  A random state of 42 was used to make the training process reproducible.

## Intended Use

The model is intended for educational purposes to demonstrate how to build, evaluate, and deploy a machine learning model through an API.  It should not be used for an real-world decisions.

## Training Data

The model was trained using the census income dataset.  The dataset contains demographic and employment-related features such as age, workclass, education, marital status, occupation, relationship, race, sex, hours worked per week, and native country.  The salary column is the target variable.

## Evaluation Data

Twenty percent of the census income dataset was designated for test data.  A random state of 42 was used for reproducibility, and the split was stratified by the salary label to help preserve the distribution of classes.  The test data was processed using the encoder that was fitted on the training data.

## Metrics

Model performance was evaluated using precision, recall, and F1 score.  On the test dataset, the model achieved a percision of 0.7353, recall of 0.6378, and F1 score of 0.6831.  Performance was also evaluated across individual values of the categorical features.  For example, for the federal-gov workclass slice, the model achieved a precision of 0.7324, recall of 0.6842, and F1 score of 0.7075.  Performance varied across slices.  Metrics based on very small numbers of observations should be interpreted carefully.

## Ethical Considerations

The dataset contains sensitive demographic attributes, including race and sex.  Historical census data may reflect social and economic inequalities that can be learned by a machine learning model.  As a result, predicitions may differ across demographic groups.  The model should not be used as the sole basis for decisions that could affect employment, credit, benefits, or other opportunities.

## Caveats and Recommendations

The model was trained on historical census data, so its performance may not represent current populations or economic conditions.  Some categorical slices contain very few observations, making their performance metrics unreliable.  A slice containing only one observation may report perfect scores even though there is not enough data to conclude that the model performs well for that group.  Future work could include additional model tuning, cross-validation, comparison with other classification algoriths, and a more detailed evaluation of performance across demogrpahic groups.