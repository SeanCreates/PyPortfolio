import pandas
#Introduction to pandas
#example one
my_dataset = {
    'cars' : ['BMMW', 'RollsRoyce', 'Tesla', 'Ford'],
    'passings' : [3, 7, 5, 6,]
}

my_var = pandas.DataFrame(my_dataset)
print(my_var)

#example two
a = [1,3,5,7]
my_var = pandas.Series(a)
print(my_var)
print(my_var[0])

a = [0, 9, 8, 7]
my_var = pandas.Series(a, index = ["x", "y", "z", "d"])
print(my_var)
print(my_var["y"])




