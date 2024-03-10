# Statistics and Probabilty

## Statistics for Data Science and Business Analysis

- Notes based on [Statistics for Data Science and Business Analysis](https://learning.oreilly.com/videos/statistics-for-data/9781789803259/).

### Population and Sample

- **Population** (*N*) - collection of all items of intereset to our study. Hard to define and hard to observe.

- **Sample** (*n*) - subset of the population. Good sample should be **random** and **representative**:

  - Representative sample - sample that accurately reflects the population;
  - Random sample - when each member of the population has an equal chance of being chosen.

### Fundamentals of Descriptive Statistics

- **Types of data**:

  - **Categorical** - describes categories/groups or yes/no questions.
  - **Numerical** (if not sure whether data is numerical try to interpret the mean):
    - Discrete - finite integer.
    - Continous - impossible to count exactly.

- **Levels of measurement**:
  - **Qualitative**:
    - Nominal - are not numbers and cannot be put in any specific order;
    - Ordinal - consists of groups/categories, but follows a strict order (f.e. scale of happinness).
  - **Quantitative**:
    - Interval - does not have a meaningful zero, but has a meaningful difference;
    - Ratio - does have a **true zero**.

#### Visualizing categorical variables

- Frequency distribution tables - nominal and relative frequency;

- Bar charts;

- Pie charts;

- Pareto diagrams (bar + cumulative) - ordered nominal frequency represented with a bar chart on one axis and cumulative relative frequency represented with a curve on the other axis.

#### Visualizing numerical variables

- Frequency distribution table does not serve its purpose with numerical data. It can be used when data is grouped into intervals (5 - 20 in most cases). Can be done in pandas with ```pd.cut(x, bins)```.

- Histogram - displays the shape and spread of continuous sample data. Each bar groups numbers into ranges. Might be useful to show relative frequencies instead of absolute ones. Some of the histograms might be created with the unequal intervals (age groups).

#### Cross tables and scatter plots

- **Cross Tables** (contingency tables) - represent relation between two variables. Can be then translated into a **side-by-side bar chart**.

- **Scatter Plots** used when representing two numerical sets of data.

### Measures of central tendency, asymmetry, and variability

NOTE: Calculating statistics for a sample most of a time is based on *(N-1)* denominator. This is done in order to increase a magnitude of the statistics representing data dispersion/variance.

#### Mean, median, mode

- Mean - watch out for outliers! If the mean and median are very different it might mean that within a dataset there are outliers that impact average value.

- If there are multiple modes then mode should not be provided as it most like does not bear any meaning.

#### Measuring skewness (measurin asymmetry)

- **Skewness** - indicates whether the data is concentrated on one side and on which side the ourliers are.

- **Positive skew** (right skew) - when mean > median; right outliers.

- **Zero skew** (symmetrical data) - when mean = media = mode; no outliers.

- **Negative skew** (left skew) - when mean < median; left outliers.

#### Measuring how data is spread out: calculating variance

- **Variance** measures the dispersion of a set of data points around their mean. Within the formula for variance squaring the difference has two main purposes:

  - Difference needs to be a non-negative value;
  - Amplifies the effect of large differences.

- In the sample variance formula denominator is denoted as *n - 1* because it will increase variance value. Since we are operating on the sample there is a dose of uncertainty the we want to be reflected in the output.

- **Standard deviation** - informs how much on average given variable deviates from the mean value.

- **Coefficient of variation (CV)** - standard deviation **relative to the mean**. It is useful when we want to compare deviations from two different datasets.

#### Calculating and understanding covariance

- **Covariance** - Covariance shows the tendency in the linear relationship between the variables, but does not measure strength/magnitude of the relationship but:

  - *cov(X,Y) < 0* - negative relationship;
  - *cov(X,Y) = 0* - no relationship;
  - *cov(X,Y) > 0* - positive relationship.

- **Correlation coefficient** (covariance divided by the product of two standard deviations) - value in range *[-1, 1]*. A normalised measurement of the covariance. It is a measure of a linear correlation between two sets of data.

### Distributions

- **Distribution** is a function that shows possible values for a variable and how they occur. Types of distributions:

  **Discrete probability distributions**:
  - **Normal**
  - **Student's T**
  - **Exponential**
  **Continous probability distribution**:
  - **Uniform**
  - **Binomial**

#### Normal Distribution

- **Gaussian distribution** - symmetrical (no skew), *mean = median = mode*. Same standard deviation, but different mean (controlling for std) will move the curve on the x axis without changing curve's shape. Same mean, but different standard deviation (controlling for the mean) will re-shape curve - the lower std the higher the curve will be and thinner the tails.

- **Standard normal distribution** - *mean = 0* and *std = 1* (*N~(0, 1)*). Normal distribution can be transformed into its standardized form by calculating z-score for each variable (check z-score normalization in machine learning notes).

#### The Central Limit Theorem

- The **central limit theorem** states that if you have a population with mean *μ* and standard deviation *σ* and take sufficiently large **random samples from the population with replacement**, then **the distribution of the sample means will be approximately normally distributed**. This will hold true regardless of whether the source population is normal or skewed, provided the sample size is sufficiently large (usually n > 30). **If the population is normal, then the theorem holds true even for samples smaller than 30.** In fact, this also holds true even if the population is binomial, provided that *min(np, n(1-p))> 5*, where *n* is the sample size and *p* is the probability of success in the population. This means that we can use the normal probability model to quantify uncertainty when making inferences about a population mean based on the sample mean. For random samples taken from the population we can compute mean of the sample means and the variance of the sample means:
$$N\sim(\mu,\frac{\sigma^2}{n})$$

- **Practical implications**: when doing an expirement it is not always known what distribution our data comes from, but knowing that sample means are normally distributed we can use mean's normal distribution to make **confidence intervals**, **t-tests**, **ANOVA**, and almost any other statistical test that uses the sample mean. This cannot be used only for data with Cauchy distribution which has undefined mean.

- **Standard Error** is a standard deviation of the distribution formed by the sample means. Standard error decreases when sample size increases (better approximation with larger samples).
$$\frac{\sigma}{\sqrt{n}}$$

- Based on CLT if you work with sample that is large enough I can assume the normality of sample means.

#### Student's T Distribution

- **t-distribution** is continous probability distribution that arise when estimating the mean of a **normally-distributed population** in situations where the **sample size is small** and the **population's standard deviation is unknown**. It has fatter tails than normal distribution due to higher uncertainty. The more **deegree of freedoms** (larger sample) the closer it is to a normal distribution. It is an approximation of the normal distribution.

- **t-statistic** ( *(sample mean - population mean) / standard error* ):
$$t_{n-1,\ \alpha} = \frac{\bar{x}-\mu}{\frac{s}{\sqrt{n}}}$$

### Estimarors and Estimates

- **Estimator** of the population parameter is an approximation depending solely on the sample information. It is a statistic that estimates some fact about the population. You can also think of an estimator as the rule that creates an estimate. Specific value given by the estimator is called an **estimand**. We distinct 2 main types of estimates:

  - **point estimates** (located in a middle of confidence interval) - occur as a result of point estimation applied to a set of sample data (f.e. standard deviation);
  - **interval estimates** (provide more information) - range of values for a statistic (f.e. confidence interval).

- Additionally there are several different properties of estimators:

  - **biased** - a statistic that is either an overestimate or an underestimate;
  - **efficient** - a statistic with small variances (the one with the smallest possible variance is also called the “best”). *Inefficient* estimators can give you good results as well, but they usually requires much larger samples;
  - **invariant** - statistics that are not easily changed by transformations, like simple data shifts;
  - **shrinkage** - a raw estimate that’s improved by combining it with other information;
  - **sufficient** - a statistic that estimates the population parameter as well as if you knew all of the data in all possible samples;
  - **unbiased** - an accurate statistic that neither underestimates nor overestimates.

- **Statistical inference** is the process of using data analysis to infer properties of an underlying distribution of probability. Inferential statistical analysis infers properties of a population, for example by testing hypotheses and deriving estimates. It is assumed that the observed data set is sampled from a larger population.

#### Confidence Intervals - Single Population

- **Confidence interval** is the range within which you expect the population parameter to be.

- Calculation of the confidence interval **depends on whether population variance is known or not**:

  - **confidence interval with known variance** (*z* is a critical value for given confidence level $1-\alpha$)
  General formula:
  $$[point\ estimate - reliability\ factor * standard\ error, point\ estimate + reliability\ factor * standard\ error]$$
  Formula example for the average:
  $$[\bar{x} - z_{\alpha/2}\frac{\sigma}{\sqrt{n}}, \bar{x} + z_{\alpha/2}\frac{\sigma}{\sqrt{n}}]$$
  *Interpretation*: with a [confidence_level] average value is going to lie in the estimated interval.

  - **confidence interval with unknown variance**:
  Compared to the results that would be obtained with a statistic with a known variance confidence interval with unknown variance yields wider interval that reflects higher level of uncertainty.
  Formula example for the average:
  $$[\bar{x} - t_{n-1,\alpha/2}\frac{s}{\sqrt{n}}, \bar{x} + t_{n-1,\alpha/2}\frac{s}{\sqrt{n}}]$$

- Confidence interval can be calculated with the use of ```scipy.stats``` module:

```python
from scipy import stats
dataset = [78000, 90000, 75000, 117000, 105000, 96000, 89500, 102300, 80000]

# For normal distribution
stats.norm.interval(0.99, loc=np.mean(dataset), scale=pd.DataFrame(dataset).sem())

# For t distribution
stats.t.interval(0.99, df=8, loc=np.mean(dataset), scale=pd.DataFrame(dataset).sem())
```

#### Confidence Intervals - Two Populations

- Sampels taken from the two populations can be:

  - dependent,
  - independent which distinguishes 3 cases:
    - population variance is known,
    - population variance is unknown but assumed to be equal,
    - population variance is unknown but assumed to be different.

##### Dependent Samples

- Most common example is for developing a medicine where given parameter is tested before and after using certain drug.

- In most of the cases difference between values from dependent samples is being calculated and then required statistic is calculated.

- Confidence interval for difference of two means from dependent samples (for large samples z-statistic should be used):
$$\bar{d}\pm t_{n-1,\alpha/2}\frac{s_d}{\sqrt{n}}$$

##### Independent Samples

###### Known Population Variance

- Used for truly independent samples (f.i. score of different students from different departments, different teachers, different exams and classes).

- First, sample statistics (mean, std) needs to be calculated for each independent sample and then further calculations for differences should carried out.

- Considerations:

  - the populations are normally distributed,
  - the population variances are known
  - the sample sizes are different.

- Variance of the difference is given by below equation because **dispersion is additive**:  $$\sigma^2_{diff} = \frac{\sigma^2_{x_1}}{n_{x_1}} + \frac{\sigma^2_{x_2}}{n_{x_2}}$$

- Confidence interval: $$(\bar{x_1} - \bar{x_2})\pm z_{\alpha/2}\sqrt{\frac{\sigma^2_{x_1}}{n_{x_1}}+\frac{\sigma^2_{x_2}}{n_{x_2}}}$$

###### Unknown Population Variance (assumed to be equal)

- Can be used when analysing prices of the same product on different markets since it makes sense that variance of given product should be equal on both markets.

- **Pooled variance** - used to estimate variance for several different populations when the mean of each population may be different, but one may assume that the variance of each population is the same.
$$s^2_p = \frac{(n_{x_1}-1)s^2_{x_1}+(n_{x_2}-1)s^2_{x_2}}{n_{x_1}+n_{x_2}-2}$$

- Confidence interval:
$$(\bar{x_1}-\bar{x_2})\pm t_{n_{x_1}+n_{x_2}-2,\ \alpha/2}\sqrt{\frac{s^2_p}{n_{x_1}}+\frac{s^2_p}{n_{x_2}}}$$

###### Unknown Population Variance (assumed to be different)

- Can be used when analysing prices of different products so that price variance can be assummed to be different.

- Confidence interval:
$$(\bar{x_1}-\bar{x_2})\pm t_{v,\ \alpha/2}\sqrt{\frac{s^2_{x_1}}{n_{x_1}}+\frac{s^2_{x_2}}{n_{x_2}}}$$

- degrees of freedom (*v*) is given by [this formula](https://opentextbc.ca/introstatopenstax/wp-content/ql-cache/quicklatex.com-6384ba6785cbf87164c59664b773c487_l3.svg).

#### Margin of Error

- **Margin of error** is a scaled quantile (f.e. *t-* or *z-statistics*) by standard error. It depends on whether population variance is known or not. Since margin of error determines the interval for confidence interval they can be summarized as:
$$\bar{x}\pm ME$$

- Following influence the margin of error (and therefore a confidence interval size):

  - type of a statistic (*z* or *t*),
  - confidence level (higher confidence level -> wider CI),
  - standard deviation (higher standard deviation -> wider CI),
  - sample size (larger sample size -> narrower CI).
