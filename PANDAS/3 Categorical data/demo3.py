# Append new category in python

import pandas as pd

s = pd.Series(["p","q","r","t","q"], dtype="category")
print("\n Category :\n", s)

s = s.cat.add_categories("s")
print("\nUpdated Category:\n",s)

s = s.cat.remove_categories("p")
print("\nUpdated categories:\n",s)