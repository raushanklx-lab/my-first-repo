

# --------------- What is Pandas --------------- #
#
# Pandas is a Python library used for data manipulation and analysis.
# It provides data structures like DataFrames that make it easy to clean, transform, analyze, and summarize large datasets efficiently.
#
# Pandas is an open-source Python library designed for data analysis and data manipulation.
# It allows us to work with structured data using DataFrames and Series, similar to tables in Excel or SQL.
# With Pandas, we can easily perform operations like data cleaning, filtering, grouping, aggregation, and time-series analysis.



# --------------- Why use Pandas --------------- #
#
# We use **Pandas for data analysis because it can easily handle large datasets.**
# With its help, we can **clean, filter, sort, and analyze data** efficiently.
# Compared to normal Python, **Pandas is faster and easier**, which is why it is **widely used in data science and analytics**.



# --------------- Pandas vs NumPy --------------- #
#
# NumPy is mainly for numerical computations on arrays, whereas Pandas is built on top of NumPy and is used for handling tabular data.
# Pandas provides DataFrames which are easy to filter, sort, and analyze, while NumPy is faster for pure number crunching.



# --------------- Pandas vs NumPy --------------- #



# --------------- iloc[] --------------- #
#
# df.iloc[row_positions, column_positions]     # Syntax:
# df.iloc[0]                                   # Single row:
# df.iloc[1,2]  # Row 1, Column 2              # Single element:
# df.iloc[0:2, 0:2]  # Rows 0-1, Columns 0-1   # Multiple rows and columns: 



# --------------- loc[] --------------- #
#
# df.loc[row_labels, column_labels]          # Syntax:
# df.loc[1]                                  # Single row, all columns:
# df.loc[1, 'Name']                          # Single row, specific columns:
# df.loc[[0,2], ['Name','City']]             # Multiple rows and columns:
# df.loc[df['Age'] > 28, ['Name', 'City']]   # Conditional selection:



# --------------- Row Selection --------------- #
#
# df.loc[0]  # First row using index label     # Select single rows:
# df.iloc[1] # Second row using position       # Select single rows:
#
# df.loc[[0, 2]]   # Rows with index 0 and 2                                # Select multiple rows:
# df.iloc[0:2]     # Rows from position 0 to 1 (stop index is exclusive)    # Select multiple rows:



# --------------- Column Selection --------------- #
#
# df['Name']  # Output: Series                  # Single Column:
# df[['Name', 'City']]  # Output: DataFrame     # Multiple Columns:



# --------------- Boolean Indexing --------------- #
#
# df[df['Age'] > 28]  # Returns rows where Age > 28     # Example:                          ## Tips:
# df[(df['Age'] > 25) & (df['City'] == 'Mumbai')]       # Multiple conditions:              ## Use & for AND, | for OR.
# df.loc[df['Age'] > 25, ['Name','City']]               # Can be combined with loc:         ## Wrap each condition in parentheses.



# --------------- Slicing --------------- #
#
# df[0:2]  # Rows 0 and 1 (like iloc)                               # Row slicing:                          # iloc slicing is position-based.
# df.loc[:, 'Name':'City']  # All rows, columns Name to City        # Column slicing (with loc):            # loc slicing is label-based, inclusive
# df.loc[0:1, 'Name':'Age']  # Rows 0-1, columns Name and Age       # Row + Column slicing:                 #  of the last index.
