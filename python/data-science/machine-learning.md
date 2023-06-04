# Data Science

## Table of Contents

- [Data Science](#data-science)
  - [Table of Contents](#table-of-contents)
  - [Sources](#sources)
  - [Statistical Testing](#statistical-testing)
    - [ANOVA (Analysis of Variance) Test](#anova-analysis-of-variance-test)
    - [Pearson Correlation Coefficient](#pearson-correlation-coefficient)
    - [Student's T-Test](#students-t-test)
      - [Student's t-Test (Independent Samples t-test)](#students-t-test-independent-samples-t-test)
      - [Student's t-Test (Paired Sample t-test)](#students-t-test-paired-sample-t-test)
      - [Student's t-Test (One Sample t-test)](#students-t-test-one-sample-t-test)
    - [Point-Biserial Correlation Coefficient](#point-biserial-correlation-coefficient)
    - [Chi-squared Test for Independence](#chi-squared-test-for-independence)
    - [Cramer's V Statistic](#cramers-v-statistic)
    - [Yule's Y](#yules-y)
  - [Machine Learning](#machine-learning)
    - [Introduction](#introduction)
    - [Basic Model Validation](#basic-model-validation)
    - [Underfitting and Overfitting](#underfitting-and-overfitting)
    - [Missing Values](#missing-values)
    - [Data Leakage](#data-leakage)
      - [Target Leakage](#target-leakage)
      - [Train-Test Contamination](#train-test-contamination)
    - [Pre-processing](#pre-processing)
      - [Categorical Encoding](#categorical-encoding)
      - [Feature Scaling (Normalization)](#feature-scaling-normalization)
    - [Model Building Methods](#model-building-methods)
      - [Ensemble-Based Methods](#ensemble-based-methods)
        - [Decision Tree Model](#decision-tree-model)
        - [Random Forests](#random-forests)
        - [Gradient Boost](#gradient-boost)
      - [Linear Models](#linear-models)
        - [Logistic Regression (Classification)](#logistic-regression-classification)
    - [Model Selection](#model-selection)
      - [Cross-Validation: Evaluating Estimator Performance](#cross-validation-evaluating-estimator-performance)
      - [Tuning The Hyper-Parameters of an Estimator](#tuning-the-hyper-parameters-of-an-estimator)
        - [Exhaustive Grid Search](#exhaustive-grid-search)
        - [Randomized Parameter Optimization](#randomized-parameter-optimization)
      - [Metrics and Scoring: Quantifying the Quality of Predictions](#metrics-and-scoring-quantifying-the-quality-of-predictions)
        - [Receiver Operating Characteristic (ROC)](#receiver-operating-characteristic-roc)
    - [Feature Selection](#feature-selection)
      - [Removing features with low variance](#removing-features-with-low-variance)
      - [Univariate feature selection](#univariate-feature-selection)
      - [Recursive feature elimination](#recursive-feature-elimination)
      - [Feature selection using SelectFromModel](#feature-selection-using-selectfrommodel)
        - [L1-based feature selection](#l1-based-feature-selection)
          - [LASSSO Regression (implicit L1 regularization)](#lassso-regression-implicit-l1-regularization)
        - [Tree-based feature selection](#tree-based-feature-selection)
      - [Sequential Feature Selection](#sequential-feature-selection)
      - [Feature selection as part of a pipeline](#feature-selection-as-part-of-a-pipeline)
  - [Machine Learning Operations](#machine-learning-operations)
    - [ModelOps](#modelops)
    - [AI Model Lifecycle Management](#ai-model-lifecycle-management)

## Sources

- [2021 Python for Machine Learning & Data Science Masterclass](https://www.udemy.com/course/python-for-machine-learning-data-science-masterclass/)
- [Kaggle Learning](https://www.kaggle.com/learn)
- [scikit-learning Docs](https://scikit-learn.org/stable/user_guide.html)

## Statistical Testing

### ANOVA (Analysis of Variance) Test

- **ANOVA test** is used to verify whether there are significant differences between different groups in a data.
Best to be used for **combination of numerical and categorical variable** where categorical variable has two (some sources provide three) or more categories.

- The hypothesis being tested in ANOVA is:

  - **Null**: All pairs of samples are same i.e. all sample means are equal;
  - **Alternate**: At least one pair of samples is significantly different.

- Testing can be divided based on number of independent variables in a test:
  
  - **One-way test** has 1 independent variable with 2 levels (i.e. brand of cereal);
  - **Two-way test** has 2 independent variables that can have multiple levels (i.e. bran of cereal and calories).

- **Groups/Levels** are different groups within the same independent variable.

- **One Way ANOVA** is used to compare two means from two independent (unrelated) groups using the F-distribution. The null hypothesis for the test is that two means are equal. Therefore a significant result means that the two means are unequal - in other words, it is unlikely that observed differences between the data groups occured due to random chance.
**EXAMPLE:** You have a group of individuals randomly split into smaller groups and completing different tasks. For example, you might be studying the effects of tea on weight loss and form three groups: green tea, black tea, and no tea.

- **Two Way ANOVA** it is an extension of the one-way ANOVA. With a one-way, there is one independent variable affecting a dependent variable. With a two-way ANOVA, there are two independents. Two-way ANOVA can be used when there is one measurement variable and two nominal variables. In other words, when experiment has a quantitative outcome and there are two categorical explanatory variables.
**EXAMPLE:** For example, you might want to find out if there is an interaction between income and gender for anxiety level at job interviews. The anxiety level is the outcome, or the variable that can be measured. Gender and Income are the two categorical variables. These categorical variables are also the independent variables, which are called factors in a Two Way ANOVA.

```python
# ANOVA using statsmodels
import statsmodels.formula.api as smf
import statsmodels.api as sm

model = smf.ols(f'{num} ~ {cat}', data=dtf)  # uses R-style formula
fitted_model = model.fit()

table = sm.stats.anova_lm(fitted_model)

# ANOVA using scipy
import scipy

scipy.stats.f_oneway(
    dtf.loc[dtf[cat] == 1, num],
    dtf.loc[dtf[cat] == 0, num]
)
```

### Pearson Correlation Coefficient

- **Pearson Correlation Coefficient** (Pearson's r) is a measure of linear correlation between two sets of data. It is the covariance of two variables, divided by the product of their standard deviations. Essentialy, it is a normalized mesurement of the covariance so that results always has a value between -1 and 1. The measure can only reflect a linear correlation of variables, and ignores other types of relationship or correlation.

```python
scipy.stats.pearsonr(dtf[cat], dtf[num])
```

### Student's T-Test

- **t-test** is most commonly applied when the test statistic would follow a normal distribution. This test is performed on **continous variables**.

- If we observe a large p-value, for example larger than 0.05 or 0.1, then we cannot reject the null hypothesis of identical average values. If the p-value is smaller than the threshold, e.g. 1%, 5% or 10%, then we reject the null hypothesis of equal averages.

- The **t score** is a ratio between the difference between two groups and the difference within the groups. The larger the t score, the more difference there is between groups. A t score of 3 means that the groups are three times as different from each other as they are within each other.

#### Student's t-Test (Independent Samples t-test)

- **Independent Samples t-test** is used when t test is run on independent samples. This means that samples are not connected - for example tests are not conducted on the same person or thing.

- **Independent variables** should be looked at as the ones that cause something (or are thought to cause something) and cannot be changed by other variables that are being measured (examples of independent variables: gender, age).

```python
scipy.stats.ttest_ind(a, b)

# Calculating the same from descriptive statistics
scipy.stats.ttest_ind_from_stats(mean1, std1, nobs1, mean2, std2, nobs2)
```

#### Student's t-Test (Paired Sample t-test)

- **Paired t test** (dependent samples) is used to compare related observations. For example, do test scores differ significantly if the test is taken at 8 a.m. or noon?

- Choose the paired t-test if you have two measurements on the same item, person or thing. You should also choose this test if you have two items that are being measured with a unique condition. For example, you might be measuring car safety performance in Vehicle Research and Testing and subject the cars to a series of crash tests. Although the manufacturers are different, you might be subjecting them to the same conditions.

```python
scipy.stats.ttest_rel(a, b)
```

#### Student's t-Test (One Sample t-test)

- **One sample t test** is used to compare a result to an expected value. For example, do males score higher than the average of 70 on a test if their exam time is switched to 8 a.m.?

- This is a two-sided test for the null hypothesis that the expected value (mean) of a sample of independent observations a is equal to the given population mean.

```python
scipy.stats.ttest_1samp(a, popmean)
```

### Point-Biserial Correlation Coefficient

- **Point-Biserial Correlation Coefficient** is a correlation coefficient used when one variable is dichotomous. It is **mathematically equivalent to the Pearson correlation** if there is one continously measured variable and one dichotomous variable. Result is a value between -1 and 1.

```python
# Basically a Pearson correlation coefficient with t-Student test p-value
# t-Student test shows whether there are no differences between
# variables (null hypothesis) or that some differences exist.
scipy.stats.pointbiserialr(dtf[cat], dtf[num])
```

### Chi-squared Test for Independence

- **Chi-squared test for independence** (Pearson's chi-squared test) compares two variables in a **contingency table** to see if they are related. It is a way to show a relationship between two **categorical variables**.

- Chi-squared statistic is a single number that tells how much difference exists between observed counts and the counts that should be expected if there were no relationship at all in the population:
  - A **very small chi-squared test statistic** means that observed data fits the expected data extremely well (relationship).
  - A **very large chi-squared test statistic** means that data does not fit very well (no relationship).

- Pearson's chi-squared test tests **null hypothesis that frequency distribution of certain events** observed in a sample **is consistent with a particular theoretical distribution**. In other words, **null hypothesis tests if there is no relationship on the categorical variables in the population** (they are independent).

- **Contingency tables** are used to summarize the relationship between several categorical variables. A contingency table is a special type of frequency distribution table, where two variables are shown simultaneously.

- Chi-squared test does not inform about the strength of the relationship between variables - this can be validated by **Cramer's V statistic** or **Yule's Y**.

- Pearson's chi-squared statistic when calculated on large samples is likely to return a low p-value even for a table with small differences from the expected distribution proportions and therefore strength of relationship should be measured with statistics mentioned above.

```python
# If one knows expected frequencies and degrees of freedom for a given data
# then this statistic can also be calculated using scipy.stats.chisquare
cont_table = dtf.groupby([x, y]).size().unstack()  # contingency table
# Alternatively: pd.crosstab(index=dtf[x], columns=dtf[y])
chi2_test = scipy.stats.chi2_contingency(cont_table)
chi2, p = chi2_test[0], chi2_test[1]
```

### Cramer's V Statistic

- **Cramer's V** (Cramer's phi) is used as a correlation statistic. It tells whether two variables covary and by how much (0 indicates no correlation; 1 indicates perfect correlation). It is based on Pearson's chi-squared statistic.

```python
# Calculating Pearson's chi-squared statistic
cont_table = dtf.groupby([x, y]).size().unstack()
chi2_test = scipy.stats.chi2_contingency(cont_table)
chi2, p = chi2_test[0], chi2_test[1]

# Calculating Cramer's V
n = cont_table.sum().sum()
phi2 = chi2/n
r, k = cont_table.shape
phi2corr = max(0, phi2 - ((k - 1) * (r - 1)) / (n - 1))
rcorr = r - ((r - 1)**2)/(n - 1)
kcorr = k - ((k - 1)**2)/(n - 1)
coeff = np.sqrt(phi2corr / min((kcorr - 1), (rcorr - 1)))
coeff, p = round(coeff, 3), round(p, 3)
conclusion = 'Significant' if p < 0.05 else 'Non-Significant'
print(f'Cramer Correlation: {coeff}. {conclusion} p-value: {p}')
```

### Yule's Y

- **Yule's Y** (coefficient of colligation) is a measure of association between two **binary** variables (-1 reflects total negative correlation; 0 reflects no association at all; +1 reflects total positive correlation)

```python
cont_table = dtf.groupby([x, y]).size().unstack()  # contingency table
# Calculating Yule's Y
a, b, c, d = [cont_table.iloc[i, j] for i in range(2) for j in range(2)]
(np.sqrt(a*b) - np.sqrt(b*c)) / (np.sqrt(a*d) + np.sqrt(b*c))
```

## Machine Learning

### Introduction

- Step of capturing patterns from data is called **fitting** or **training** the model. The data used to **fit** the training model is called the **training data**. When process of fitting a model is completed it can be then applied to a new data to make predictions.

- **Decision tree learning** - is the predictive modelling approach used in ML. It uses a **decision tree** to go from observations (represented by **branches**) to conclusions about the item's target value (represented by **leaves**). Within the decision tree each decision happens in a **node** and results in a **split**.

- Column with the values that we want to predict is called the **prediction target** (by convention called **y**).

- Columns that are inputted into the model and then used to make predictions are called **features** (by convention called **X**).

- **Steps to bulding and using a model are**:

  - Define - what type of modela will it be?
  - Fit - capture patterns from provided data.
  - Predict.
  - Evaluate - determine how acurate the model's predictions are.

### Basic Model Validation

- Almost all of the trained models need to be evaluated. In most cases, the relevant measure of model quality is predictive accuracy (whether model's predictions are close to actual values).

- **Mean Absolute Error** (**MAE**) is a model quality metric. It is calculated based on the average of the absolute differences between actual values and predicted values:

```python
from sklearn.metrics import mean_absolute_error

predicted_home_prices = melbourne_model.predict(validation_data_features)
mean_absolute_error(validation_data_target, predicted_home_prices)
```

- **In-sample score** is a metric that has been obtained using the same sample for both building the model and evaluating it. This is not a correct approach since in the sample data some features may not be casually related with the target value. If identified pattern does not hold when the model receives new data, model would be very inaccurate when used in practice.

- The most straightforward way to avoid in-sample scoring is to split initial data to training data and **validation data**:

```python
from sklearn.model_selection import train_test_split

# split data into training and validation data, for both features and target
# The split is based on a random number generator. Supplying a numeric value to
# the random_state argument guarantees we get the same split every time we
# run this script.
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 0)
# Define model
melbourne_model = DecisionTreeRegressor()
# Fit model
melbourne_model.fit(train_X, train_y)

# get predicted prices on validation data
val_predictions = melbourne_model.predict(val_X)
print(mean_absolute_error(val_y, val_predictions))
```

### Underfitting and Overfitting

- **Overfitting** - capturing spurious patterns that won't recur in the future, leading to less accurate predictions. If a decision tree used for building a model has a large *depth* (has a large number of splits) it may end up having too many leaves that split training data into too many groups with a small sample each. In that case, given path will result in a prediction that is very close to the training values, but for a new data might end up with unreliable predictions (model adapts too much to the training data and performs badly outside the train set).

- **Underfitting** - failing to capture relevant patterns, again leading to less accurate predictions. If a decision tree is too shallow, model may end up with leaves with large sample that do not capture important distinctions and patterns in the data. In such case trained model might perform poorly in both training and new data.

- ```max_leaf_nodes``` argument provides a very sensible way to control overfitting vs underfitting. The more leaves we allow the model to make, the more we move from the underfitting to the overfitting:

```python
# Function for calculating the MEA
def get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
    model.fit(train_X, train_y)
    preds_val = model.predict(val_X)
    mae = mean_absolute_error(val_y, preds_val)
    return(mae)

for max_leaf_nodes in [5, 50, 500, 5000]:
  my_mae = get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y)
  print("Max leaf nodes: %d  \t\t Mean Absolute Error:  %d" %(max_leaf_nodes, my_mae))
```

- When model reaches its final form we can feed validation data back to the model so it becomes more accurate.

### Missing Values

There are 4 main ways to handle missing values in a dataset:

  1. Drop columns with missing values
  2. Drop rows with missing values
  3. Imputation - fill in the missing value with some number (mean, median, mode, etc.)
  4. Extension to imputation - fill in the missing value and additionally indicate in a new column that given variable was missing for a given row (*var_was_missing -> True*)

- Imputing can be done using ```SimpleImputer()```:

```python
from sklearn.impute import SimpleImputer

my_imputer = SimpleImputer()
imputed_X_train = pd.DataFrame(my_imputer.fit_transform(X_train))
imputed_X_validate = pd.DataFrame(my_imputer.transform(X_train))
```

### Data Leakage

- **Data leakage** (or leakage) happens when your training data contains information about the target, but similar data will not be available when the model is used for prediction. This leads to high performance on the training set (and possibly even the validation data), but the model will perform poorly in production. In other words, leakage causes a model to look accurate until you start making decisions with the model, and then the model becomes very inaccurate.

- There are two main types of leakage: **target leakage** and **train-test contamination**.

#### Target Leakage

- **Target leakage** occurs **when your predictors include data that will not be available at the time you make predictions**. It is important to think about target leakage in terms of the timing or chronological order that data becomes available, not merely whether a feature helps make good predictions.

- To prevent this type of data leakage, any variable updated (or created) after the target value is realized should be excluded.

#### Train-Test Contamination

- Process of validation can be corrupted in subtle ways if the validation data affects the preprocessing behavior. This is sometimes called **train-test contamination**.

- If validation is based on a simple train-test split, exclude the validation data from any type of fitting, including the fitting of preprocessing steps. This is easier if you use scikit-learn pipelines. When using cross-validation, it's even more critical that preprocessing is done inside the pipeline!

### Pre-processing

#### Categorical Encoding

- **Categorical encoding** - process of converting categories to numbers.

- **Label encoding** (```sklearn.preprocessing.LabelEncoder```) creates a set out of the provided categories and then to each unique item numerical value is assigned based on the alphabetical order of the categories. Not recommended for nominal (non-ordinal) features since model may capture ranking relationship *a < b < c*.

```python
enc = scikit.preprocessing.LabelEncoder()
enc.fit_transform(data)
```

- **One-hot encoding** (```sklearn.preprocessing.OneHotEncoder```) creates additional *dummy*/*binary* feature for each unique value in the categorical feature. It has the advantage that the **result is binary** rather than ordinal and sits in an **orthogonal vector space**. Requires checking of the **multicollinearity** refered to as **the dummy variable trap**. Additionally, one-hot encoding of the categorical variables with high cardinality can cause inefficiency in tree-based ensembles. Continuous variables will be given more importance than the dummy variables by the algorithm which will obscure the order of feature importance resulting in poorer performance - [reference](https://towardsdatascience.com/one-hot-encoding-is-making-your-tree-based-ensembles-worse-heres-why-d64b282b5769).

```python
# Using scikit's preprocessing
enc = scikit.preprocessing.OneHotEncoder(drop='first', sparse=False)
# Using drop='first' is useful when dealing with perfectly collinear
# features as these might cause problems. This, however, breaks
# the symmetry of the original representation and can therefore
# induce a bias in downstream models, for instance for penalized
# linear classification or regression models.
# Alternatively drop='if_binary'.
# Using sparse=False so that output is not in the compressed format.
x = enc.fit_transform(data)
x.index = data.index  # one-hot encoding removes index

# Using pandas functionality
pd.get_dummies(data, columns=['col_name'], drop_first=True))
```

#### Feature Scaling (Normalization)

- **Rescaling (min-max normalization)r** - is the simplest method and consists in rescaling the range of features to scale the range in [0, 1] or [−1, 1]. It is less affected by the outliers but compresses all inliers in a narrow range.
$$x' = \frac{x - min(x)}{max(x) - min(x)}$$

- **Mean normalization**
$$x' = \frac{x - average(x)}{max(x) - min(x)}$$

- **Standardization (Z-score Normalization)** - assumes data is normally distributed and rescales it such that the distribution centres around 0 with a standard deviation of 1. However, the outliers have an influence when computing the empirical mean and standard deviation which shrink the range of the feature values, therefore this scaler cannot guarantee balanced feature scales in the presence of outliers.
$$x' = \frac{x - average(x)}{\sigma}$$

- **Scaling to unit length** - aother option that is widely used in machine-learning is to scale the components of a feature vector such that the complete vector has length one. This usually means dividing each component by the Euclidean length of the vector:
$$x' = \frac{x}{||x||}$$

### Model Building Methods

#### Ensemble-Based Methods

##### Decision Tree Model

- Basic example of defininng a decision tree model with **scikit-learn** and fitting it with the features and target variable:

```python
from sklearn.tree import DecisionTreeRegressor

# Define model. Specify a number for random_state to ensure same results each run
melbourne_model = DecisionTreeRegressor(random_state=1)  # creates a new, untrained model

# Fit model
melbourne_model.fit(X, y)

# Making predictions on a sample data:
melbourne_model.predict(X.head())
```

##### Random Forests

- **Random forest** uses many decision trees, making predictions by averaging the predictions of each component tree. Usually, this model has much better predictive accuracy than a single tree. There is a small trade-off though - random forest model's interpretability is harder as it is no longer based on a 'starting-node-to-leaf' path within a single decision tree:

```python
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

forest_model = RandomForestRegressor(random_state=1)
forest_model.fit(train_X, train_y)
melb_preds = forest_model.predict(val_X)
print(mean_absolute_error(val_y, melb_preds))
```

- Random forest model can be tuned in a similar way as decision tree model by adjusting its depth with ```max_leaf_nodes``` parameter value.

##### Gradient Boost

- **Gradient Boosting** is a machine learning technique for **regression and classification problems**, which produces a prediction model in the form of an ensemble of weak prediction models, typically decision trees. When a decision tree is the weak learner, the resulting algorithm is called gradient boosted trees, which usually outperforms random forest.

- Gradient boosting **builds an additive model in a forward stage-wise fashion**. It allows for the optimization of arbitrary differentiable loss functions. In each stage ```n_classes_``` regression trees are fit on the negative gradient of the binomial or multinomial deviance loss function. Binary classification is a special case where only a single regression tree is induced.

- Gradient boost starts by making a single leaf instead of a tree or stump. This leaf represents an initial guess for dependant variable of all of the samples. It usually starts with the average value for regression and with $log(odds)$ which is $\log{\frac{p}{1-p}}$ for classification.

- Gradient boost builds fixed sized trees based on the previous tree's errors (unlike in AdaBoost each tree can be larger than a stump). New tree prediction output is added to the previous prediction, but it is additionally scaled down by a **learning rate** that is a fixed value (unlike in AdaBoost). New trees are added to the model unles desired number of trees is reached or until additional trees fail to improve the fit.

- Most commonly used **loss function for regression** with gradient boost is $\frac{1}{2}(Observed - Predicted)^2$ which is the same loss function as the one used in linear regression but divided by 2.

- Most commonly used **loss function for classification** with gradient boost is a function of the predicted $log(odds)$ - $-Observed\times\log{odds} + \log{(1+e^{\log{odds}})}$ which is converted from the negative $log(likelihood)$ of the data, which is a function of the predicted probability *p*. The better the prediction, the larger the $log(likelihood)$, and this is why, when doing the logistic regression, the goal is to maximize its value.

- Reasonable amount of leaves is between 8 and 32.

```python
best_model_params = { 'subsample': 0.8,
                      'n_estimators': 1500,
                      'min_samples_split': 40,
                      'min_samples_leaf': 1,
                      'max_features': 6,
                      'max_depth': 4,
                      'learning_rate': 0.01}
model = ensemble.GradientBoostingClassifier(**best_model_params)
```

General description of gradient boosting from Kaggle:

- Gradient boosting is a method that goes through cycles to iteratively add models into an ensemble.

- It begins by initializing the ensemble with a single model, whose predictions can be pretty naive. (Even if its predictions are wildly inaccurate, subsequent additions to the ensemble will address those errors.) Then, we start the cycle:

  - First, we use the current ensemble to generate predictions for each observation in the dataset. To make a prediction, we add the predictions from all models in the ensemble.
  - These predictions are used to calculate a loss function (like mean squared error, for instance).
  - Then, we use the loss function to fit a new model that will be added to the ensemble. Specifically, we determine model parameters so that adding this new model to the ensemble will reduce the loss. (Side note: The "gradient" in "gradient boosting" refers to the fact that we'll use gradient descent on the loss function to determine the parameters in this new model.)
  - Finally, we add the new model to ensemble, and ...
  - ... repeat!

- ```XGBoost``` is technically more advanced than the sci-kit's implementation of the gradient boosting. In-depth explanation of gradient boosting can be found [here](https://www.kaggle.com/alexisbcook/xgboost):

```python
from xgboost import XGBRegressor

my_model = XGBRegressor(n_estimators=1000, learning_rate=0.05, n_jobs=4)
my_model.fit(X_train, y_train, 
             early_stopping_rounds=5, 
             eval_set=[(X_valid, y_valid)], 
             verbose=False)
```

#### Linear Models

##### Logistic Regression (Classification)

- **Logistic regression** is a linear model for classification. Logistic regression is also known in the literature as logit regression, maximum-entropy classification (MaxEnt) or the log-linear classifier. In this model, the probabilities describing the possible outcomes of a single trial are modeled using a logistic function.

- Logistic regression is implemented in ```sklearn.linear_model.LogisticRegression```. This implementation can fit binary, One-vs-Rest, or multinomial logistic regression with optional L1, L2 or Elastic-Net regularization.

```python
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
X, y = load_iris(return_X_y=True)
clf = LogisticRegression(random_state=0).fit(X, y)
clf.predict(X[:2, :])
```

### Model Selection

#### Cross-Validation: Evaluating Estimator Performance

- **Cross-validation** (also called rotation estimation or out-of-sample testing) is any of various similar model validation techniques for assessing how the results of a statistical analysis will generalize to an independent data set.

- Cross-validation does not waste data since it does not require making 3 subsets of it (training data, validation data, test data). Instead CV uses **k-fold** approach in which training data is split into *k* smaller sets. Then model is trained using following procedure:

  - A model is trained using *k - 1* of the folds as training data;
  - the resulting model is validated on the remaining part of the data (i.e., it is used as a test set to compute a performance measure such as accuracy).

- The performance measure reported by *k*-fold cross-validation is then the average of the values computed in the loop. This approach can be computationally expensive, but does not waste too much data (as is the case when fixing an arbitrary validation set), which is a major advantage in problems such as inverse inference where the number of samples is very small.

- It is mainly used in settings where the goal is prediction, and one wants to estimate how accurately a predictive model will perform in practice. In a prediction problem, a model is usually given a dataset of known data on which training is run (training dataset), and a dataset of unknown data (or first seen data) against which the model is tested (called the validation dataset or testing set). The **goal of cross-validation is to test the model's ability to predict new data that was not used in estimating it**, in order **to flag problems like overfitting or selection bias and to give an insight on how the model will generalize to an independent dataset** (i.e., an unknown dataset, for instance from a real problem).

- Scikit-learn provides 2 main approaches to CV:

  - **cross-validation generator** - a non-estimator family of classes used to split a dataset into a sequence of train and test portions, by providing ```split``` and ```get_n_splits``` methods. Note that unlike estimators, these do not have ```fit``` methods and do not provide ```set_params``` or ```get_params```. Parameter validation may be performed in ```__init__```.
  The simplest way to use cross-validation this way is to call the ```cross_val_score``` helper function on the estimator and the dataset:

  ```python
  from sklearn.model_selection import cross_val_score
  clf = svm.SVC(kernel='linear', C=1, random_state=42)
  scores = cross_val_score(clf, X, y, cv=5)
  
  # The mean score and the standard deviation are hence given by:
  print("%0.2f accuracy with a standard deviation of %0.2f" % (scores.mean(), scores.std()))

  # By default, the score computed at each CV iteration is the score
  # method of the estimator. It is possible to change this by using
  # the scoring parameter:
  from sklearn import metrics
  scores = cross_val_score(
    clf, X, y, cv=5, scoring='f1_macro')
  ```
  
  - **cross-validation estimator** - an estimator that has built-in cross-validation capabilities to automatically select the best hyper-parameters. Some example of cross-validation estimators are ```ElasticNetCV``` and ```LogisticRegressionCV```. Cross-validation estimators are named *EstimatorCV* and tend to be roughly equivalent to ```GridSearchCV(Estimator(), ...)```. The advantage of using a cross-validation estimator over the canonical estimator class along with grid search is that they can take advantage of warm-starting by reusing precomputed results in the previous steps of the cross-validation process. This generally leads to speed improvements. An exception is the ```RidgeCV``` class, which can instead perform efficient Leave-One-Out CV.

- ```model_selection.StratifiedKFold``` can be used to cross-validate samples that have classes (f.e. classiffication models). The folds are made by preserving the percentage of samples for each class.

#### Tuning The Hyper-Parameters of an Estimator

- **Hyper-parameters** are parameters that are not directly learnt within estimators. In scikit-learn they are passed as arguments to the constructor of the estimator classes. Typical examples include ```C```, ```kernel``` and ```gamma``` for Support Vector Classifier, ```alpha``` for Lasso, etc.

- It is possible and recommended to search the hyper-parameter space for the best cross validation score. Any parameter provided when constructing an estimator may be optimized in this manner.

- Two generic approaches to parameter search are provided in scikit-learn: for given values, ```GridSearchCV``` exhaustively considers all parameter combinations, while ```RandomizedSearchCV``` can sample a given number of candidates from a parameter space with a specified distribution. Both these tools have successive halving counterparts ```HalvingGridSearchCV``` and ```HalvingRandomSearchCV```, which can be much faster at finding a good parameter combination.

- Some parameter settings may result in a failure to fit one or more folds of the data. By default, this will cause the entire search to fail, even if some parameter settings could be fully evaluated. Setting ```error_score=0``` (or ```=np.NaN```) will make the procedure robust to such failure, issuing a warning and setting the score for that fold to 0 (or NaN), but completing the search.

- Try starting with a **gradient boosting algorithm** (like XGBoost). Since there are lots of hyperparameters ```RandomizedSearchCV``` can be used for their tuning.

##### Exhaustive Grid Search

- ```GridSearchCV``` - exhaustive search over specified parameter values for an estimator.

- GridSearchCV implements a “fit” and a “score” method. It also implements “score_samples”, “predict”, “predict_proba”, “decision_function”, “transform” and “inverse_transform” if they are implemented in the estimator used.

- The parameters of the estimator used to apply these methods are optimized by cross-validated grid-search over a parameter grid.

##### Randomized Parameter Optimization

- ```RandomizedSearchCV``` performs a randomized search on hyperparameters.

- ```RandomizedSearchCV``` implements a “fit” and a “score” method. It also implements “score_samples”, “predict”, “predict_proba”, “decision_function”, “transform” and “inverse_transform” if they are implemented in the estimator used.

- The parameters of the estimator used to apply these methods are optimized by cross-validated search over parameter settings.

- In contrast to ```GridSearchCV```, **not all parameter values are tried out**, but rather a fixed number of parameter settings (given by ```n_iter```) is sampled from the specified distributions. The **number of parameter settings that are tried is given** by ```n_iter```. In summary, randomized search on hyperparameters has two main benefits over an exhaustive search:

  - A budget can be chosen independent of the number of parameters and possible values.
  - Adding parameters that do not influence the performance does not decrease efficiency.

- If all parameters are presented as a list, sampling without replacement is performed. If at least one parameter is given as a distribution, sampling with replacement is used. **It is highly recommended to use continuous distributions for continuous parameters** (f.e. ```C```).

- **Important parameters:**

  - ```n_iter``` - number of parameter settings that are sampled. ```n_iter``` trades off runtime vs quality of the solution.

  - ```param_distributions``` - dictionary with parameters names (```str```) as keys and distributions or lists of parameters to try. Distributions must provide a ```rvs``` method for sampling (such as those from ```scipy.stats.distributions```). If a list is given, it is sampled uniformly. If a list of dicts is given, first a dict is sampled uniformly, and then a parameter is sampled using that dict as above.

  - ```scoring``` - strategy to evaluate the performance of the cross-validated model on the test set. By default, parameter search uses the score function of the estimator to evaluate a parameter setting. These are the ```sklearn.metrics.accuracy_score``` for classification and ```sklearn.metrics.r2_score``` for regression. An alternative scoring function can be specified via the scoring parameter of most parameter search tools. [Predefined scoring functions on scikit-learn](https://scikit-learn.org/stable/modules/model_evaluation.html#scoring-parameter).

```python
## Trying gradient boosting algorithm

## calling model
model = ensemble.GradientBoostingClassifier()

## define hyperparameters combinations to try
param_dic = {'learning_rate':[0.15,0.1,0.05,0.01,0.005,0.001],  #weighting factor for the corrections by new trees when added to the model
'n_estimators':[100,250,500,750,1000,1250,1500,1750],  #number of trees added to the model
'max_depth':[2,3,4,5,6,7],  #maximum depth of the tree
'min_samples_split':[2,4,6,8,10,20,40,60,100],  #sets the minimum number of samples to split
'min_samples_leaf':[1,3,5,7,9],  #the minimum number of samples to form a leaf
'max_features':[2,3,4,5,6,7],  #square root of features is usually a good starting point
'subsample':[0.7,0.75,0.8,0.85,0.9,0.95,1]}  #the fraction of samples to be used for fitting the individual base learners. Values lower than 1 generally lead to a reduction of variance and an increase in bias.

## random search
random_search = model_selection.RandomizedSearchCV(
  model,
  param_distributions=param_dic,
  n_iter=1000,
  scoring='accuracy'
).fit(X_train, y_train)

print(f'Best Model parameteres: {random_search.best_params_}')
print(f'Best Model mean accuracy: {random_search.best_score_}')

model = random_search.best_estimator_
```

#### Metrics and Scoring: Quantifying the Quality of Predictions

- There are 3 different APIs for evaluating the quality of a model’s predictions:

  - **Estimator score method**: Estimators have a ```score``` method providing a default evaluation criterion for the problem they are designed to solve.
  
  - **Scoring parameter**: Model-evaluation tools using cross-validation (such as ```model_selection.cross_val_score``` and ```model_selection.GridSearchCV```) rely on an internal scoring strategy.
  
  - **Metric functions**: The ```sklearn.metrics``` module implements functions assessing prediction error for specific purposes.

##### Receiver Operating Characteristic (ROC)

- **Receiver operating characteristic** (ROC, ROC curve)  is a graphical plot which illustrates the performance of a binary classifier system as its discrimination threshold is varied. It is created by plotting the fraction of true positives out of the positives (**TPR** = true positive rate) vs. the fraction of false positives out of the negatives (**FPR** = false positive rate), at various threshold settings. TPR is also known as sensitivity, and FPR is one minus the specificity or true negative rate.

- The ```roc_auc_score``` function computes the area under the receiver operating characteristic (ROC) curve, which is also denoted by AUC or AUROC. By computing the area under the roc curve, the curve information is summarized in one number. For more information see the Wikipedia article on AUC.

### Feature Selection

#### Removing features with low variance

- This is a simple baseline approach to feature selection. All features whose variance does not meet some threshold will be removed. By default, this approach removes all zero-variance features (features that have the same value in all samples).

```python
from sklearn.feature_selection import VarianceThreshold
X = [[0, 0, 1], [0, 1, 0], [1, 0, 0], [0, 1, 1], [0, 1, 0], [0, 1, 1]]
sel = VarianceThreshold(threshold=(.8 * (1 - .8)))
sel.fit_transform(X)
array([[0, 1],
       [1, 0],
       [0, 0],
       [1, 1],
       [1, 0],
       [1, 1]])
```

#### Univariate feature selection

- Univariate feature selection that works by choosing *k* best features based on the computed univariate statistical tests:

  - ```SelectKBest``` removes all but the *k* highest scoring features;
  - ```SelectPercentile``` removes all but a user-specified highest scoring percentage of features;
  - using common univariate statistical tests for each feature: false positive rate ```SelectFpr```, false discovery rate ```SelectFdr```, or family wise error ```SelectFwe```;
  - ```GenericUnivariateSelect``` allows to perform univariate feature selection with a configurable strategy. This allows to select the best univariate selection strategy with hyper-parameter search estimator.

```python
# Univariate feature selection based on statistical tests
# using ANOVA F-values (suitable only for classification)
selector = feature_selection.SelectKBest(k=10).fit(X, y)
anova_selected_features = feature_names[selector.get_params()]
```

- These objects take as input a scoring function that returns univariate scores and p-values (or only scores for ```SelectKBest``` and ```SelectPercentile```):

  - For regression: ```f_regression```, ```mutual_info_regression```,
  - For classification: ```chi2```, ```f_classif```, ```mutual_info_classif```.

- The methods based on F-test estimate the degree of linear dependency between two random variables. On the other hand, mutual information methods can capture any kind of statistical dependency, but being nonparametric, they require more samples for accurate estimation.

- If you use sparse data (i.e. data represented as sparse matrices), ```chi2```, ```mutual_info_regression```, ```mutual_info_classif``` will deal with the data without making it dense.

- **Beware not to use a regression scoring function with a classification problem**, you will get useless results.

#### Recursive feature elimination

- Given an external estimator that assigns weights to features (e.g., the coefficients of a linear model), the goal of recursive feature elimination (RFE) is to select features by recursively considering smaller and smaller sets of features. First, the estimator is trained on the initial set of features and the importance of each feature is obtained either through any specific attribute (such as coef_, feature_importances_) or callable. Then, the least important features are pruned from current set of features. That procedure is recursively repeated on the pruned set until the desired number of features to select is eventually reached.

- ```RFECV``` performs RFE in a cross-validation loop to find the optimal number of features.

#### Feature selection using SelectFromModel

- ```SelectFromModel``` is a meta-transformer that can be used along with any estimator that importance of each feature through a specific attribute (such as coef_, feature_importances_) or callable after fitting. The features are considered unimportant and removed, if the corresponding importance of the feature values are below the provided threshold parameter. Apart from specifying the threshold numerically, there are built-in heuristics for finding a threshold using a string argument. Available heuristics are “mean”, “median” and float multiples of these like “0.1*mean”. In combination with the threshold criteria, one can use the max_features parameter to set a limit on the number of features to select.

##### L1-based feature selection

- Linear models penalized with the L1 norm have sparse solutions: many of their estimated coefficients are zero. When the goal is to reduce the dimensionality of the data to use with another classifier, they can be used along with ```SelectFromModel``` to select the non-zero coefficients. In particular, sparse estimators useful for this purpose are the ```Lasso``` for regression, and of ```LogisticRegression``` and ```LinearSVC``` for classification:

```python
# Selecting features for a logistic regression classifier model
# that uses LASSO regularization (adding L1 penalty to absolute
# value of the magnitude of coefficients) and therefore yields
# sparse models
selector = feature_selection.SelectFromModel(
    estimator=linear_model.LogisticRegression(
        C=1,
        penalty='l1',
        solver='liblinear'
    ),
    max_features=10
).fit(X, y)
lasso_selected_features = feature_names[selector.get_support()]
```

- With SVMs and logistic-regression, the parameter *C* controls the sparsity: the smaller *C* the fewer features selected. With Lasso, the higher the alpha parameter, the fewer features selected.

###### LASSSO Regression (implicit L1 regularization)

- **Lasso** (least absolute shrinkage and selection operator) is a regression analysis method that **performs both variable selection and regularization** in order to enhance the prediction accuracy and interpretability of the resulting statistical model. Lasso regression is a type of linear regression that uses **shrinkage**. The lasso procedure encourages simple, sparse models (i.e. models with fewer parameters). This particular type of regression is **well-suited for models showing high levels of muticollinearity** or when you want to automate certain parts of model selection, like variable selection/parameter elimination.

- **Lasso regression performs L1 regularization**, which adds a **penalty equal to the absolute value of the magnitude of coefficients**. This type of regularization can result in sparse models with few coefficients; Some coefficients can become zero and eliminated from the model. Larger penalties result in coefficient values closer to zero, which is the ideal for producing simpler models. On the other hand, **L2 regularization** (e.g. Ridge regression) doesn’t result in elimination of coefficients or sparse models as it adds penalty equal to the square of the magnitude of coefficients (all coefficients are shrunk by the same factor and none are eliminated). This makes the Lasso far easier to interpret than the Ridge.

- **Shrinkage** is where data values are shrunk towards a central point, like the mean. Shrinking data can result in:

  Advantages:
  - Better, more stable, estimates for true population parameters,
  - Reduced sampling and non-sampling errors,
  - Smoothed spatial fluctuations.

  Disadvantages:
  - Serious errors if the population has an atypical mean. Knowing which means are 'typical' and which are 'atypical' can be difficult and sometimes impossible.
  - Shrunk estimators can become biased estimators, tending to underestimate the true population parameters.
  - Shrunk fitted models can perform more poorly on new data sets compared to the original data set used for fitting. Specifically, r-squared “shrinks.”

##### Tree-based feature selection

- Tree-based estimators (see the ```sklearn.tree``` module and forest of trees in the ```sklearn.ensemble``` module) can be used to compute **impurity-based feature importances**, which in turn can be used to discard irrelevant features (when coupled with the ```SelectFromModel``` meta-transformer).

- **The impurity-based feature importances** - The higher, the more important the feature. The importance of a feature is computed as the (normalized) total reduction of the criterion brought by that feature. It is also known as the **Gini importance**.

- Impurity-based feature importances **can be misleading for high cardinality features** (many unique values). See ```sklearn.inspection.permutation_importance``` as an alternative.

```python
from sklearn.ensemble import ExtraTreesClassifier, RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectFromModel
X, y = load_iris(return_X_y=True)
clf = ExtraTreesClassifier(n_estimators=50)
clf = clf.fit(X, y)
clf.feature_importances_  
model = SelectFromModel(clf, prefit=True)

# Extracting feature importances
X = X_train.values
y = y_train.values
feature_names = X_train.columns

model = ensemble.RandomForestClassifier(
    n_estimators=100,
    criterion='entropy',
    random_state=42
)
model.fit(X, y)
importances = model.feature_importances_
```

#### Sequential Feature Selection

- Sequential Feature Selection (SFS) is available in the ```SequentialFeatureSelector``` transformer. SFS can be either forward or backward:

  - **Forward-SFS** is a greedy procedure that iteratively finds the best new feature to add to the set of selected features. Concretely, we initially start with zero feature and find the one feature that maximizes a cross-validated score when an estimator is trained on this single feature. Once that first feature is selected, we repeat the procedure by adding a new feature to the set of selected features. The procedure stops when the desired number of selected features is reached, as determined by the ```n_features_to_select``` parameter.
  
  - **Backward-SFS** follows the same idea but works in the opposite direction: instead of starting with no feature and greedily adding features, we start with all the features and greedily remove features from the set. The ```direction``` parameter controls whether forward or backward SFS is used.
  
- In general, forward and backward selection do not yield equivalent results. Also, one may be much faster than the other depending on the requested number of selected features: if we have 10 features and ask for 7 selected features, forward selection would need to perform 7 iterations while backward selection would only need to perform 3.

- SFS differs from ```RFE``` and ```SelectFromModel``` in that it does not require the underlying model to expose a ```coef_``` or ```feature_importances_``` attribute. It may however be slower considering that more models need to be evaluated, compared to the other approaches. For example in backward selection, the iteration going from m features to *m - 1* features using k-fold cross-validation requires fitting *m* k* models, while ```RFE``` would require only a single fit, and ```SelectFromModel``` always just does a single fit and requires no iterations.

#### Feature selection as part of a pipeline

- Feature selection is usually used as a pre-processing step before doing the actual learning. The recommended way to do this in scikit-learn is to use a ```Pipeline```:

```python
clf = Pipeline([
  ('feature_selection', SelectFromModel(LinearSVC(penalty="l1"))),
  ('classification', RandomForestClassifier())
])
clf.fit(X, y)
```

- In this snippet we make use of a ```LinearSVC``` coupled with ```SelectFromModel``` to evaluate feature importances and select the most relevant features. Then, a ```RandomForestClassifier``` is trained on the transformed output, i.e. using only relevant features. You can perform similar operations with the other feature selection methods and also classifiers that provide a way to evaluate feature importances of course. See the Pipeline examples for more details.

## Machine Learning Operations

### ModelOps

- **ModelOps** (model operations) is focused primarily on the governance and life cycle management of a wide range of operationalized AI and decision models. It is a holistic approach for rapidly and iteratively moving models through the analytics life cycle so they are deployed faster and deliver expected business value.

- It orchestrates the model life cycles of all models in production across the entire enterprise, from putting a model into production, then evaluating and updating the resulting application according to a set of governance rules, including both technical and business KPI's. It grants business domain experts the capability to evaluate AI models in production, independent of data scientists.

- ModelOps is the process of taking all kind of predictive analytics/machine learning workflows and making them operational. Actually using them in the business so there make the desired impact on a day-to-day business activities rather than just providing static insights. This is required due to the scale at which models are being produced.

- ModelOps are responsible for developing ModelOps Lifecycles.

- **Models** are technical artifacts deployed in end-user applications that help drive automated decisioning with the software the operates the business.

- Business value of an application is a major component of accountability for models.

- [Model Lifecycle](file://C:\Users\mdebs\Documents\GitHub\udemy-python-for-machine-learning\model-lifecycle.png), [Model Lifecycle 2 p1](file://C:\Users\mdebs\Documents\GitHub\udemy-python-for-machine-learning\model-lifecycle_2_p1.png) and [Model Lifecycle 2 p2](file://C:\Users\mdebs\Documents\GitHub\udemy-python-for-machine-learning\model-lifecycle_2_p2.png)

- [ModelOps Cycle](https://upload.wikimedia.org/wikipedia/commons/5/52/ModelOpsFlow.png)

- Effective monitoring must address four aspects of the model:

  - Operations: Model is meeting SLA performance and expected decisioning rate;
  - Quality: Decisioning and outcomes are producing optimal results;
  - Risk: Outcomes are ethically fair and unbiased and operating within compliance thresholds;
  - Processes: Operational and governance processes and gates are properly followed.

- The goal for developing ModelOps was to address the gap between model deployment and model governance, ensuring that all models were running in production with strong governance, aligned with technical and business KPI's, while managing the risk.

- ModelOps automates the model life cycle of models in production. Such automation includes designing the model life cycle, inclusive of technical, business and compliance KPI's and thresholds, to govern and monitor the model as it runs, monitoring the models for bias and other technical and business anomalies, and updating the model as needed without disrupting the applications. ModelOps is the dispatcher that keeps all of the trains running on time and on the right track, ensuring risk control, compliance and business performance. The orchestration, governance, retraining, monitoring, and refreshing is done with ModelOps.

- The ModelOps process focuses on automating the governance, management and monitoring of models in production across the enterprise, enabling AI and application developers to easily plug in life cycle capabilities (such as bias-detection, robustness and reliability, drift detection, technical, business and compliance KPI's, regulatory constraints and approval flows) for putting AI models into production as business applications. The process starts with a standard representation of candidate models for production that includes a metamodel (the model specification) with all of the component and dependent pieces that go into building the model, such as the data, the hardware and software environments, the classifiers, and code plug-ins, and most importantly, the business and compliance/risk KPI's.

- ModelOps is a DevOps variation that share foundations: version control, deployment automation, continuous integration, test automation, test data management, shift left on security, loosely coupled architecture, empowered teams (choosing their own tools), monitoring, and proactive notification.

- ModelOps’ responsibilities include workflow automation, version management, promotions, compute resource management, monitoring, and scaling and tuning.

- The main idea behind ModelOps is to get maximum business value out of the models by operationalizing and putting analytics to work.

### AI Model Lifecycle Management

- During the infusion of AI, we need to collect data, train the data, build a model, deploy the model, and run the predictor.

- In enterprise, the critical role of AI requires a well-defined and robust methodology and platform, and a business may even fail if its methodology and platform are not up to par. For example, if fraud detection makes bad decisions, a business will be negatively affected. In the long pipeline for AI, response time, quality, fairness, explainability, and other elements must be managed as part of the whole lifecycle. It is impossible to manage them individually.

- AI Model Lifecycle Management manages the complicated AI pipeline and helps ensure the necessary results in enterprise.

- [AI Model Lifecycle](https://1.cms.s81c.com/sites/default/files/2020-11-05/Screen%20Shot%202020-11-05%20at%209.05.37%20AM.png):

  - collect - collect data and make it accessible,
  - organize - create business-ready analytics foundation,
  - analyze - build and scale AI,
  - infuse - operationalize AI throughout a business
  - quality check - during the whole pipelining, data governance for AI Model Lifecycle Management should monitor and give feedback regarding quality, fairness, and explainability.
