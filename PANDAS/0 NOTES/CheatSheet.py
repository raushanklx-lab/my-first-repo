# ---------------  ---------------- #


#---------------Q8. Add a New Column  ---------------- #
#
# --------------- Add a New Column using the insert() Method ---------------- #
# DataFrame.insert(Column_POsition, "Column_Name", [Colum_Data ]) 
# DataFrame.insert(     2         ,    "Roll"    , [101, 102, 103, 104, 105] )

# --------------- insert a New Column using the assign() Method ---------------- #
# variable = df_variable( Column_Name = [Column_Data])
# ResDF =    df.assign(Id=["EID01","EID02","EID03","EID04","EID05"])



# ---------------Q9. Delete Rows/Column using Drop() Method  ---------------- #
#
# ---------------  Drop a Column in pandas ---------------- #
# Variable = DataFrame_Variable.drop( "Column_Name" , axis="colummns" / axis=1)
# resDF = df.drop("Rank", axis="columns")
#
# ---------------  Drop a Row in pandas ---------------- #
# Variable = DataFrame_Variable.drop( index_Number" , axis="index" / axis=0)
# resDF = df.drop(2 , axis="index")



# ---------------Q10. Iterate over Rows or Columns  ---------------- #
#
# --------------- Pandas iterrows() to iterate over rows ---------------- #
# for row in df.iterrows():     # Using For loop
#    print("\nIterate over rows: \n", row)
#
# --------------- Pandas itertuples() to iterate over rows ---------------- #
# for row in df.itertuples():     # Using For loop
#     print("\nDisplay records as a tuple object: \n", row)
#
# --------------- Pandas items() to iterate over rows ---------------- #
# for key, values in df.items():
# for a, b in df.items():      # Using For loop with dictionary
#     print(a)
#     print(b)



# ---------------  ---------------- #