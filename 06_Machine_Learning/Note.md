# Statistical Tests and Machine-Learning Models

In a data science project, statistical hypothesis tests and machine-learning models serve different purposes.

## Exploratory Data Analysis and Hypothesis Testing

Exploratory Data Analysis (EDA) helps us discover patterns in our data, such as observing that smokers have higher medical charges than non-smokers.

A statistical test, such as an independent *t*-test, can then be used when we specifically want to determine whether the observed difference between two groups is statistically significant and supported by evidence beyond random sampling variation.

## Machine-Learning Models

A hypothesis test is not a mandatory step before building a machine-learning model. If our goal is prediction, we can directly preprocess the data, train a model, and evaluate its predictive performance using metrics such as:

- **MAE** (Mean Absolute Error)
- **RMSE** (Root Mean Squared Error)
- **R²** (coefficient of determination)

This is what we did with the Medical Cost dataset. In that case, the model's purpose is to predict a person's medical charges, while the *t*-test's purpose is to answer a different question about the data.

## Key Takeaway

Statistical tests should be viewed as tools for answering specific inference or research questions, not as compulsory preprocessing steps for every machine-learning model.
