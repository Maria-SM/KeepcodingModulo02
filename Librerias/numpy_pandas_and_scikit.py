
########### Python libraries for data analysis ########################

# Whenever we use a particular library, we first have to import the modules:
import numpy as np
import pandas as pd
import sklearn


# Notice how we can rename the modules we import. This is especially handy for longer names. You can also import pieces of a module:
from math import pi
print(pi)


# In this case, we imported a fixed value. We can also import functions, etc.

############ NumPy #####################3

# NumPy can be used for many different things, most notably for manipulating arrays.


# Create empty arrays/matrices
empty_array = np.zeros(5)

empty_matrix = np.zeros((5,2))

print('Empty array: \n',empty_array)
print('Empty matrix: \n',empty_matrix)

# Create matrices
mat = np.array([[1,2,3],[4,5,6]])
print('Matrix: \n',mat)
print('Transpose: \n',mat.T)
print('Item 2,2: ',mat[1,1])
print('Item 2,3: ',mat[1,2])
print('#rows and #columns: ',np.shape(mat))
print('Sum total matrix: ',np.sum(mat))
print('Sum row 1: ',np.sum(mat[0]))
print('Sum row 2: ',np.sum(mat[1]))
print('Sum column 3: ',np.sum(mat,axis=0)[2])


########## Pandas ####################

# pandas is great for reading and creating datasets, as well as performing basic operations on them.

# Creating a matrix with three rows of data
data = [['johannes',10],['giovanni',2],['john',3]]

# Creating and printing a pandas DataFrame object from the matrix
df = pd.DataFrame(data)
print(df)

# Adding columns to the DataFrame object
df.columns = ['names','years']
print(df)

# Taking out a single column and calculating its sum
# This also shows the type of the variable: a 64bit integer (array)
print(df['years'])
print('Sum of all values in column: ',df['years'].sum())

# Creating a larger matrix
data = [['johannes',10],['giovanni',2],['john',3],['giovanni',2],['john',3],['giovanni',2],['john',3],['giovanni',2],['john',3],['johannes',10]]

# Again, creating a DataFrame object, now with columns
df = pd.DataFrame(data, columns = ['names','years'])

# Print the 5 first (head) and 5 last (tail) observations
print(df.head())
print('\n')
print(df.tail())


# Print all unique values of the column names
print(df['names'].unique())

# Add a column names 'code' with all zeros
df['code'] = np.zeros(10)
print(df)


# You can also easily find things in a DataFrame use ```.loc```:

# Rows 2 to 5 and all columns:
print(df.loc[2:5, :])


# In[12]:


# Rows 2 to 4 and columns selected by name:
print(df.loc[2:4, ('years', 'code')])

# You can get a histogram of particular values in a column:
print(df['names'].value_counts())


######### scikit-learn ###############3

# scikit-learn is great for performing all major data analysis operations. It also contains datasets. In this code, we will load a dataset and fit a simple linear regression (more details on that model later).

from sklearn import datasets as ds

# Load the Boston Housing dataset
dataset = ds.load_boston()

# It is a dictionary, see the keys for details:
print(dataset.keys())


# The 'DESCR' key holds a description text for the whole dataset
print(dataset['DESCR'])

# The data (independent variables) are stored under the 'data' key
# The names of the independent variables are stored in the 'feature_names' key
# Let's use them to create a DataFrame object:
df = pd.DataFrame(data=dataset['data'], columns=dataset['feature_names'])
print(df.head())

# The dependent variable is stored separately
df_y = pd.DataFrame(data=dataset['target'], columns=['target'])
print(df_y.head())

# Now, let's build a linear regression model
from sklearn.linear_model import LinearRegression as LR

# First we create a linear regression object
regression = LR()

# Then, we fit the independent and dependent data
regression.fit(df, df_y)

# We can obtain the R^2 score (more on this later)
print(regression.score(df, df_y))


# Very often, we need to perform an operation on a single observation. In that case, we have to reshape the data using numpy:

# Consider a single observation 
so = df.loc[2, :]
print(so)

# Just the values of the observation without meta data
print(so.values)


# Reshaping yields a new matrix with one row with as many columns as the original observation (indicated by the -1)
# This is often needed to make data compatible with particular methods
print(np.reshape(so.values, (1, -1)))

# For two observations:
so_2 = df.loc[2:3, :]
print(np.reshape(so_2.values, (2, -1)))


# This concludes our quick run-through of some basic functionality of the modules. We will use more and more specialised functions and objects as you progress through the course, but this has already set you up with the basics for playing around with data.
