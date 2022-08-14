# Python for Machine Learning

## Table of Contents

- [Python for Machine Learning](#python-for-machine-learning)
  - [Table of Contents](#table-of-contents)
  - [Sources](#sources)
  - [NumPy](#numpy)
    - [NumPy Arrays](#numpy-arrays)
    - [NumPy Indexing and Selection](#numpy-indexing-and-selection)
  - [Pandas](#pandas)
    - [Options](#options)
    - [Series](#series)
    - [DataFrames](#dataframes)
      - [apply](#apply)
      - [pipe](#pipe)
      - [Missing Data](#missing-data)
      - [GroupBy Operations (+ Multi Level Indexing)](#groupby-operations--multi-level-indexing)
      - [Combining DataFrames](#combining-dataframes)
      - [Text Methods in Pandas](#text-methods-in-pandas)
      - [Time Methods for Date and Time Date](#time-methods-for-date-and-time-date)
      - [Pandas Input and Output](#pandas-input-and-output)
      - [Pandas Pivot Tables](#pandas-pivot-tables)
    - [Useful Methods](#useful-methods)
  - [Idiomatic Pandas](#idiomatic-pandas)
    - [Modern Pandas](#modern-pandas)
    - [Method Chaining](#method-chaining)
      - [Pipelines](#pipelines)
    - [Indexes](#indexes)
    - [Fast Pandas](#fast-pandas)
      - [Improving Code Speed](#improving-code-speed)
    - [Tidy Data](#tidy-data)
  - [Data Visualization](#data-visualization)
    - [Matplotlib](#matplotlib)
      - [Functional matplotlib](#functional-matplotlib)
      - [OOP matplotlb](#oop-matplotlb)
        - [Subplots](#subplots)
        - [Styling](#styling)
    - [Plotting in pandas](#plotting-in-pandas)
    - [Seaborn](#seaborn)
      - [Scatterplot](#scatterplot)
      - [Distribution Plots](#distribution-plots)
      - [Categorical Plots](#categorical-plots)
      - [Comparison Plots](#comparison-plots)
      - [Grid Plots](#grid-plots)
      - [Matrix Plots](#matrix-plots)

## Sources

- [2021 Python for Machine Learning & Data Science Masterclass](https://www.udemy.com/course/python-for-machine-learning-data-science-masterclass/)
- [Kaggle Learning](https://www.kaggle.com/learn)
- [Calm Code](https://calmcode.io/)

## NumPy

### NumPy Arrays

- In order to create an evenly spaced set of numbers in the defined number range (inclusive) ```np.linspace()``` can be used. It is especially useful when we want to combine it with ```np.quantile``` and ```pd.cut``` so that binned data is not of an equal width based on the range of values, but based on the actual data distribution:

```python
# Basic linspace
np.linspace(0, 10, 3) # Output: array([0, 5, 10])

# Linspace combined with np.quantile and pd.cut
breaks = np.quantile(dtf[num], np.linspace(0, 1, 11))
tmp = dtf.groupby([dtf['Y'], pd.cut(dtf['Age'], breaks, duplicates='drop')])
```

- To create identity matrix ```np.eye()``` can be used.

- ```np.random.rand``` uses uniform distribution (all of the numbers in the range of [0, 1) have same probability of being sampled); ```np.random.randint``` can be used to uniformly sample defined range (output will be integers only). ```np.random.randn``` uses standard normal distribution:

  - mean = 0, variance = 1;
  - includes negative values;
  - numbers closer to 0 have higher probability of being selected).

- ```nparray.min()```, ```nparray.max()``` return minimum and maximum values from the array, whereas ```nparray.argmin()```, ```nparray.argmax()``` return the indices of those values (same as ```idxmax()``` and ```idxmin()```)

- ```np.count_nonzero()``` can be used to count number of ```True``` values in the array.

```python
x = np.random.choice([False, True], size=100000)
np.count_nonzero(x[:-1] < x[1:])
```

- ```np.ufunc.accumulate()``` accumulates the results of applying the operator to all elements.

```python
# Calculating maximum profit from the series of stock prices
prices = (20, 23, 21, 35, 14, 17, 20, 21, 15)

# Using vanilla Python
def profit(prices):
    max_px = 0
    min_px = prices[0]
    for px in prices[1:]:
        min_px = min(min_px, px)
        max_px = max(px - min_px, max_px)
    return max_px


# Using NumPy
np.max(prices - np.minimum.accumulate(prices))
```

### NumPy Indexing and Selection

- ```copy()``` can be used for both NumPy arrays and pandas Series and DataFrames.

- In mutlidimmensional arrays slicing only on lower levels can be done without adding slices from the rest of the levels: ```np_2d_array[5:3]```. Slicing of the lower levels must be included and sequential. For example, ```np.add.accumulate()``` is equivalent to ```np.cumsum()```.

- Slicing a NumPy array returns **view** of the source ```numpy.array``` whereas integer or Boolean indexing returns **copy**:

```python
# `arr` is the original array:
arr = np.array([1, 2, 4, 8, 16, 32])

# `a` and `b` are views created through slicing:
a = arr[1:3]
b = arr[1:4:2]

# `c` and `d` are copies created through integer and Boolean indexing:
c = arr[[1, 3]]
d = arr[[False, True, False, True, False, False]]
```

- Broadcasting in NumPy follows general rule that is based on comparing arrays' shapes element-wise. It starts with the trailing dimensions and works its way forward. Two dimensions are compatible when:

  1. The arrays all have exactly the same shape.
  2. The arrays all have the same number of dimensions, and the length of each dimension is either a common length or 1.
  3. The arrays that have too few dimensions can have their NumPy shapes prepended with a dimension of length 1 to satisfy property #2.

```python
sample = np.random.normal(loc=[2., 20.], scale=[1., 3.5],
                          size=(3, 2))
sample_min = sample.min(axis=1)[:, None]  # expands dimensionality of an array (None is an alias for np.newaxis) - shape from (3,) -> (3,1)

sample - sample_min  # shape (3,2) vs. shape (3,1)
```

## Pandas

### Options

- You can change default panda's configuration by using ```pd.set_options('parameter', value)```:

```python
pd.set_option('display.max.columns', None)
pd.set_option('display.precision', 2)
```

### Series

- When adding Series to each other ```pd.series.add()``` with ```fillna``` argument should be used instead of '+' if there are missing labels in either of the Series.

- Series and DataFrames support ```.keys()``` method (0 axis for Series and 1 axis for DataFrame) and therefore accept *in* operator ```'Column_name/Index_name' in df/s```.

### DataFrames

- Columns are features; rows are instances of data.

- ```df.info()``` in order to get metadata about a DataFrame.

- ```pd.read_``` to read different type of files as DataFrame.

- ```df.describe()``` to get general data on numerical columns within DataFrame. ```df.describe().transpose()``` makes it more readable.

- ```df.describe()``` can be be passed *include* argument together with the list of dtypes that should be included in the function output; *all* string can be used if stats should be shown for all the columns:

- ```df.to_numpy()``` converts given DataFrame or Series to NumPy array and is recommended over ```df.values```.

```python
nba.describe(include=np.object)
nba.describe(include='all')
```

- ```np.around()```

- ```df.drop()``` ```axis=0``` for rows ```axis=1``` for columns. ```inplace=True``` for inplace drop of the items in the axis. It is better to just reassign DataFrame to a desirable variable. *inplace* will most likely be depreciated. Dropping for columns can also be done via *columns* keyword:

```python
df = df.drop(columns=columns_to_drop)
```

- Columns can also be dropped when reading a CSV file via *usecols* keyword - it will **retain** columns that are passed to the keyword or columns which names called on passed function will return ```True```:

```python
# List-like passed to the keyword
pd.read_csv(path, usecols=columns_to_use)

# Function called on each column name
hw_exam_grades = pd.read_csv(
    path,
    converters={"SID": str.lower},
    usecols=lambda x: "Submission" not in x,
)
```

- When reading a CSV file columns can also be renames using ```names``` keyword:

```python
pd.read_csv(file, names=['first_col_name', 'second_col_name'])
```

- When writing a DataFrame to a CSV or Excel file ```na_rep``` keyword argument can be used to define how missing data should be represented in the output file (default is an empty string):

```python
df.to_csv('new-data.csv', na_rep='(missing)')
```

- When reading a file to a DataFrame ```na_values``` argument can be passed to determine what values should be considered as a missing ones (apart from the default ones).

```python
pd.read_csv('new-data.csv', index_col=0, na_values='(missing)')
```

- When reading a CSV or Excel file to a DataFrame *dtypes* can be passed as ```dtypes``` argument in form of a dict:

```python
dtypes = {'POP': 'float32', 'AREA': 'float32', 'GDP': 'float32'}
df = pd.read_csv('data.csv', index_col=0, dtype=dtypes)
```

- When reading a CSV or Excel file to a DataFrame columns with dates can be automatically parsed if passed to ```parse_dates``` argument:

```python
df = pd.read_csv('data.csv', index_col=0, parse_dates=['IND_DAY'])
```

- When writing a DataFrame to a CSV file ```date_format``` argument can be passed to set-up output format for date columns:

```python
df.to_csv('formatted-data.csv', date_format='%B %d, %Y')
```

- If you have a file with one data column and want to get a Series object instead of a DataFrame, then you can pass ```squeeze=True``` to ```read_csv()```.

- When working with Big Data following optimization methods can be used:

  - compression,
  - choosing only the required columns,
  - omissions of the not needed rows,
  - forcing the use of the less precise data types,
  - splitting the data into chunks.

- Data can be split into the chunks in order to handle large datasets. Chunks can then be iterated over to obtain smaller DataFrames:

```python
data_chunk = pd.read_csv('data.csv', index_col=0, chunksize=8)

for df_chunk in pd.read_csv('data.csv', index_col=0, chunksize=8):
    print(df_chunk, end='\n\n')
    print('memory:', df_chunk.memory_usage().sum(), 'bytes', end='\n\n\n')

# Alternatively you can use pd.read_csv(iterator=True) to return an iterator object
```

- Writing to and reading from SQL database requires correct setup:

```python
from sqlalchemy import create_engine
engine = create_engine('sqlite:///data.db', echo=False)

df.to_sql('data.db', con=engine, index_label='ID')
df = pd.read_sql('data.db', con=engine, index_col='ID')
```

- Written files can be automatically compressed:

```python
df.to_csv('data.csv.zip')
```

- Axes are 0 for rows and 1 for columns because that's how those will be defined in the *shape* tuple - ```df.shape``` will output ```(num_of_rows, num_of_columns)```.

- To append a new row to a DataFrame using ```df.append()``` we need to provide a set of data (Series, DataFrame, dict, dict-like object, or list of these) that needs to have the same number of columns (shape) as a DataFrame to which we append rows (in case of 2d arrays).

- It is possible to re-assign index to given axis with ```df.set_axis()```:

```python
df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
df.set_axis(['I', 'II'], axis=1)
```

- Conditional filtering on the same columns with multiple ```or``` conditions (equivalent of ```in``` operator in Python) can be coded like this: ```df['col'].isin.(list_of_options)```

- In order to filter the items from given axis based on list of items/like in label/RegEx pattern ```df.filter()``` can be used:

```python
# Filtering column names that meet certain RegEx pattern
homework_scores = final_data.filter(regex=r"^Homework \d\d?$", axis=1)
```

- DataFrames sorting can be done with either ```sort_values()``` or ```sort_index()```. By default *quicksort* is being used as a sorting algorithm - this sorting is **unstable sort** which means that records with equal keys might not appear in the same order as they appear in a dataset. Mergesort can be used in case when stable sorting is required: ```sort_values(by='col_name', kind='mergesort')```. *kind* argument is ignored when sorting is based on more than one columns or label.

- Sorting with multiple columns/hierarchical index can be combined with mutliple sort order by passing equally sized boolean array to *ascending* argument:

```python
df.sort_values(
    by=["make", "model", "city08"],
    ascending=[True, True, False]
)
```

- Both DataFrame sorting functions accept ```na_position``` parameter - either *first* or *last* whereas *last* is the default value. This argument makes missing values or indices appear at the end or at the beginning of the data set.

#### apply

- When ```apply()``` is called on the Series in does not take *axis* keyword, but when it is called on the DataFrame it needs to be run with ```axis=1``` in order to apply given function on each row.

- When ```apply()``` in called on the DataFrame and multiple columns are passed *lambda* function needs to be used regardless whether it will call another function (it will be then responsible for passing the function arguments - mostly DataFrame - to the desired function) or it will be a standalone function to be applied.

- ```Series.map()``` map values of Series according to the provided input (can be a dict, Series or a function):

```python
# Using dict for mapping
s = pd.Series(['cat', 'dog', np.nan, 'rabbit'])
s.map({'cat': 'kitten', 'dog': 'puppy'})

# Using function for mapping
grades = {
    90: "A",
    80: "B",
    70: "C",
    60: "D",
    0: "F",
}

def grade_mapping(value):
    for key, letter in grades.items():
        if value >= key:
            return letter

final_data["Ceiling Score"].map(grade_mapping)
```

- ```df.applymap(foo)``` can be used to call certain function on **each DataFrame's** element. This function may have significant runtime for large datasets since it maps a Python callable to each individual element.

- Instead of calling ```apply()``` or ```map()``` on multiple columns or ```applymap()``` on a DataFrame it is more computationally efficient to call ```np.vectorize(function_to_call)(df['col1'], df['col2'])```. ```np.vectorize()``` vectorizes an operation using NumPY which uses C under the hood and calls given function on each element.

- The purpose of ```np.vectorize``` is to transform functions which are not numpy-aware into functions that can operate on (and return) numpy arrays.

#### pipe

- Use ```df.pipe()``` when chaining together functions that expect Series, DataFrames or GroupBy objects:

```python
from functools import wraps
import datetime as dt
import pandas as pd

def log_step(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        #decorator definition

@log_step
def start_pipeline(dataf):
    return dataf.copy()

@log_step
def set_dtypes(dataf):
    pass

@log_step
def remove_outliers(dataf, min_row_country=32):
    pass

clean_df = (df
  .pipe(start_pipeline)
  .pipe(set_dtypes)
  .pipe(remove_outliers, min_row_country=20))
```

#### Missing Data

- ```np.nan == np.nan``` will retun ```False``` which makes sense if you think about it as a missing value that we do not really know what it is. When we want to check whether something is a *NaN* value we should use ```variable is np.nan```.

- ```df.isnull()``` returns boolean array that indicates which values are missing (same as ```df.isna()```). ```df.notnull()``` does the same but indicates non-missing values (same as ```df.notna()```).

- ```df.dropna``` drops NaN values on the desired axis whereas ```df.fillna``` fills in NaN values with desired values on a desired axis and with a desired fill method.

- ```df.isnull().sum()``` since summing on booleans is based on *False = 0* and *True = 1* this summation returns number of missing values for each data columns.

#### GroupBy Operations (+ Multi Level Indexing)

- When we want to grab every row from the first level of a MultiIndex we just have to use ```df.loc['level_0']```. When want to get a specifc value we need to provide a tuple ```df.loc[('level_0', 'level_1')]```.

- ```df.xs()``` allows to select data at a particular level of a MultiIndex where ```key``` argument takes label contained in the index or MultiIndex and ```level``` argument indicates which levels are used. Allows for grouping based on the inner levels of the MultiIndex across all of the outer levels.

- It is often easier to filter the data before applying grouping methods if desired output would be hard to obtain with those methods.

- ```df.agg()``` can be called when we want to perform an aggregation using one or more operations over the specified axis. When list of function strings is provided those are called on entire DataFrame. Dictionary can be passed that will specify what functions should be called on which columns:

```python
df = pd.read_csv('https://calmcode.io/datasets/bigmac.csv')
df2 = (df
  .assign(date=lambda d: pd.to_datetime(d['date']))
  .sort_values(['currency_code', 'date'])
  .groupby('currency_code')
  .agg(n=('date', 'count')))  # tuples of '(column, aggfunc) that are a name 'n'
```

- ```pd.Grouper()``` allows to specify a groupby instruction for an object. Can be used to resample datetime-like columns to group by different frequency:

```python
# Changes frequency to weekly where Monday is the first day of the week
df.groupby(pd.Grouper(key='date_col', freq='W-MON))
```

- ```DataFrameGroupBy``` object can be iterated similar to a dict where key will be an index label based on which DataFrame has been groupedby and value will be an actual DataFrame where key matched grouping criteria:

```python
# 'section' handles indices (1, 2, 3) and 'table' handles respective DataFrames
for section, table in final_data.groupby("Section"):
    section_file = DATA_FOLDER / f"Section {section} Grades.csv"
    num_students = table.shape[0]
    print(
        f"In Section {section} there are {num_students} students saved to "
        f"file {section_file}."
    )
    table.sort_values(by=["Last Name", "First Name"]).to_csv(section_file)
```

- Instead of dropping columns from a DataFrame to get a single count column ```size()``` aggregating function can be used.

#### Combining DataFrames

- Concatenating of DataFrames is performed with ```pd.concat()``` method that joins a list of DataFrames based on their indices (```axis=0```) or columns (```axis=1```). The the output can either be an union (```join='outer'```) or an intersection (```join='inner'```) of the labels or indices. Missing values will be indicated by NaN.

- ```df.join()``` is an efficient way to join multiple DataFrame objects by index.

#### Text Methods in Pandas

- In order to split delimited values into multiple columns: ```df['col1'].str.split(',', expand=True)```

- In order to extract data from a Series matching given pattern use ```pd.Series.str.extract()```:

```python
df['col'].str.extract(pattern, expand=False)  # expand=False ensures that output is a Series
```

#### Time Methods for Date and Time Date

- Date oriented alternative to ```np.arange()``` is ```pd.date_range()```.

- ```pd.to_datetime(Series)``` to convert strings to datetime objects. ```first=True``` to indicate European datetime formatting. ```format='custom_format'``` to indicate custom formatting.

- When reading a data with ```pd.read_[method]``` ```parse_dates=`[list_of_columns_indices_to_parse]`` argument can be provided so that columns with a date will automatically be set to appropriate pandas object.

- ```df.resample()``` is basically a ```df.groupby()``` for time-series data. It can be used to split given date format into other date interval.

- In order to access data-time objects attributes and methods *dt* should be used: ```df['col1'].dt.[method_or_attribute_of_choice]```.

#### Pandas Input and Output

- Saving DataFrame as an output in the external file is done via ```df.to_[output_format] method.

- When Excel that we want to read into DataFrame with pandas has multiple sheets we can either read in entire Excel file with ```wb = pd.ExcelFile()``` and then access sheet names with ```wb.sheet_names``` or we can read entire excel with ```pd.read_excel('path', shet_name=None)``` as a dictionary (keys are sheet names and values are actual DataFrames).

#### Pandas Pivot Tables

- Pivots could be used more for the purpose of increasing readability. For the actual data manipulation most of the time ```df.groupby()``` method should be sufficient to obtain the same results unless we want to spread categorical data into columns instead of having it in the index.

- ```df.pivot()``` reshapes data (produces a “pivot” table) based on column values. Uses unique values from specified index / columns to form axes of the resulting DataFrame. This function does not support data aggregation, multiple values will result in a MultiIndex in the columns.

- ```pd.pivot_table()``` creates a spreadsheet-style pivot table as a DataFrame. The levels in the pivot table will be stored in MultiIndex objects (hierarchical indexes) on the index and columns of the result DataFrame.

- ```pd.melt()``` unpivots a DataFrame from wide to long format. It can be used for example when there are 2 or more columns for data that can be included in a single column (f.e. home and away teams that play against each other can be melted into a single column):

```python
tidy = pd.melt(games.reset_index(),
               id_vars=['game_id', 'date'], value_vars=['away_team', 'home_team'],
               value_name='team')
```

### Useful Methods

- In order to get a count value for categorical columns ```df['col1'].value_counts()``` can be used.

- ```unique``` returns an array of unique values in the list of values (Series etc.).  ```nunique``` returns a number of unique values.

- When single value within the column needs to be replaced use ```replace()``` function. When multiple values require replacing use ```map()``` function instead that takes dictionary as an input.

- When we want to simply count number of unique values in a Series we can use ```Series.value_counts()``` which counts and sorts (descending by default) unique values.

- In order to Series or DataFrame by index use ```sort_index()```.

- It is possible to extract single values with the use of ```.loc[]``` and ```.iloc[]```, but it is more desired to use ```.at[]``` or ```.iat[]``` in such cases.

- To avoid *SettingWithCopyWarning* in pandas, that indicates that assignment is done on a DataFrame copy, following should be done:

  - **Avoid chained assignments** that combine two or more indexing operations like ```df["z"][mask] = 0``` and ```df.loc[mask]["z"] = 0``` - masking in pandas and NumPy returns a copy of the object and therefore any direct assignments will be lost. To retain this state change a copy should be first assigned to a variable. (**to be confirmed**)

  - Apply single assignments with just one indexing operation like ```df.loc[mask, "z"] = 0```. This might (or might not) involve the use of accessors, but they are certainly very useful and are often preferable.

- ```df.iteritems()``` and ```df.iterrows()``` can be used to iterate over columns and rows; iterator returns a tuple with column/row label and Series of data for given axis. ```df.itertuples()``` iterates over rows and yields a named tuple with the index and data.

- In order to check whether given Series contains unique values (f.i. to check whether it is suitable for becoming an Index) *is_unique* attribute na be checked:

```python
df['Identifier'].is_unique  # True or False for the output
```

- In order to obtain list out of Series use ```df.to_list()```.

- Converting Series from one type to another can be done with ```astype()``` casting, but also with ```pd.to_numeric(pd.Series)``` for conversion to numeric. ```astype()``` accepts dictionary that maps columns to specific data types.

- In order to use vectorized IF-like function use ```np.where(condition, then, else)```. If multiple conditions needs to be used it is more readable than multiple reassigments with ```[]``` or ```.loc```:

```python
# General form:
np.where(condition1, x1, 
  np.where(condition2, x2, 
      np.where(condition3, x3, ...)))

pub = df['Place of Publication']
london = pub.str.contains('London')
oxford = pub.str.contains('Oxford')
df['Place of Publication'] = np.where(london, 'London',
                                      np.where(oxford, 'Oxford',
                                               pub.str.replace('-', ' ')))
```

- Broadcasting of operation for DataFrames works similarly to the one for the Series, but takes into consideration indices from both axes. It is therefore possible to perform given operation on both DataFrames without obtaining *NaN* values when both DataFrames have the same index labels for both rows and columns:

```python
A = pd.DataFrame(np.random.randint(0, 10, (3,3)), columns=['A','B','C'])
B = pd.DataFrame(np.random.randint(0, 10, (3,3)), columns=['1','2','3'])

B = B.set_axis(A.columns, axis=1)  # setting the same column names for B
A/B
```

- General rules for broadcasting in pandas:

  - if operation is called on Series index labels are being matched;
  - if operation is called on DataFrames **both** index and column labels are being matched;
  - if operation is called on DataFrame and Series then Series' index is being matched against DataFrame's columns and Series is broadcasted on '0' axis.

```python
quiz_scores = final_data.filter(regex=r"^Quiz \d$", axis=1) # 5 columns
quiz_max_points = pd.Series(
    {"Quiz 1": 11, "Quiz 2": 15, "Quiz 3": 17, "Quiz 4": 14, "Quiz 5": 12}
)
# Broadcasting happens here
average_quiz_scores = (quiz_scores / quiz_max_points).sum(axis=1) 
final_data["Average Quizzes"] = average_quiz_scores / quiz_scores.shape[1]
```

- ```ser.factorize(sort=True)``` encodes the object as an enumerated type or categorical variable. This is useful for obtaining a numeric representation of an array when all that matters is identifying disctinct values - f.e. when computing correlation matrix for categorical features. Available also as a top-level function ```pd.factorize()```.

- ```df.diff()``` - calculates the difference of a Dataframe element compared with another element in the Dataframe (default is element in previous row).

- In order to conver Series into a DataFrame object use ```ser.to_frame()```.

## Idiomatic Pandas

### Modern Pandas

- Use ```loc``` and ```iloc``` for explicitly accessing the items by their labels or positions.

- Avoid chained assignments and use ```loc```, ```iloc``` or ```assign``` instead.

- Multidimensional indexing:
  
  - it is easy for 0-level indexing (0 level being the most outer one): ```df.loc[['lvl_0_index1', 'lvl_0_index2'], ['col1', 'col2']]```;
  - for querying consecutive levels (f.i. 0 and 1) it is also easy since multilevel indexing just needs to be wrapped with a tuple: ```df.loc[(['lvl_0_index1', 'lvl_0_index2'], [lvl_1_index1, lvl_1_index2]), ['col1', 'col2']]```;
  - taking all of the index labels from the outer levels and querying part of the inner levels used to be hard, but currently it is just: ```df.loc[pd.IndexSlice[:, ['lvl_1_index_1', 'lvl_1_index_2']], ['col1', 'col2']]```.

### Method Chaining

- ```inplace``` enabled methods should not be used since they do not allow for method chaining and they are not guaranteed to be faster since most of the time they rely on a copy of a dataframe and reassignment.

#### Pipelines

- **Pipelines** are a simple way to keep data preprocessing and modeling code organized. Specifically, a pipeline bundles preprocessing and modeling steps so one can use the whole bundle as if it were a single step.

```python
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder

categorical_cols = [cname for cname in X_train_full.columns if X_train_full[cname].nunique() < 10 and 
                        X_train_full[cname].dtype == "object"]
numerical_cols = [cname for cname in X_train_full.columns if X_train_full[cname].dtype in ['int64', 'float64']]

# Preprocessing for numerical data
numerical_transformer = SimpleImputer(strategy='constant')

# Preprocessing for categorical data
categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
  ])

# Bundle preprocessing for numerical and categorical data
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numerical_transformer, numerical_cols),
        ('cat', categorical_transformer, categorical_cols)
    ])

from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor(n_estimators=100, random_state=0)

from sklearn.metrics import mean_absolute_error
# Bundle preprocessing and modeling code in a pipeline
my_pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                              ('model', model)
                             ])

# Preprocessing of training data, fit model 
my_pipeline.fit(X_train, y_train)

# Preprocessing of validation data, get predictions
preds = my_pipeline.predict(X_valid)
```

- Since pipelining makes debugging harder functions can be wrapped with a logging function using decorator:

```python
from functools import wraps
import logging

def log_shape(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logging.info("%s,%s" % (func.__name__, result.shape))
        return result
    return wrapper

def log_dtypes(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logging.info("%s,%s" % (func.__name__, result.dtypes))
        return result
    return wrapper
```

### Indexes

- ```Index```es are immutable multiset-like (they allow duplicates in index) objects that allow for set-like operations: & - intersection, | - union, ^ - symmetrics difference.

- Appropriately defined ```Index``` allows for easy merging with ```pd.concat``` which also allows for defining the ```axis``` of a concatation, and even a behaviour of merging with ```join``` parameter.

### Fast Pandas

- DataFrame appends are expensive relative to a list append so when loading input from multiple different sources (f.e. multiple csv files) it is better to make many smaller DataFrames and concatenate them at the end. This is because, depending on the values, pandas might have to recast the data to a different type. And indexes are immutable, so each time you append pandas has to create an entirely new one.

#### Improving Code Speed

1. Use benchmarks (timeit, vprof, snakeviz, line_profiles) on the code to make sure that optimisation is actually required.

2. Make sure you use proper algorithm and you make use of built-in pandas functions.

3. Vectorize function so it operates directly on the NumPy array. **You rarely want to use ```DataFrame.apply```** and almost never should use it with ```axis=1```. **It is better to write functions that take arrays, and pass those in directly**.

- Pandas ```GroupBy``` objects intercept calls for common functions like mean, sum, etc. and substitutes them with optimized Cython versions;
- Similarly, unwrapped ```.transform(np.mean)``` is fast.
- ```Groupby.apply``` is always going to be around, beacuse it offers maximum flexibility. If you need to fit a model on each group and create additional columns in the process, it can handle that. It just might not be the fastest (which may be OK sometimes).

- **Categoricals** are an efficient way of representing data (typically strings) that have a low cardinality. Since it's cheaper to store a code (value representation) than a category, we save on memory. Beyond saving memory, having codes and a fixed set of categories offers up a bunch of algorithmic optimizations that pandas and others can take advantage of.

### Tidy Data

- ```melt``` and ```pivot.

- ```stack``` and ```unstack```.

- ```pd.map``` can be used for merging Series (TODO: I should actually test how it is being done).

## Data Visualization

### Matplotlib

#### Functional matplotlib

- ```plt.plot(x,y)``` to create basic visualization.

- X-Y-axis names: ```plt.xlabel('X label name')``` and ```plt.ylabel('Y label name')```.

- ```plt.title('Visualization Title')``` to name a visualization.

- ```plt.xlim(min_val, max_val)``` and ```plt.ylim(min_val, max_val)```to set axes limits.

- To save plots: ```plt.savefig('name.jpg')```.

#### OOP matplotlb

- ```fig = plt.figure()``` blank canvas 432x288 pixels with 0 axes.

- ```plt.figure(figsize=(4,4), dpi=200)``` - *figsize* argument sets canvas width and heigth, and *dpi* sets quality of the image (default 100).

- ```axes = fig.add_axes([0, 0, 1, 1])``` - first 2 indicate position of a lower left corner of axes and next 2 indicate **width** and **height** of the axes - all parameters are **relative to a figure** in **ratios**. Axes are like layers for on the canvas.

- In order to set basic parameters to the axes ```set_``` methods should be used such as ```axes.set_xlim()```.

- Actual plotting on the set of axes: ```axes.plot(x, y)```.

- ```fig.savefig('new_chart.png', bbox_inches='tight')``` or ```plt.savefig()``` in order to get axes and labels.

##### Subplots

- In order to create multiple plots side by side ```plt.subplots(nrows=1, ncols=1)``` can be used since it returns a tuple of figure and axes objects. If there are more than one axis *axes* is a numpy array. Keyword arguments from ```plt.figure``` are available here as well (*figsize*, *dpi* etc.).

- To automatically fix spacing: ```plt.tight_layout()```.

- To manually fix spacing: ```fig.subplots_adjust(wspace=, hspace=)``` where key arguments are in the fraction of width and heigth of the axes.

- To get a title for the entire figure: ```fig.suptitle('Figure Level Title')```.

##### Styling

- Adding a legend is done via ```axes.plot()``` call with ```label='Just a label'``` argument and running ```axes.legend()``` at the end. ```loc``` argument determines where legend should be located.

- ```asex.plot()``` takes styling arguments:
  
  - *color* argument (either string or RGB HEX),
  
  - *lw*/*linewidth* argument (fraction of a line width),

  - *ls*/*linestyle* argument that defines line style (f.e. '--' for dashed line),

  - Custom line styling can be done with ```set_dashes([2,4,4,2])``` function that is called on the list element of axes plot (```lines = ax.plot(); lines[0]```) - passed list is basically a sequence of the solid point-spacing pairs where number corresponds to their length;

  - *marker* takes a string that indicate how each point will be represented graphically (f.i. ```marker='o'```);

  - *ms*/*markersize* argument takes a ratio of a default marker size;

  - Additional styling for markers: *markerfacecolor*, *markeredgewidth*, *markeredgecolor*.

### Plotting in pandas

- pandas provides basic wrapper for matplotlib with ```plot()``` functon that takes index labels for X-axis and values for Y-axis. Those can also be explicitly provided by ```x``` and ```y``` keywords.

- Type of a plot can be provided either via ```kind``` keyword argument or by another wrapper f.e. ```plot.bar()```.

### Seaborn

- To set a style for Seaborn plots use ```sns.set(style='dark')```.

- Matplotlib customization keyword arguments are available in Seabord plot calls (f.e. 'color', 'edgecolor', 'linewidth', etc,)

#### Scatterplot

- Basic scatterplot is being called via ```sns.scatterplot(x='col1', y='col2', data=df)```.

#### Distribution Plots

- Three main distribution plot types:
  - Rug Plot - tick for each value;
  - Histogram - data divided into bins and then presented in form of value counts within a bin or percentage distribution;
  - KDE (Kernel Density Estimation) Plot - fuction showing distribution of data constructed based on a given type of distribution (Gaussian/normal distribution most of the time) that is centered for all of the ticks in Rug Plot and then summed up.

- Basic Rug Plot ```sns.rugplot(x='col', data=df, height=0.5)```.

- Basic Histogram ```sns.displot(x='col', data=df, kde=True, rug=True, bw_adjust=1, shade=True, bins=50)``` (*bw* is a bandwitdh argument that determines how much noise plot will display) or ```sns.histplot(x='col', data=df)```.

- To show only KDE use ```sns.kdeplot(x='col', data=df, clip=[0, 100])```.

- In order to change the way of calculation for histogram plots from **count** to **density/probability/frequency** use ```stat='density'```.

- Distribution within categories:
  - Boxplot - interquartile range (Q1 - Q3) with whiskers equal to 1.5 times IQR and outliers: ```sns.boxplot(data=df, y='col1', x='col2', hue='col3');
  - Violinplot - basically a mirrored KDE joined with KDE: ```sns.violinplot(data=df, x='col1', y='col2', hue='col3', split=True, bw=0.5)``` (split will work only with 2 categories, inner='quartile'),
  - Swarmplot: ```sns.swarmplot(data=df, x='col1', y='col2', hue='col3', dodge=True)```,
  - Boxenplot (Letter-Value Plot): ```sns.boxenplot(data=df, x='col1', y='col2', hue='col3')```.

#### Categorical Plots

- ```sns.countplot(x='col', data=df)``` - takes in just a count of a categorical value in a dataset.

- ```sns.barplot(x='col', data=df, estimator=np.mean, ci='sd')``` - takes in any measure or estimator for the y-axis (f.e. mean, standard deviation); watch out for over-use of this plot type since it might be easier to display some measures in a table.

- Stacked barplot can be easily created with pandas ```plot``` wrapper:

```python
dtf_temp.groupby(['Y', 'bins']).size().unstack().apply(
    lambda x: x/sum(x)
).T.plot(kind='bar', stacked=True)
```

#### Comparison Plots

- Jointplot: ```sns.jointplot(x='col1', y='col2', data=df, kind='hex')```;

- Pairplot: ```sns.pairplot(x='col1', y='col2', data=df, hue='col3', diag_kind='hist', corner=True)``` (can be called just with *data* argument).

#### Grid Plots

- Creating multiple plots (grids) of given kind based on categorical value that can categorize each plot ```sns.catplot(data=df, x='col1', y='col2', kind='box', row='category_col1', col='category_col2')```.

- Creating a grid of combinations for all numerical columns in a DataFrame; basically a customization of a pairplot:

```python
g = sns.PairGrid(df, hue='col')
g = g.map_upper(sns.scatteplot)
g = g.lower(sns.kdeplot)
g = g.map_diag(sns.histplot)
g = g.add_legend()
```

#### Matrix Plots

- Visual equivalent of displaying a pivot table.

- Heat Map should include values in a same rates (f.e. percentage) in order to provide a readable plot: ```sns.heatmap(data=df, linewidth=0.5, annot=True, cmap='viridis')```.

- Cluster Map provides additional information via groupping together certain data in a hierarchy: ```sns.clustermap(col_cluster=False) # takes same arguments as heat map```.
