# pandas 

## 10 minutes to pandas¶

* This is a short introduction to pandas, geared mainly for new users. You can see more complex recipes in the Cookbook.

Customarily, we import as follows:

```py
import numpy as np

import pandas as pd

Object creation
```
See the Data Structure Intro section.

Creating a Series by passing a list of values, letting pandas create a default integer index:
```py
s = pd.Series([1, 3, 5, np.nan, 6, 8])

s
Out[4]: 
0    1.0
1    3.0
2    5.0
3    NaN
4    6.0
5    8.0
dtype: float64


## Checking the data

>`data.shape`

## Seeing the data

>`data.head(3)`

# The basic functions of pandas

## Logical operations

>`data[(data['column_1']=='french') & (data['year_born']==1990) & ~(data['city']=='London')]`

## Basic plotting

This feature is made possible thanks to the matplotlib package. As we said in the intro, it’s usable directly in pandas.
>`data['column_numerical'].plot()`

![plot](https://miro.medium.com/max/489/1*QyYuLym-PSTQk_3MYt81VA.png)

## Updating the data
>`data.loc[8, 'column_1'] = 'english'`

# Medium level functions

## Counting occurrences
>`data['column_1'].value_counts()`
![ex](https://miro.medium.com/max/378/1*7h20rGiaDoXUlWyfKhP1Vw.png)


## Operations on full rows, columns, or all data
The .map() operation applies a function to each element of a column.

>`data['column_1'].map(len).map(lambda x: x/100).plot()`

## tqdm, the one and only
When working with large datasets, pandas can take some time running .map(), .apply(), .applymap() operations. tqdm is a very useful package that helps predict when theses operations will finish executing (yes I lied, I said we would use only pandas).


>`from tqdm import tqdm_notebook`

>`tqdm_notebook().pandas()`

![ex](https://miro.medium.com/max/713/1*uerveZ-vqCl5sTyaeRLwSw.gif)

## Correlation and scatter matrices
>`data.corr()`

>`data.corr().applymap(lambda x: int(x*100)/100)`

![ex](https://miro.medium.com/max/875/1*VcCx97BF-kTMpzxbxPDqXg.png)


# Advanced operations in pandas

## The SQL join
>`data.merge(other_data, on=['column_1', 'column_2', 'column_3'])`




    



