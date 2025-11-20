#Key/value in Dicts as objects in Series
import pandas as pd
calories = {"day 1": 420, "day 2": 380, "day 3": 600}
my_var = pd.Series(calories)
print(my_var)

my_var = pd.Series(calories, index = ["day 1", "day 2"])
print(my_var)

#Data-Frames, Multidimensional, Rows and Columns creating a table storing data

data ={
    "calories" : [420, 380 , 600],
    "duration" : [50, 40, 45]
}
my_var = pd.DataFrame(data)
print(my_var)